from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
import json

# Create your views here.


@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username=json_data["username"]
        password=json_data["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("okey")
        else:
            print("kullanıcı yok")

    d = {
        "result": "login"
    }
    return JsonResponse(d)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username=json_data["username"]
        email=json_data["email"]
        password=json_data["password"]
        first_name=json_data["first_name"]
        last_name=json_data["last_name"]

        if User.objects.filter(username=username).exists():
            print("Kullanıcı adı alınmış.")
        elif User.objects.filter(email=email).exists():
            print("Mail Alınmış")
        else:
            user=User.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name)
            user.save()
            print("okey")

    d = {
        "result": "register"
    }
    return JsonResponse(d)
