from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('reg_process', views.reg_process),
    path('login', views.login),
    path('logout', views.logout),
    path('wall', views.wall),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    # path('delete', views.delete),
]