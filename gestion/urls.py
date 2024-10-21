from django.urls import path
from gestion import views


urlpatterns = [


    # CATEGORY
    path('categorylist/', views.categorylist, name='categorylist'),
    path('addcategory', views.addcategory, name='addcategory'),
    path('updatecategory/<cat>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<cat>/', views.deletecategory, name='deletecategory'),


    #ITEM
    path('<cat>/list/', views.itemlist, name='itemlist'),
    path('<cat>/additem/', views.additem, name='additem'),
    path('<cat>/updateitem/<int:id>/', views.updateitem, name='updateitem'),
    path('<cat>/deleteitem/<int:id>/', views.deleteitem, name='deleteitem'),
]