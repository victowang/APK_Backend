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

