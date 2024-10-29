from django.urls import path
from . import views


urlpatterns = [

path('login/', views.view_login, name='login'),

    path('', views.gestion_menu, name='gestionmenu'),
]