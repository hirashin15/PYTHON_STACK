from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.template.defaulttags import register

# Create your views here.
def root(request):
  return render(request, 'index.html')

@register.filter(name='times')
def times(value):
  return range(value)

def register(request):
  errors = User.objects.reg_Validator(request.POST)
  if len(errors) > 0:
    for val in errors.values():
      messages.error(request, val)
    return redirect('/')
  else:
    password = request.POST["password"]
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
      name = request.POST["name"],
      alias = request.POST["alias"],
      email = request.POST["email"],
      password = hashed
    )
    request.session["id"] = user.id
    messages.success(request, "Successfully registered!")
  return redirect('/books')

def login(request):
  errors = User.objects.login_validator(request.POST)
  if len(errors) > 0:
    for val in errors.values():
      messages.error(request, val)
    return redirect('/')
  else:
    find_user = User.objects.filter(email=request.POST["email"])
    if find_user:
      logged_user = find_user[0]
      if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
        request.session["id"] = logged_user.id
      else:
        messages.error(request, "Login failed. Try again")
        return redirect('/')
  return redirect('/books')

# **************************************

def books(request):
  context = {
    "user_logged": User.objects.get(id=request.session["id"]),
    "authors": Author.objects.all(),
    "first_3_reviews": Review.objects.all().order_by('-id')[0:3],
    "rest_of_reviews": Review.objects.all().order_by('-id')[3:]
  }
  return render(request, 'books.html', context)

# ***************************************
def add_page(request):
  context = {
    "authors": Author.objects.all()
  }
  return render(request, 'add_review_page.html', context)

def add_review(request):
  all_books = Book.objects.all()
  all_authors = Author.objects.all()
  all_reviews = Review.objects.all()
  this_user = User.objects.get(id=request.session["id"])
  # book_errors = Book.objects.book_validator(request.POST)
  # review_errors = Review.objects.review_validator(request.POST)


  # if len(book_errors) > 0 or len(review_errors) > 0:
  #   for val in book_errors.values():
  #     messages.error(request, val)
  #   for val in review_errors.values():
  #     messages.error(request, val)
  #   return redirect('/add_review')

  this_book = request.POST["title"]
  this_book_filter = all_books.filter(title=this_book)
  if this_book_filter:
    book_id = this_book_filter[0].id
    add_book = Book.objects.get(id=book_id)
  else:
    add_book = Book.objects.create(title=this_book)
    book_id = add_book.id

  create_author = request.POST["create_author"]
  if create_author:
    for author in all_authors:
      if author.name == create_author:
        messages.error(request, "Author already exists in database.")
      return redirect("/books/add")
    add_author = Author.objects.create(name=create_author)
  else:
    author_id = request.POST["select_author"]
    add_author = Author.objects.get(id=author_id)
  add_book.authors.add(add_author)

  book_review = request.POST["review"]
  book_rating = request.POST["rating"]
  Review.objects.create(text=book_review, rating=book_rating, review_by=this_user, review_for=add_book)
  return redirect(f'/book_info/{book_id}')

# ***************************************

def book_info_page(request, id):
  context = {
    "this_user": User.objects.get(id=request.session["id"]),
    "this_book": Book.objects.get(id=id),
    "reviews": Review.objects.all()
  }
  return render(request, 'book_info.html', context)

def add_just_review(request, id):
  this_user = User.objects.get(id=request.session["id"])
  this_book = Book.objects.get(id = id)
  book_review = request.POST["review"]
  book_rating = request.POST["rating"]

  Review.objects.create(text=book_review, rating=book_rating, review_by=this_user, review_for=this_book)
  return redirect(f"/book_info/{id}")

def delete_review(request, review_id, book_id):
  Review.objects.get(id=review_id).delete()
  return redirect(f'/book_info/{book_id}')

# *****************************************************************
def user_profile(request, id):
  this_user = User.objects.get(id=id)
  review_length = len(this_user.reviews_by_user.all())

  context = {
    "this_user": this_user,
    "review_length": review_length
  }
  return render(request, 'user_profile.html', context)


def logout(request):
  request.session.flush()
  return redirect('/')