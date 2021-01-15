from django.shortcuts import render, redirect, HttpResponse
from .models import Dojo, Ninja

# Create your views here.
def root(request):
  context = {
    "dojo_ninja_list": Dojo.objects.all()
  }
  return render(request, 'index.html', context)

def process(request):
  if request.POST["form_type"] == "dojo":
    Dojo.objects.create(
      name = request.POST["name"],
      city = request.POST["city"],
      state = request.POST["state"]
    )
  else:
    Ninja.objects.create(
      first_name = request.POST["fname"],
      last_name = request.POST["lname"],
      dojo_id = Dojo.objects.get(city=request.POST["dojo"])
    )
  return redirect('/')

def delete(request):
  city_name = request.POST["delete"]
  Dojo.objects.get(city=city_name).delete()
  return redirect('/')