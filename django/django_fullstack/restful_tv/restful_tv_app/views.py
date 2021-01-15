from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import TVshow, Network
import datetime


def home(request):
    return redirect("/shows")

def shows_main(request):
    context = {
		"tvshows" : TVshow.objects.all(),
    }
    return render(request, "main.html", context)


def show_info_page(request, id):
    context = {
        "tvshow" : TVshow.objects.get(id=id),
        "tvshow_list" : TVshow.objects.all()
    }
    return render(request, "showinfo.html", context)


def edit_page(request, id):
    context = {
        "tvshow" : TVshow.objects.get(id=id),
        "tvshow_list" : TVshow.objects.all()
    }
    return render(request, "editpage.html", context)


def edit_page_process(request, id):
    errors = TVshow.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return (f'/shows/{id}/edit')
    else:
        the_show = TVshow.objects.get(id=id)
        the_show.title = request.POST["title"]
        the_show.network = request.POST["network"]
        the_show.release = request.POST["date"]
        the_show.desc = request.POST["desc"]
        the_show.save()
    
    return redirect(f'/shows/{id}')


def new_show(request):
    context = {
		"network_list" : Network.objects.all()
    }
    return render(request, 'newshow.html', context)

def create_show(request):
    errors = TVshow.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST["title"]
        release = request.POST["date"]
        desc = request.POST["desc"]
        network = Network.objects.get(id=request.POST["network"])
        
        #Creating the new TV show
        new_show = TVshow.objects.create(title = title, release = release, desc = desc)
        id = new_show.id
        
        #New TV show is being added into the network
        new_show.networks.add(network)
    return redirect(f'/shows/{id}')


def destroy(request, id):
    d = TVshow.objects.get(id = id)
    d.delete()
    
    return redirect("/shows")