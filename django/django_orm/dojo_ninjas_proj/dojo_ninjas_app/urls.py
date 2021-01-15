from django.urls import path
from . import views

urlpatterns = [
  path('', views.root),
  path('process', views.process),
  path('delete', views.delete),
]