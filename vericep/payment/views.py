from django.http import JsonResponse
from .models import PastPayments, Balance, CreditCard
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from decimal import Decimal


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
            response["message"]="İşlem Başarılı."
        except:
            response["result"] = 0
            response["message"]="İşlem Başarısız."
    return JsonResponse(response)

@csrf_exempt
def listCard(request):
    response = dict()
    card_list=[]
    count=0
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id=json_data["user_id"]
            user_ = User.objects.filter(id=user_id).first()
            cards=CreditCard.objects.filter(user=user_)
            for each in cards:
                count=count+1
                card={"id":each.pk,"card_name":each.card_name,"card_number":each.card_number,"expiration_date_month":each.expiration_date_month,"expiration_date_year":each.expiration_date_year,"cvc":each.cvc}
                card_list.append(card)
            response["result"] = 1
            response["message"]="İşlem Başarılı."
            response["cardCount"]=count
            response["cards"]=card_list   
        except:
            response["result"] = 0
            response["message"]="İşlem Başarısız."
    return JsonResponse(response)

@csrf_exempt
def getBalance(request):
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id=json_data["user_id"]
            user_ = User.objects.filter(id=user_id).first()
            balance=Balance.objects.filter(user=user_).first()
            response["result"]=1
            response["message"]="İşlem Başarılı."
            response["amaount"]=balance.amaount
        except:
            response["result"]=0
            response["message"]="İşlem Başarısız."
    return JsonResponse(response)

@csrf_exempt
def setBalance(request):
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id=json_data["user_id"]
            process_price=json_data["process_price"]
            user_ = User.objects.filter(id=user_id).first()
            balance=Balance.objects.filter(user=user_).first()
            balance.amaount+=Decimal(process_price)
            if balance.amaount<0:
                response["result"]=0
                response["message"]="Bakiye Yetersiz."
                return JsonResponse(response)
            balance.save()
            response["result"]=1
            response["message"]="İşlem Başarılı."
        except:
            response["result"]=0
            response["message"]="İşlem Başarısız."
    return JsonResponse(response)

@csrf_exempt
def addPayments(request):
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id=json_data["user_id"]
            add_amaount=json_data["add_amaount"]
            card_id=json_data["card_id"]
            verification_cvc=json_data["verification_cvc"]
            user_ = User.objects.filter(id=user_id).first()
            balance=Balance.objects.filter(user=user_).first()
            balance.amaount+=Decimal(add_amaount)
            balance.save()
            card=CreditCard.objects.filter(id=card_id).first()
            if int(verification_cvc)!=int(card.cvc):
                response["result"]=0
                response["message"]="CVC Numarası Doğrulanamadı."
                return JsonResponse(response)

            payment = PastPayments(amaount=add_amaount,card=card)
            payment.save()
            response["result"]=1
            response["message"]="İşlem Başarılı."
        except:
            response["result"]=0
            response["message"]="İşlem Başarısız."
    return JsonResponse(response)


@csrf_exempt
def listPastPayments(request):
    payment_list=[]
    count=0
    total_payment_price=0
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id=json_data["user_id"]
            user_ = User.objects.filter(id=user_id).first()
            cards=CreditCard.objects.filter(user=user_)

            for card in cards:
                payments=PastPayments.objects.filter(card=card)
                cardInfo={"id":card.pk,"card_name":card.card_name,"card_number":card.card_number,"expiration_date_month":card.expiration_date_month,"expiration_date_year":card.expiration_date_year,"cvc":card.cvc}
                for each in payments:

                    payment={"id":each.pk,"date":each.date,"amount":each.amaount,"payment_card":cardInfo}
                    payment_list.append(payment)
                    count+=1
                    total_payment_price+=each.amaount
            response["result"]=1
            response["message"]="İşlem Başarılı."
            response["paymentCount"]=count
            response["totalPaymentPrice"]=total_payment_price
            response["payments"]=payment_list
        except:
            response["result"]=0
            response["message"]="İşlem Başarısız."
    return JsonResponse(response)
