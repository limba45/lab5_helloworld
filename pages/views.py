from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def my_view(request):
    return JsonResponse({"Name": "Hello World!"})