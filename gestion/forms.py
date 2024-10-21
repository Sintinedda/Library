from django import forms
from .models import *


# CATEGORY

class AddCatForm(forms.Form):
    name = forms.CharField(required=True)


class UpdateCatForm(forms.Form):
    name = forms.CharField(required=True)