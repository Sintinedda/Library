from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from gestion.models import *


def home_viewer(request):
    cats = Item.CAT_CHOICES
    return render(request, 'viewer/cat_list.html',
                  {'cats': cats})


def lists_viewer(request, cat):
    category = Item.CAT_CHOICES[cat]
    c = category.lower()
    m = ContentType.objects.get(model=c)
    model = m.model_class()
    items = model.objects.filter(category=category, available=True)
    return render(request, 'viewer/item_lists.html',
                  {'items': items, 'cat': cat})