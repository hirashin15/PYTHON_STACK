from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<id>', views.delete),
    path('ajax', views.ajax_posting, name="ajax_posting")
]
