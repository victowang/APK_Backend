import os
from rest_framework import status
from . import aaptTools
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
@csrf_exempt #TODO secure it
def applications(request):
    if request.method == 'GET':
        #response = JsonResponse(aaptTools.getAllAppInfos().data, safe = False)
        return Response(aaptTools.getAllAppInfos().data)
        #return response

    if request.method == 'POST':
        #TODO use a form to check input
        data, msg = aaptTools.handle_uploaded_file(request.FILES['file'], request.POST["appName"])
        return Response(data, status=msg)

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
    appInfo = aaptTools.getAppInfo(filename)
    return appInfo.data, msg

