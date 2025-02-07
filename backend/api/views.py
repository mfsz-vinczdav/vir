from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"message": "Hello, Floorball API!"})

def home(request):
    return JsonResponse({"message": "Welcome to the Floorball API!"})
