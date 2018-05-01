from django.shortcuts import render
from .forms import ListFilmsForm
from .models import Films


# Create your views here.

def landing(request):
    name = 'Cod'
    form = ListFilmsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["director"])

        new_form = form.save()

    query_results = Films.objects.all()

    return render(request, 'landing/landing.html', locals())
