from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True, label="Nom d'utilisateur")
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput,
                               required=True)