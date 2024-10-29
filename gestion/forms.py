from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True, label="Nom d'utilisateur")
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput,
                               required=True)


                                          # MEDIAS

class AddItemForm(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    author = forms.CharField(required=True, label="Auteur")
    parution = forms.DateField(required=True, label="Date de parution", widget=forms.DateInput)


class EditItemForm(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    author = forms.CharField(required=True, label="Auteur")
    parution = forms.DateField(required=True, label="Date de parution", widget=forms.DateInput)