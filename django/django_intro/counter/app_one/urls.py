from django.urls import path
from . import views

urlpatterns = [
  path('', views.root),
  path('destroy_session', views.destroy),
  path('+2', views.add_two),
  path('custom', views.custom_add),
]