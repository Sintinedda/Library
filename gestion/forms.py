from django import forms
from .models import *


                                      # CATEGORY

class AddCatForm(forms.Form):
    nom = forms.CharField(required=True)


class UpdateCatForm(forms.Form):
    nom = forms.CharField(required=True)


                                         # ITEM

class AddItemForm(forms.Form):
    nom = forms.CharField(required=True)
    auteur = forms.CharField(required=True)


class UpdateItemForm(forms.Form):
    nom = forms.CharField(required=True)
    auteur = forms.CharField(required=True)
    categorie = forms.ModelChoiceField(queryset=Category.objects.all())