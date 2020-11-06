from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Analysis
from django.contrib.auth.models import User
import json
import os
from . import sendMail


# Create your views here.

@csrf_exempt
def create(request):
    response = dict()
    if request.method == 'POST':
        
        csv_file=request.FILES["data"]

        file_format = "."+csv_file.name.split('.')[1]
        print(file_format)
      
        user_id=request.POST["user_id"]

        user_ = User.objects.filter(id=user_id).first()
        analysis = Analysis(user=user_)
        analysis.save()
        print(analysis.pk)

        handle_uploaded_file(csv_file,analysis.pk,file_format)
        create_analysis(str(analysis.pk)+str(file_format))
        
        sendMail.send_test_mail(user_.email,str(analysis.pk))

        response["result"] = 1
        response["message"]="İşlem Başarılı."

    return JsonResponse(response)


def handle_uploaded_file(f,id,file_format):  
    with open('uploads/'+str(id)+file_format, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  



def create_analysis(file_name):
    import pandas as pd
    import pandas_profiling as pp

    df = pd.read_csv("uploads/"+file_name)
    report = pp.ProfileReport(df)
    os.chdir('outputs/')
    report.to_file(file_name.split(".")[0]+".html")
    os.chdir('../')
  