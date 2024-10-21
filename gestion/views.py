from django.shortcuts import render, redirect
from unicodedata import category

from .forms import *
from .models import *


                              #CATEGORY

def categorylist(request):
    categories = Category.objects.all()
    return render(request, 'category/catlist.html',
                  {'categories': categories})


def addcategory(request):
    form = AddCatForm(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        if Category.objects.filter(name=name).exists():
            error = 'Cette catégorie existe déjà!!!'
            return render(request, 'category/addcat.html',
                          {'form': form, 'error': error})
        else:
            if form.is_valid():
                category = Category()
                category.name = form.cleaned_data['nom']
                category.save()
                return redirect('categorylist')
    else:
        return render(request, 'category/addcat.html',
                      {'form': form})


def updatecategory(request, cat):
    form = UpdateCatForm(request.POST)
    cat = Category.objects.get(name=cat)
    if request.method == 'POST':
        name = request.POST.get('name')
        if Category.objects.filter(name=name).exists():
            error = 'Cette catégorie existe déjà!!!'
            return render(request, 'category/updatecat.html',
                          {'cat': cat, 'form': form, 'error': error})
        else:
            if form.is_valid():
                cat.name = form.cleaned_data['nom']
                cat.save()
                return redirect('categorylist')
    else:
        return render(request, 'category/updatecat.html',
                      {'cat': cat, 'form': form})


def deletecategory(request, cat):
    cat = Category.objects.get(name=cat)
    if request.method == 'POST':
        cat.delete()
        return redirect('categorylist')
    else:
        return render(request, 'category/deletecat.html',
                      {'cat': cat})



                                # ITEM

def itemlist(request, cat):
    cat = Category.objects.get(name=cat)
    items = Item.objects.filter(category__name=cat)
    return render(request, 'item/itemlist.html',
                  {'items': items, 'cat': cat})


def additem(request, cat):
    cat = Category.objects.get(name=cat)
    form = AddItemForm(request.POST)
    if request.method == 'POST':
        name = request.POST.get('nom')
        author = request.POST.get('auteur')
        if Item.objects.filter(name=name, author=author).exists():
            error = 'Cet item existe déjà!!!'
            return render(request, 'item/additem.html',
                          {'form': form, 'cat': cat, 'error': error})
        else:
            if form.is_valid():
                item = Item()
                item.name = form.cleaned_data['nom']
                item.author = form.cleaned_data['auteur']
                item.category = Category.objects.get(pk=cat.id)
                item.save()
                return redirect('itemlist', cat)
    else:
        return render(request, 'item/additem.html',
                      {'form': form, 'cat': cat})


def updateitem(request, cat, id):
    cat = Category.objects.get(name=cat)
    item = Item.objects.get(pk=id)
    form = UpdateItemForm(request.POST)
    if request.method == 'POST':
        name = request.POST.get('nom')
        author = request.POST.get('auteur')
        if Item.objects.filter(name=name, author=author).exists():
            error = 'Cet item existe déjà!!!'
            return render(request, 'item/updateitem.html',
                          {'cat': cat, 'item': item, 'form': form, 'error': error})
        else:
            if form.is_valid():
                item.name = form.cleaned_data['nom']
                item.author = form.cleaned_data['auteur']
                item.category = form.cleaned_data['categorie']
                item.save()
                return redirect('itemlist', cat)
    else:
        return render(request, 'item/updateitem.html',
                      {'cat': cat, 'item': item, 'form': form})


def deleteitem(request, cat, id):
    cat = Category.objects.get(name=cat)
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('itemlist', cat)
    else:
        return render(request, 'item/deleteitem.html',
                      {'cat': cat, 'item': item})