from django.http import JsonResponse
from .models import MlModel,ModelInput

# Create your views here.


def listModel(request):
    
    response=dict()
    model_list=[]
    input_list=[]
    count=0
    

    models=MlModel.objects.all()

    for each in models:
        if each.isPublished== True:
            count2=0
            input_list=list()
            count=count+1
            inputs=ModelInput.objects.filter(model_id=each.pk) 
            for each2 in inputs:
                count2=count2+1
                input_={"id":each2.pk,"name":each2.input_name,"type":each2.typed,"description":each2.description}
                input_list.append(input_)
            model={"id":each.pk,"name":each.model_name,"url":each.heroku_url,"description":each.model_description,"inputCount":count2,"inputs":input_list}
            model_list.append(model)
    response["modelCount"]=count
    response["models"]=model_list
    return JsonResponse(response)
