from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
		path('shows', views.shows_main),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<id>', views.show_info_page),
		path('shows/<id>/edit', views.edit_page),
		path('shows/<id>/update', views.edit_page_process),
		path('shows/<id>/destroy', views.destroy),
]