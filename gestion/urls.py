from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.view_login, name='login'),

    path('', views.gestion_menu, name='gestionmenu'),


# MEDIAS
    path('categories/', views.categories, name='categories'),
    path('<cat>/', views.cat, name='cat'),
    path('<cat>/ajouter/', views.add_item, name='add_item'),
    path('<cat>/editer/<int:id>/', views.edit_item, name='edit_item'),
    path('<cat>/supprimer/<int:id>/', views.del_item, name='del_item'),
    path('<cat>/<int:id>/', views.card_item, name='card_item'),
]