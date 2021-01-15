from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt



def index(request):
	return render(request, "login.html")


def reg(request):

    errors = User.objects.Uservalidator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/')
    else:
        hashed = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST["fname"], 
            last_name = request.POST["lname"],
            email = request.POST["email"],
            password = hashed,
        )
        request.session['id'] = user.id
        return redirect('/books')

def login(request):
    errors = User.objects.loginvalidator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/')
        
    user = User.objects.filter(email=request.POST["email"])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect("/books")


def books(request):
    context = {
        "the_person": User.objects.get(id=request.session['id']),
        "books": Book.objects.all()
    }
    return render(request, "welcome.html", context)

def addbook(request):
    errors = Book.objects.Bookvalidator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
    else:
        Book.objects.create(
            title = request.POST["title"],
            desc = request.POST["desc"],
            upload = User.objects.get(id = request.session['id']),
        )
    return redirect('/books')

def bookinfo(request, id):
    context = {
        "book": Book.objects.get(id = id),
        "the_person": User.objects.get(id=request.session['id']),
    }
    return render(request, "book_info.html", context)

def update(request, id):
    errors = Book.objects.Bookvalidator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
        return redirect(f'/books/{id}')
        
    this_book = Book.objects.get(id=id)
    this_book.title = request.POST["title"]
    this_book.desc = request.POST["desc"]
    this_book.save()
    return redirect(f"/books/{id}")

def favorite(request, id):
    this_person = User.objects.get(id=request.session["id"])
    book_to_add = Book.objects.get(id = id)
    this_person.userfavs.add(book_to_add)
    return redirect(f"/books/{id}")


def unfavorite(request, id):
    this_person = User.objects.get(id=request.session["id"])
    this_book = Book.objects.get(id=id)
    this_person.userfavs.remove(this_book)
    return redirect(f"/books/{id}")


def delete(request, id):
    d = Book.objects.get(id = id)
    d.delete()
    return redirect("/books")

def logout(request):
    request.session.flush()
    return redirect("/")