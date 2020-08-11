from django.http import JsonResponse

# Create your views here.


def login(request):
    d = {
        "result": "login"
    }
    return JsonResponse(d)


def register(request):
    d = {
        "result": "register"
    }
    return JsonResponse(d)
