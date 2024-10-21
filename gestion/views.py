from django.shortcuts import render, redirect
from .forms import *
from .models import *


# CATEGORY

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
                category.name = form.cleaned_data['name']
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
                cat.name = form.cleaned_data['name']
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