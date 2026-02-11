from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Student.objects.create(
            roll=data["roll"],
            name=data["name"],
            mail=data["mail"],
            pswd=data["pswd"],
            mobile=""
        )

        return JsonResponse({"success":True})


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        exists = Student.objects.filter(
            roll=data["roll"],
            pswd=data["pswd"]
        ).exists()

        return JsonResponse({"success":exists})
