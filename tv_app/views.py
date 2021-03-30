from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show
def rendercreate(request):
    return render(request, 'create.html')

def create(request):
    errors = Show.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/shows/')

    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description']
    )
    print(Show.objects.all())
    return redirect('/shows/read')

def read(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'read.html', context)

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html', context)

def renderupdate(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'update.html', context)

def update(request, show_id):
    to_update = Show.objects.get(id=show_id)
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/shows/read')

def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')