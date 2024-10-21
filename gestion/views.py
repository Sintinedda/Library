from django.shortcuts import render, redirect
from .forms import *
from .models import *


                                                  # CATEGORY

def categorylist(request):
    categories = Category.objects.all()
    return render(request, 'category/catlist.html',
                  {'categories': categories})


def addcategory(request):
    if request.method == 'POST':
        form = AddCatForm(request.POST)
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
        form = AddCatForm()
        return render(request, 'category/addcat.html',
                      {'form': form})


def updatecategory(request, cat):
    cat = Category.objects.get(name=cat)
    if request.method == 'POST':
        form = UpdateCatForm(request.POST)
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
        form = UpdateCatForm()
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
    if request.method == 'POST':
        form = AddItemForm(request.POST)
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
        form = AddItemForm()
        return render(request, 'item/additem.html',
                      {'form': form, 'cat': cat})


def updateitem(request, cat, id):
    cat = Category.objects.get(name=cat)
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        form = UpdateItemForm(request.POST)
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
        form = UpdateItemForm()
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


                                         # MEMBER

def memberlist(request):
    members = Member.objects.all()
    return render(request, 'member/memberlist.html',
                  {'members': members})


def addmember(request):
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        firstname = request.POST.get('prenom')
        lastname = request.POST.get('nom')
        if Member.objects.filter(firstname=firstname, lastname=lastname):
            error = 'Ce membre existe déjà!!!'
            return render(request, 'member/addmember.html',
                          {'form': form, 'error': error})
        else:
            if form.is_valid():
                member = Member()
                member.firstname = form.cleaned_data['prenom']
                member.lastname = form.cleaned_data['nom']
                member.save()
                return redirect('memberlist')
    else:
        form = AddMemberForm()
        return render(request, 'member/addmember.html',
                      {'form': form})


def updatemember(request, id):
    member = Member.objects.get(pk=id)
    if request.method == 'POST':
        form = UpdateMemberForm(request.POST)
        firstname = request.POST.get('prenom')
        lastname = request.POST.get('nom')
        if Member.objects.filter(firstname=firstname, lastname=lastname):
            error = 'Ce membre existe déjà!!!'
            return render(request, 'member/updatemember.html',
                          {'form': form, 'member': member, 'error': error})
        else:
            if form.is_valid():
                member.firstname = form.cleaned_data['prenom']
                member.lastname = form.cleaned_data['nom']
                member.save()
                return redirect('memberlist')
    else:
        form = UpdateMemberForm()
        return render(request, 'member/updatemember.html',
                      {'form': form, 'member': member})


def deletemember(request, id):
    member = Member.objects.get(pk=id)
    if request.method == 'POST':
        member.delete()
        return redirect('memberlist')
    else:
        return render(request, 'member/deletemember.html',
                      {'member': member})