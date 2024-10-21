from django.urls import path
from gestion import views


urlpatterns = [


    # CATEGORY
    path('categorylist/', views.categorylist, name='categorylist'),
    path('addcategory', views.addcategory, name='addcategory'),
    path('updatecategory/<cat>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<cat>/', views.deletecategory, name='deletecategory'),


    # ITEM
    path('<cat>/list/', views.itemlist, name='itemlist'),
    path('<cat>/additem/', views.additem, name='additem'),
    path('<cat>/updateitem/<int:id>/', views.updateitem, name='updateitem'),
    path('<cat>/deleteitem/<int:id>/', views.deleteitem, name='deleteitem'),


    # MEMBER
    path('memberlist/', views.memberlist, name='memberlist'),
    path('addmember/', views.addmember, name='addmember'),
    path('updatemember/<int:id>/', views.updatemember, name='updatemember'),
    path('deletemember/<int:id>', views.deletemember, name='deletemember'),
]