from django.shortcuts import render, HttpResponse, redirect

def root(request):
  if 'count' in request.session:
    print('key exists')
    request.session['count'] += 1
  else:
    print('key does not exist')
    request.session['count'] = 1
  if 'total' in request.session:
    request.session['total'] += 1
  else:
    request.session['total'] = 1
  return render(request, 'index.html')


def destroy(request):
  del request.session['count']
  return redirect('/')

def add_two(request):
  request.session['count'] += 1
  return redirect('/')

def custom_add(request):
  request.session['count'] += int(request.POST['increment']) - 1
  return redirect('/')