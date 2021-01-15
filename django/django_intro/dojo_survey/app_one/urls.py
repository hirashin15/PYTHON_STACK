from django.urls import path
from . import views

urlpatterns = [
  path('', views.root),
  path('result', views.form_to_html),
  path('submitted/<name>/<location>/<language>/<comment>', views.submitted)
]