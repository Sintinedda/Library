from django import forms
from gestion.models import Member


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True, label="Nom d'utilisateur")
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput,
                               required=True)


                                          # MEDIA

class AddItemForm(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    author = forms.CharField(required=True, label="Auteur")
    parution = forms.DateField(required=True, label="Date de parution", widget=forms.DateInput,
                               help_text='La date doit être au format AAAA-MM-JJ')


class EditItemForm(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    author = forms.CharField(required=True, label="Auteur")
    parution = forms.DateField(required=True, label="Date de parution", widget=forms.DateInput,
                               help_text='La date doit être au format AAAA-MM-JJ')


                                        # MEMBER

class AddMembForm(forms.Form):
    firstname = forms.CharField(required=True, label="Prénom")
    lastname = forms.CharField(required=True, label="Nom")


class EditMembForm(forms.Form):
    firstname = forms.CharField(required=True, label="Prénom")
    lastname = forms.CharField(required=True, label="Nom")


                                        # LOAN

class LendItemForm(forms.Form):
    member = forms.ModelChoiceField(queryset=Member.objects.filter(blocked=False),
                                    required=True, label='Membre')