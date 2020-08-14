from django.urls import path
from . import views

urlpatterns = [
    path('addCard/', views.addCard, name='addCard')
]
