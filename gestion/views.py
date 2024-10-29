from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *



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


                                     # MEDIAS

@login_required
def categories(request):
    cats = Item.CAT_CHOICES
    return render(request, 'gestion/item/cat_list.html',
                  {'cats': cats})


@login_required
def cat(request, cat):
    category = Item.CAT_CHOICES[cat]
    c = category.lower()
    m = ContentType.objects.get(model=c)
    model = m.model_class()
    items = model.objects.all()
    loans = Loan.objects.all()
    return render(request, 'gestion/item/lists.html',
                  {'cat': category, 'items': items, 'loans': loans})


@login_required
def add_item(request, cat):
    category = Item.CAT_CHOICES[cat]
    c = category.lower()
    m = ContentType.objects.get(model=c)
    model = m.model_class()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        name = request.POST['name']
        if model.objects.filter(name=name, category=category).exists():
            err = 'Cet item existe déjà'
            return render(request, 'gestion/item/add.html',
                          {'form': form, 'err': err, 'cat': category})
        else:
            if form.is_valid():
                m = model()
                m.name = form.cleaned_data['name']
                m.parution = form.cleaned_data['parution']
                m.category = cat
                if category == 'Livre':
                    m.author = form.cleaned_data['author']
                    m.save()
                    return redirect('cat', cat)
                elif category == 'Cd':
                    m.interpreter = form.cleaned_data['author']
                    m.save()
                    return redirect('cat', cat)
                elif category == 'Dvd':
                    m.realisator = form.cleaned_data['author']
                    m.duration = form.data['duration']
                    m.save()
                    return redirect('cat', cat)
                elif category == 'Tabletop':
                    m.creator = form.cleaned_data['author']
                    m.save()
                    return redirect('cat', cat)
            else:
                err = "Un des champs requis n'est pas bien renseigné"
                return render(request, 'gestion/item/add.html',
                              {'form': form, 'err': err, 'cat': category})
    else:
        form = AddItemForm()
        if category == 'Cd':
            form.fields['author'].label = 'Interprète'
            return render(request, 'gestion/item/add.html',
                          {'form': form, 'cat': category})
        elif category == 'Dvd':
            form.fields['author'].label = 'Réalisateur'
            return render(request, 'gestion/item/add.html',
                          {'form': form, 'cat': category})
        elif category == 'Tabletop':
            form.fields['author'].label = 'Créateur'
            return render(request, 'gestion/item/add.html',
                          {'form': form, 'cat': category})
        else:
            return render(request, 'gestion/item/add.html',
                          {'form': form, 'cat': category})


@login_required
def edit_item(request, cat, id):
    category = Item.CAT_CHOICES[cat]
    c = category.lower()
    m = ContentType.objects.get(model=c)
    model = m.model_class()
    item = model.objects.get(pk=id)
    if request.method == 'POST':
        form = EditItemForm(request.POST)
        name = request.POST['name']
        if model.objects.filter(name=name, category=category).exists():
            err = 'Cet item existe déjà'
            return render(request, 'gestion/item/edit.html',
                          {'form': form, 'err': err, 'cat': category, 'item': item})
        else:
            if form.is_valid():
                item.name = form.cleaned_data['name']
                item.parution = form.cleaned_data['parution']
                item.category = cat

                if category == 'Livre':
                    item.author = form.cleaned_data['author']
                    item.save()
                    return redirect('cat', cat)
                elif category == 'Cd':
                    item.interpreter = form.cleaned_data['author']
                    item.save()
                    return redirect('cat', cat)
                elif category == 'Dvd':
                    item.realisator = form.cleaned_data['author']
                    item.duration = form.data['duration']
                    item.save()
                    return redirect('cat', cat)
                elif category == 'Tabletop':
                    item.creator = form.cleaned_data['author']
                    item.save()
                    return redirect('cat', cat)
            else:
                err = "Un des champs requis n'est pas bien renseigné"
                return render(request, 'gestion/item/edit.html',
                              {'form': form, 'err': err, 'cat': category, 'item': item})
    else:
        form = EditItemForm()
        if category == 'Cd':
            form.fields['author'].label = 'Interprète'
            return render(request, 'gestion/item/edit.html',
                          {'form': form, 'cat': category, 'item': item})
        elif category == 'Dvd':
            form.fields['author'].label = 'Réalisateur'
            return render(request, 'gestion/item/edit.html',
                          {'form': form, 'cat': category, 'item': item})
        elif category == 'Tabletop':
            form.fields['author'].label = 'Créateur'
            return render(request, 'gestion/item/edit.html',
                          {'form': form, 'cat': category, 'item': item})
        else:
            return render(request, 'gestion/item/edit.html',
                          {'form': form, 'cat': category, 'item': item})


@login_required()
def del_item(request, cat, id):
    category = Item.CAT_CHOICES[cat]
    c = category.lower()
    m = ContentType.objects.get(model=c)
    model = m.model_class()
    item = model.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('cat', cat)
    else:
        return render(request, 'gestion/item/del.html',
                      {'cat': category, 'item': item})


@login_required
def card_item(request, cat, id):
    category = Item.CAT_CHOICES[cat]
    c = category.lower()
    m = ContentType.objects.get(model=c)
    model = m.model_class()
    item = model.objects.get(pk=id)
    loans = Loan.objects.filter(item=item)
    return render(request, 'gestion/item/card.html',
                  {'cat': category, 'item': item, 'loans': loans})