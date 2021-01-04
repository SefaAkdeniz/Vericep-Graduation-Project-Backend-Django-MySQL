from django.http import JsonResponse
from .models import MlModel, ModelInput

# Create your views here.


def listModel(request):
    response = dict()
    model_list = []
    input_list = []
    modelCount = 0

    try:
        models = MlModel.objects.all()
        for each in models:
            if each.isPublished == True:
                inputCount = 0
                input_list = list()
                modelCount += 1
                inputs = ModelInput.objects.filter(model_id=each.pk)
                for each2 in inputs:
                    inputCount += 1
                    input_ = {"id": each2.pk, "name": each2.input_name,
                              "type": each2.typed, "description": each2.description}
                    input_list.append(input_)
                model = {"id": each.pk, "name": each.model_name, "url": each.heroku_url,
                         "description": each.model_description, "inputCount": inputCount, "inputs": input_list}
                model_list.append(model)
        response["result"] = 1
        response["message"] = "İşlem Başarıyla Gerçekleştirildi."
        response["modelCount"] = modelCount
        response["models"] = model_list
        return JsonResponse(response)
    except Exception as e:
        response["result"] = 0
        response["message"] = str(e)
        return JsonResponse(response)
