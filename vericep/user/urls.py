from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('updateAccount/', views.updateAccount, name='updateAccount'),
    path('getAccountInfo/', views.getAccountInfo, name='getAccountInfo'),
]
