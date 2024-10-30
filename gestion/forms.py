from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True, label="Nom d'utilisateur")
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput,
                               required=True)


                                          # MEDIA

class AddItemForm(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    author = forms.CharField(required=True, label="Auteur")
    parution = forms.DateField(required=True, label="Date de parution", widget=forms.DateInput)


class EditItemForm(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    author = forms.CharField(required=True, label="Auteur")
    parution = forms.DateField(required=True, label="Date de parution", widget=forms.DateInput)


                                        # MEMBER

class AddMembForm(forms.Form):
    firstname = forms.CharField(required=True, label="Prénom")
    lastname = forms.CharField(required=True, label="Nom")


class EditMembForm(forms.Form):
    firstname = forms.CharField(required=True, label="Prénom")
    lastname = forms.CharField(required=True, label="Nom")