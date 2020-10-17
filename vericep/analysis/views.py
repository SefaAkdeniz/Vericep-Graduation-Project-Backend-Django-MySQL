from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def create(request):
    response = dict()
    if request.method == 'POST':
        
        csv_file=request.FILES["data"]
        
        print(csv_file.name)
        
        a=request.POST["user_id"]
        print(a)
        handle_uploaded_file(csv_file)
        
        response["result"] = 1
        response["message"]="İşlem Başarılı."
       


    return JsonResponse(response)


def handle_uploaded_file(f):  
    with open('uploads/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  