from django.urls import path
from . import views

urlpatterns=[
    path('',views.getModel,name ='getModel')
]