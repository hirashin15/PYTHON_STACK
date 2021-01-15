\\\\\\\\\ VERY IMPORTANT REMINDER ////////////////////////////////////////////////
\\\\\\\\\\\\\\\\\\\\\/////////////////////////////////////////////////////////////
\\\\\\\\\\\ Project settings.py //////////////////////////////////////////////////

INSTALLED APPS = [
	'login_reg_app',
	'django.contrib.admin',
	'django.contrib.auth',
	...
	'your_app_name_here',
]


\\\\\\\\\\  Project urls.py //////////////////////////////////////////////////////

from django.urls import path, include

urlpatterns = [
	path('', include('login_reg_app.urls')),
	path('', include('your_app_name_here.urls')),
]


\\\\\\\\\\ Your_App models.py /////////////////////////////////////////////////////

from django.db import models
from login_reg_app.models import User


\\\\\\\\\\ Your_App urls.py (to be created) ///////////////////////////////////////

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
]


\\\\\\\\\\ Your_App views.py //////////////////////////////////////////////////////

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return HttpResponse("Some string!")


\\\\\\\\\\ Additional Commands ////////////////////////////////////////////////////

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py flush

\\\\\\\\\\ Adding CSS/Script //////////////////////////////////////////////////////

{% load static %}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href={% static 'css/style.css' %}>
<script src="{% static 'js/script.js' %}"></script>


side note: (css/script files goes into static/css or /script folder) 
