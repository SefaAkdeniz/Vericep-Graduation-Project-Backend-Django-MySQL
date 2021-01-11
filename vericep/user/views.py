from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
import json
from payment.models import Balance
import re

# Create your views here.


@csrf_exempt
def login(request):
    response = dict()
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data["username"]
        password = json_data["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            userInfo = User.objects.filter(username=username).first()
            userInfo = {"id": userInfo.pk, "first_name": userInfo.first_name, "last_name": userInfo.last_name,
                        "email": userInfo.email, "last_login": userInfo.last_login, "date_joined": userInfo.date_joined}
            response["result"] = 1
            response["userInfo"] = userInfo
        else:
            response["result"] = 0
            response["message"] = "Sisteme kayıtlı kullanıcı bulunamadı."

    return JsonResponse(response)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data["username"]
        email = json_data["email"]
        password = json_data["password"]
        first_name = json_data["first_name"].capitalize()
        last_name = json_data["last_name"].capitalize()

        response = validatorForm(
            first_name, last_name, username, password, email)

        if not bool(response):
            user = User.objects.create_user(
                username=username, password=password, email=email, last_name=last_name, first_name=first_name)
            user.save()
            balance = Balance(user=user, amaount=0)
            balance.save()
            response["result"] = 1
            response["message"] = "Hesap başarıyla oluşturulmuştur."

    return JsonResponse(response)


def validatorForm(first_name, last_name, username, password, email, oldUsername="", oldEmail=""):
    response = dict()
    if User.objects.filter(username=username).exists():
        if oldUsername != username:
            response["result"] = 0
            response["message"] = "Kullanıcı adı daha önceden kullanılmıştır."
    if User.objects.filter(email=email).exists():
        if oldEmail != email:
            response["result"] = 0
            response["message"] = "E-posta adresi daha önceden kullanılmıştır."
    if len(first_name) < 2:
        response["result"] = 0
        response["message"] = "İsim 2 karakterden kısa olamaz."
    if len(last_name) < 2:
        response["result"] = 0
        response["message"] = "Soyisim 2 karakterden kısa olamaz."
    if len(password) < 8:
        response["result"] = 0
        response["message"] = "Şifre 8 karakterden kısa olamaz."
    if len(username) < 3:
        response["result"] = 0
        response["message"] = "Kullanıcı adı 3 karakterden kısa olamaz."
    if checkMailFormat(email):
        response["result"] = 0
        response["message"] = "E-Posta adresi uygun formatta değil."
    return response


@csrf_exempt
def updateAccount(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data["username"]
        user_id = json_data["user_id"]
        email = json_data["email"]
        password = json_data["password"]
        first_name = json_data["first_name"].capitalize()
        last_name = json_data["last_name"].capitalize()

        user_ = User.objects.filter(id=user_id).first()

        response = validatorForm(
            first_name, last_name, username, password, email, user_.username, user_.email)

        if not bool(response):
            user = User(id=user_id, username=username,
                        last_name=last_name, first_name=first_name, email=email)
            user.set_password(password)
            user.save()
            response["result"] = 1
            response["message"] = "Hesap başarıyla güncellendi."

    return JsonResponse(response)


@csrf_exempt
def getAccountInfo(request):
    response = dict()
    if request.method == 'POST':
        json_data = json.loads(request.body)
        user_id = json_data["user_id"]

        user = User.objects.filter(id=user_id).first()

        if user is not None:
            userInfo = {"id": user.pk, "first_name": user.first_name, "last_name": user.last_name,
                        "email": user.email, "last_login": user.last_login, "date_joined": user.date_joined, "username": user.username}
            response["result"] = 1
            response["userInfo"] = userInfo
        else:
            response["result"] = 0
            response["message"] = "Sisteme kayıtlı kullanıcı bulunamadı."

    return JsonResponse(response)


def checkMailFormat(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return False
    else:
        return True
