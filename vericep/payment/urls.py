from django.urls import path
from . import views

urlpatterns = [
    path('addCard/', views.addCard, name='addCard'),
    path('deleteCard/', views.deleteCard, name='deleteCard'),
    path('listCard/', views.listCard, name='listCard'),
    path('getBalance/', views.getBalance, name='getBalance'),
    path('setBalance/', views.setBalance, name='setBalance'),
    path('doPayment/', views.doPayment, name='doPayment'),
    path('listPastPayments/', views.listPastPayments, name='listPastPayments')
]
