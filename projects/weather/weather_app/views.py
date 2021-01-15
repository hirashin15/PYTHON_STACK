import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.http import JsonResponse

# Create your views here.
def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=071fa982631d36e09402617f08e2b721'

  cities = City.objects.all()
  weather_data = []
  for city in cities: 
    r = requests.get(url.format(city)).json()
    city_weather = {
      'id': city.id,
      'city': city.name,
      'temp': r['main']['temp'],
      'desc': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon'],
    }
    weather_data.append(city_weather)

  context = {
    'weather_data': weather_data,
    'form': CityForm()
  }
  return render(request, 'weather/weather.html', context)

def delete(request, id):
  instance = City.objects.get(id=id)
  instance.delete()
  return redirect('/')

def ajax_posting(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=071fa982631d36e09402617f08e2b721'
  if request.method == 'POST':
    form = CityForm(request.POST)
    if form.is_valid():
      City.objects.create(name=request.POST['name'])
  
  cities = City.objects.all()
  weather_data = []
  for city in cities: 
    r = requests.get(url.format(city)).json()
    city_weather = {
      'id': city.id,
      'city': city.name,
      'temp': r['main']['temp'],
      'desc': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon'],
    }
    weather_data.append(city_weather)

  context = {
    'weather_data': weather_data,
  }
  return render(request, 'weather/cities.html', context)