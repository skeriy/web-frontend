from django import forms
from .models import *
from django.utils.translation import ugettext as _


class ListFilmsForm(forms.ModelForm):

    class Meta:
        model = Films
        exclude = [""]


class FilmsDel(forms.Form):
    id = forms.CharField(label='id', max_length=10)
