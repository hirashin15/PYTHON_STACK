from django.shortcuts import render, redirect
from time import strftime, localtime
import random

# Create your views here.
def root(request):
  if 'content' not in request.session:
    request.session['content'] = ''
  if 'which_form' not in request.session:
    request.session['which_form'] = ''
  if 'total_gold' not in request.session:
    request.session['total_gold'] = 0
  return render(request, 'index.html')

def process(request):
  gold_won=0
  if request.POST['which_form'] == 'farm':
    gold_won = random.randint(10, 20)
  elif request.POST['which_form'] == 'cave':
    gold_won = random.randint(5, 10)
  elif request.POST['which_form'] == 'house':
    gold_won = random.randint(2, 5)
  elif request.POST['which_form'] == 'casino':
    gold_won = random.randint(-50, 50)
  
  location = request.POST['which_form']
  date_time = strftime("%Y/%m/%d %I:%M %p", localtime())
  request.session['total_gold'] += gold_won

  if gold_won < 0:
    request.session['content'] += f'<p class="red">Entered a {location} and lost {gold_won} golds...Ouch..{date_time}</p>'
  else:
    request.session['content'] += f'<p class="green">Earned {gold_won} golds from the {location}! {date_time}</p>'
  return redirect('/')

def clear(request):
  request.session.clear()
  return redirect('/')