from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def root(request):
  return redirect('/time_display')

def display(request):
  context = {
    "date": strftime("%b %d, %Y"),
    "time": strftime("%I:%M %p", localtime())
  }
  return render(request, 'index.html', context)