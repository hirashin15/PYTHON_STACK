from django.shortcuts import render, redirect
from login_reg_app.models import User
from .models import *

# Create your views here.

def books(request):
    context = {
        "myuser" : User.objects.get(id = request.session['user_id'])
    }
    return render(request, "books.html", context)
