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
            name = json_data["name"]
            card_number = json_data["card_number"]
            expiration_date_month = json_data["expiration_date_month"]
            expiration_date_year = json_data["expiration_date_year"]
            cvc = json_data["cvc"]
            try:
                int(card_number)
                if len(card_number) != 16:
                    response["result"] = 0
                    response["message"] = "Kart Numarısı 16 haneli olmalıdır."
                    return JsonResponse(response)

            except:
                response["result"] = 0
                response["message"] = "Kart Numarısı sayısal değer olmalıdır."
                return JsonResponse(response)
            try:
                int(cvc)
                if len(cvc) != 3:
                    response["result"] = 0
                    response["message"] = "Kart Numarısı 3 haneli olmalıdır."
                    return JsonResponse(response)
            except:
                response["result"] = 0
                response["message"] = "CVV sayısal değer olmalıdır."
                return JsonResponse(response)

            if len(name.split(" ")) < 2:
                response["result"] = 0
                response["message"] = "Ad soyad en az 2 kelimeden oluşmalıdır."
                return JsonResponse(response)

            user_ = User.objects.filter(id=user_id).first()
            card = CreditCard(user=user_, card_name=name, card_number=card_number,
                              expiration_date_month=expiration_date_month, expiration_date_year=expiration_date_year, cvc=cvc)
            card.save()
            response["result"] = 1
            response["message"] = "İşlem Başarılı."
        except Exception as e:
            response["result"] = 0
            response["message"] = str(e)
    return JsonResponse(response)


@csrf_exempt
def deleteCard(request):
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            card_id = json_data["card_id"]
            print(card_id)
            if CreditCard.objects.filter(id=card_id).exists():
                pass
            else:
                response["result"] = 0
                response["message"] = "Kart bulunamadı."
                return JsonResponse(response)
            card = CreditCard.objects.filter(id=card_id).delete()
            response["result"] = 1
            response["message"] = "İşlem Başarılı."
        except Exception as e:
            response["result"] = 0
            response["message"] = str(e)
    return JsonResponse(response)


@csrf_exempt
def listCard(request):
    response = dict()
    card_list = []
    cardCount = 0
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id = json_data["user_id"]
            user_ = User.objects.filter(id=user_id).first()
            cards = CreditCard.objects.filter(user=user_)
            for each in cards:
                cardCount += 1
                card = {"id": each.pk, "name": each.card_name, "card_number": each.card_number,
                        "expiration_date_month": each.expiration_date_month, "expiration_date_year": each.expiration_date_year, "cvc": each.cvc}
                card_list.append(card)
            response["result"] = 1
            response["message"] = "İşlem Başarılı."
            response["cardCount"] = cardCount
            response["cards"] = card_list
        except Exception as e:
            response["result"] = 0
            response["message"] = str(e)
    return JsonResponse(response)


@csrf_exempt
def getBalance(request):
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id = json_data["user_id"]
            user_ = User.objects.filter(id=user_id).first()
            balance = Balance.objects.filter(user=user_).first()
            response["result"] = 1
            response["message"] = "İşlem Başarılı."
            response["amaount"] = balance.amaount
        except Exception as e:
            response["result"] = 0
            response["message"] = str(e)
    return JsonResponse(response)


@csrf_exempt
def doPayment(request):
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id = json_data["user_id"]
            add_amaount = json_data["add_amaount"]
            card_id = json_data["card_id"]
            verification_cvc = json_data["verification_cvc"]
            add_amaount = Decimal(add_amaount.replace(",", "."))

            card = CreditCard.objects.filter(id=card_id).first()
            if int(verification_cvc) != int(card.cvc):
                response["result"] = 0
                response["message"] = "CVC Numarası Doğrulanamadı."
                return JsonResponse(response)

            if add_amaount >= 1000:
                response["result"] = 0
                response["message"] = "1000 TL'den az ödeme yapabilirsiniz."
                return JsonResponse(response)

            user_ = User.objects.filter(id=user_id).first()
            balance = Balance.objects.filter(user=user_).first()
            balance.amaount += Decimal(add_amaount)
            payment = PastPayments(amaount=add_amaount, card=card)
            payment.save()
            balance.save()
            response["result"] = 1
            response["message"] = "İşlem Başarılı."
        except Exception as e:
            response["result"] = 0
            response["message"] = str(e)
    return JsonResponse(response)


@csrf_exempt
def listPastPayments(request):
    payment_list = []
    paymentCount = 0
    total_payment_price = 0
    response = dict()
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user_id = json_data["user_id"]
            user_ = User.objects.filter(id=user_id).first()
            cards = CreditCard.objects.filter(user=user_)

            for card in cards:
                payments = PastPayments.objects.filter(card=card)
                cardInfo = {"id": card.pk, "name": card.card_name, "card_number": card.card_number,
                            "expiration_date_month": card.expiration_date_month, "expiration_date_year": card.expiration_date_year, "cvc": card.cvc}
                for each in payments:

                    payment = {"id": each.pk, "date": each.date,
                               "amount": each.amaount, "payment_card": cardInfo}
                    payment_list.append(payment)
                    paymentCount += 1
                    total_payment_price += each.amaount

            payment_list = sorted(
                payment_list, key=lambda payment: payment["date"])
            response["result"] = 1
            response["message"] = "İşlem Başarılı."
            response["paymentCount"] = paymentCount
            response["totalPaymentPrice"] = total_payment_price
            response["payments"] = payment_list
        except Exception as e:
            response["result"] = 0
            response["message"] = str(e)
    return JsonResponse(response)
