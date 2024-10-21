from django.urls import path
from gestion import views


urlpatterns = [

    # CATEGORY
    path('category/', views.categorylist, name='categorylist'),
    path('category/addcategory', views.addcategory, name='addcategory'),
    path('category/updatecategory/<cat>/', views.updatecategory, name='updatecategory'),
    path('category/deletecategory/<cat>/', views.deletecategory, name='deletecategory')
]