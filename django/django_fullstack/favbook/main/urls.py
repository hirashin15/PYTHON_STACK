from django.urls import path
from . import views


urlpatterns = [
	path('', views.index),
    path('books', views.books),
    path('login', views.login),
    path('reg', views.reg),
    path('add_book', views.addbook),
    path('books/<id>', views.bookinfo),
    path('delete/<id>', views.delete),
    path('favorite/<id>', views.favorite),
    path('unfavorite/<id>', views.unfavorite),
    path('update/<id>', views.update),
    path('logout', views.logout),
]