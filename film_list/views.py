from django.shortcuts import render
from .forms import *
from .models import Films


# Create your views here.

def landing(request):
    form_add = ListFilmsForm()
    form_del = FilmsDel()

    if request.POST is None:
        form_add = ListFilmsForm(request.POST)
        form_del = FilmsDel(request.POST)

    if request.method == "POST":
        if 'add_button' in request.POST:
            form_add = ListFilmsForm(request.POST)
            if form_add.is_valid():
                form_add.save()
                print(request.POST)
                print(form_add.cleaned_data)
                data = form_add.cleaned_data
                print(data["director"])
                print('post add')
        elif 'delete_button' in request.POST:
            form_del = FilmsDel(request.POST)
            if form_del.is_valid():
                id_del = form_del.cleaned_data.get('id', None)
                print('post del')
                Films.objects.filter(id=id_del).delete()

    query_results = Films.objects.all()

    print('end')
    return render(request, 'landing/landing.html', locals())
