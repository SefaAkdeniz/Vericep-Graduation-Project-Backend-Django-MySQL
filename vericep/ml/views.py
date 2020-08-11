from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def listModel(request):
    
    d = {
    "sefa":"5",
    "result":1
    }
   
    return JsonResponse(d)