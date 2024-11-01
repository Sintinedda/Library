from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.view_login, name='login'),

    path('', views.gestion_menu, name='gestion_menu'),


# MEDIA
    path('categories/', views.cat_list, name='cat_list'),
    path('liste/<cat>/', views.item_lists, name='item_lists'),
    path('ajouter/<cat>/', views.add_item, name='add_item'),
    path('editer/<cat>/<int:id>/', views.edit_item, name='edit_item'),
    path('supprimer/<cat>/<int:id>/', views.del_item, name='del_item'),


# MEMBER
    path('membres/', views.memb_list, name='memb_list'),
    path('membres/ajouter/', views.add_memb, name='add_memb'),
    path('membres/editer/<int:id>/', views.edit_memb, name='edit_memb'),
    path('membres/supprimer/<int:id>/', views.del_memb, name='del_memb'),
    path('membres/<int:id>/', views.card_memb, name='card_memb'),


# LOAN
    path('preter/<cat>/<int:id>/', views.lend_item, name='lend_item'),
    path('retour/<cat>/<int:id>/', views.return_item, name='return_item'),
]