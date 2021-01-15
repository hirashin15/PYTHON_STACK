from django.shortcuts import render, HttpResponse, redirect

def root(request):
  return render(request, 'index.html')

def form_to_html(request):
  name = request.POST['name']
  location = request.POST['location']
  language = request.POST['language']
  comment = request.POST['comment']
  return redirect(f'/submitted/{name}/{location}/{language}/{comment}')

def submitted(request, name, location, language, comment):
  content = {
    'name': name,
    'location': location,
    'language': language,
    'comment': comment
  }
  return render(request, 'submitted.html', content)