from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import aaptTools

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def applications(request):
    if request.method == 'GET':
        #info = aaptTools.getInfo("ademo.apk") # test erreur fichier non trouvé
        info = aaptTools.getInfo("demo.apk")
        response = JsonResponse(info.data, safe = False)

        return response

    if request.method == 'POST':
        response = JsonResponse({}, safe = False)
        return response
