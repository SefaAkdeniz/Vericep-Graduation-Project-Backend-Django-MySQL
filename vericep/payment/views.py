from django.http import JsonResponse
from .models import PastPayments, Balance, CreditCard
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json


# Create your views here.
@csrf_exempt
def addCard(request):
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id = json_data["user_id"]
            card_name = json_data["card_name"]
            card_number = json_data["card_number"]
            expiration_date_month = json_data["expiration_date_month"]
            expiration_date_year = json_data["expiration_date_year"]
            cvc = json_data["cvc"]
            user_ = User.objects.filter(id=user_id).first()
            card = CreditCard(user=user_, card_name=card_name, card_number=card_number,
                              expiration_date_month=expiration_date_month, expiration_date_year=expiration_date_year, cvc=cvc)
            card.save()
            response["result"] = 1
            response["message"] = "İşlem Başarıyla Gerçekleştirildi."
            return JsonResponse(response)

        except:
            response["result"] = 0

            return JsonResponse(response)


def listCard(request):
    response = dict()
    card_list=[]
    count=0
    if request.method == 'POST':
        json_data = json.loads(request.body)
        user_id=json_data["user_id"]
        user_ = User.objects.filter(id=user_id).first()
        cards=CreditCard.objects.filter(user=user_)
        for each in cards:
            count=count+1
            card={"id":each.pk,"card_name":each.card_name,"card_number":each.card_number,"expiration_date_month":each.expiration_date_month,"expiration_date_year":each.expiration_date_year,"cvc":each.cvc}
            card_list.append(card)
    response["cardCount"]=count
    response["cards"]=card_list
    return JsonResponse(response)


def getBalance(request):
    response = dict()
    return JsonResponse(response)


def setBalance(request):
    response = dict()
    return JsonResponse(response)


def listPastPayments(request):
    response = dict()
    return JsonResponse(response)
