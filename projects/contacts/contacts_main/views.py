from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ContactModelForm
from .models import Contact
# Create your views here.

def contacts(request):
  form = ContactModelForm()
  print("This is the start>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  if request.method == 'POST':
    print("I entered method == post >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    form = ContactModelForm(request.POST)
    print(form)
    if form.is_valid():
      print("I entered is_valid>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      form.save()
  context = {
    'contacts': Contact.objects.all(),
    'contacts_form': form
  }
  return render(request, 'contacts.html', context)