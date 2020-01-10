from django.http import JsonResponse
from . import aaptTools
from django.views.decorators.csrf import csrf_exempt
import os
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt #TODO secure it
def applications(request):
    if request.method == 'GET':
        response = JsonResponse(aaptTools.getAllAppInfos().data, safe = False)
        return response

    if request.method == 'POST':
        #TODO use a form to check input
        body, msg = handle_uploaded_file(request.FILES['file'], request.POST["appName"])
        return JsonResponse({}, status=msg)

def handle_uploaded_file(file, filename):
    if not os.path.exists('media/'):
        os.mkdir('media/')
    if os.path.isfile('media/'+filename):
        msg = status.HTTP_200_OK
    else:
        msg = status.HTTP_201_CREATED

    with open('media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return {}, msg