from django.http import JsonResponse
from . import aaptTools
from django.views.decorators.csrf import csrf_exempt
import os


@csrf_exempt #TODO secure it
def applications(request):
    if request.method == 'GET':
        response = JsonResponse(aaptTools.getAllAppInfos().data, safe = False)
        return response

    if request.method == 'POST':
        #TODO use a form to check input
        handle_uploaded_file(request.FILES['file'], request.POST["appName"])
        return JsonResponse({})


def handle_uploaded_file(file, filename):
    if not os.path.exists('media/'):
        os.mkdir('media/')

    with open('media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)