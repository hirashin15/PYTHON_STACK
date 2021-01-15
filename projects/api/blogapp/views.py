  
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactModelForm
# Create your views here.

def homepage(request):
	form = ContactModelForm()
	if request.is_ajax():
		form = ContactModelForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({'msg': 'Success'})
	return render(request, 'homepage.html', {'form': form})