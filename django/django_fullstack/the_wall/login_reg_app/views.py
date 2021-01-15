from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt



def root(request):
    return render(request, 'index.html')

def reg_process(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/')
        
    else:
        password = request.POST["password"]
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        User.objects.create(
            fname = request.POST["fname"],
            lname = request.POST["lname"],
            email = request.POST["email"],
            hashpw = hashed,
        )
        messages.success(request, "Successfully registered. Please login.")
        return redirect ('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/')

    user = User.objects.filter(email=request.POST['email']) 
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.hashpw.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/wall')
    else:
        messages.error(request, "Login failed. Try again.")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')


# *******************************************



def wall(request):
    context = {
        "message": Message.objects.all(),
        "user": User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'thewall.html', context)


def post_message(request):
    print("100"*30)
    Message.objects.create(
        message = request.POST["post_message"],
        message_by = User.objects.get(id=request.POST["user_id"]),
    )
    return redirect('/wall')

def post_comment(request):
    Comment.objects.create(
        comment = request.POST["post_comment"],
        comment_by = User.objects.get(id= request.session['user_id']),
        comment_for = Message.objects.get(id = request.POST['msg_id']),
    )
    return redirect('/wall')
    
#     thisid = comments.message_id
#     context = {
#         "comment_in_messages": Comment.objects.filter(user_id = thisid)
#     }
#     return redirect('thewall.html')




# def delete(request):
#     # d = Comment.objects.get(id = request.POST['post_comment'])
#     return redirect("/wall")