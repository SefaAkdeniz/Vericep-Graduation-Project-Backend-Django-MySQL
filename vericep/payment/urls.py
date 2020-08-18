from django.urls import path
from . import views

urlpatterns = [
    path('addCard/', views.addCard, name='addCard'),
    path('listCard/', views.listCard, name='listCard'),
    path('getBalance/', views.getBalance, name='getBalance'),
    path('setBalance/', views.setBalance, name='setBalance'),
    path('listPastPayments/', views.listPastPayments, name='listPastPayments')
]

