from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def create(request):
    response = dict()
    if request.method == 'POST':
        a=request.FILES["data"]
        print(a)
       
        try:
            json_data = json.loads(request.body)
            user_id = json_data["user_id"]
            data = json_data["data"]
            response["result"] = 1
            response["message"]="İşlem Başarılı."
            print(type(data))
        except:
            response["result"] = 0
            response["message"]="İşlem Başarısız."
    


    return JsonResponse(response)