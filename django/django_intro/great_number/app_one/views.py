from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def root(request):
  if 'match' not in request.session:
    request.session['match'] = random.randint(1, 100)
  print(request.session['match'], "this is the match*********************************")
  if 'count' not in request.session:
    request.session['count'] = 0
  return render(request, 'index.html')


def process_guess(request):
  if request.POST['guess'] == '':
    print("no guess made")
  else: 
    guess = int(request.POST['guess'])
    print(guess, "This is the guess**************************************")
    if request.session['match'] < guess:
      request.session['result'] = 'Too high'
      request.session['is_match'] = False
    elif request.session['match'] > guess:
      request.session['result'] = 'Too low!'
      request.session['is_match'] = False
    else:
      request.session['result'] = str(guess) + ' was the number!'
      request.session['is_match'] = True
      request.session['display_hidden'] = 'd-hidden'
    request.session['count'] += 1
    
  if request.session['count'] is 5:
    request.session['result'] = 'You Lose!'
    request.session['is_match'] = False
    request.session['display_hidden'] = 'd-hidden'
  print(request.session['count'])
  return redirect('/')

def clear_match(request):
  request.session.clear()
  return redirect('/')