from django.urls import path
from . import views

urlpatterns = [
  path('', views.root),
  path('process_guess', views.process_guess),
  path('clear', views.clear_match)
]