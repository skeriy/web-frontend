from django import forms
from .models import *


class ListFilmsForm(forms.ModelForm):

    class Meta:
        model = Films
        exclude = [""]