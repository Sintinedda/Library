from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_viewer, name='home_viewer'),
    path('liste/<cat>/', views.lists_viewer, name='lists_viewer'),
]
