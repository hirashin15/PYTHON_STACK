from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.
def root(request):
  content = {
    "all_users": User.objects.all() 
  }
  return render(request, 'index.html', content)

def process(request):
  post_first = request.POST["first"]
  post_last = request.POST["last"]
  post_email = request.POST["email"]
  post_age = request.POST["age"]

  User.objects.create(first_name=post_first, last_name=post_last, email_address=post_email, age=post_age)
  return redirect('/')
