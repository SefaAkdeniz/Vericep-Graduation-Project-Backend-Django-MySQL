from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getModel(request):
    return JsonResponse({'sa':'as'})