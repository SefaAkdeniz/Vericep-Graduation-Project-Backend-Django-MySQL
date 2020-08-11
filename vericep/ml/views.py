from django.http import JsonResponse
from .models import MlModel

# Create your views here.


def listModel(request):
    #models = MlModel.objects.all()

    d = {

        "result": "litmodel"
    }

    return JsonResponse(d)
