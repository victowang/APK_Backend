from . import aaptTools
from . import dbTools
from . import validationTools
from .serializers import AppSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
@csrf_exempt #TODO secure it
def applications(request):
    if request.method == 'GET':
        infos = AppSerializer(dbTools.getAllAppInfo(), many=True).data
        return  Response(infos)#from database
        #return Response(aaptTools.getAllAppInfo().data) #from file system

    if request.method == 'POST':
        #check input name
        appName = request.POST['appName']
        if not validationTools.isValidName(appName):
            return Response({}, status.HTTP_304_NOT_MODIFIED)

        data, status_code = aaptTools.handle_uploaded_file(request.FILES['file'], appName) # saves the app in the file system
        if status_code == "HTTP_201_CREATED":
            dbTools.uploadAppInfo(data) # saves the app metadata in the database
            return Response(data, status=status.HTTP_201_CREATED)
        elif status_code == "HTTP_200_OK":
            dbTools.updateAppInfo(data)
            return Response(data, status=status.HTTP_200_OK)
        else :
            return Response(data, status.HTTP_304_NOT_MODIFIED)

