from django.shortcuts import render
from .models import Account
from django.http import JsonResponse


def users_list(request):
    MAX_OBJECTS = 20
    users = Account.objects.all()
    data = {"results":list(user.values("first_name", "last_name", "bio", "location", "birth_date"))}
    return JsonResponse(data)
# Create your views here.
