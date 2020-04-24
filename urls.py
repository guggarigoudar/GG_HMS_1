from django.urls import path
from . import views

urlpatterns=[

path('', views.fnIndex),
path('IPD/',views.fnIpdRegister,name='IPD'),
path('OPD/',views.fnOpdRegister, name='OPD'),
path('index/', views.fnIndex, name='index'),
path('VIEWDATA/', views.fnViewData, name='VIEWDATA'),
path('OPDPROFILE/', views.fnViewOpdProfile),

]