from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('add1',views.add1,name='add1'),
    path('edit/<id>',views.edit,name='edit'),
    path('delete/<id>',views.delete,name='delete'),
    path('logout/', views.logout_user, name='logout'),
    
]
