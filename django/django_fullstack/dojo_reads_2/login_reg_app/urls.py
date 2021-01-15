from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('reg_process', views.reg_process),
    path('login', views.login),
    path('logout', views.logout),
    path('delete/<id>', views.delete),
    path('success', views.success),
]