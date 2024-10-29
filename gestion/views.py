from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *



def view_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gestionmenu')
        else:
            errmsg = "Les identifiants ne sont pas corrects"
            return render(request, 'registration/login.html',
                          {'form': form, 'errmsg': errmsg})
    else:
        form = LoginForm()
        return render(request, 'registration/login.html',
                      {'form': form})


@login_required
def gestion_menu(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return render(request, 'gestion/menu.html')
