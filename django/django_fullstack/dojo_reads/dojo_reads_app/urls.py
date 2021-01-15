from django.urls import path
from . import views

urlpatterns = [
  path('', views.root),
  path('register', views.register),
  path('login', views.login),
  path('books', views.books),
  path('books/add', views.add_page),
  path('add_review', views.add_review),
  path('book_info/<id>', views.book_info_page),
  path('book_info/add_review/<id>', views.add_just_review),
  path('user/<id>', views.user_profile),
  path('delete/<review_id>/<book_id>', views.delete_review),

  
  path('logout', views.logout),
]