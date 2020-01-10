from .models import App
from .serializers import AppSerializer

def getAppInfos(appName):
    app = App.objects.get(application=appName)
    return AppSerializer(app).data

def getAllAppInfos():
    all_apps = App.objects.values().all()
    return AppSerializer(all_apps, many=True).data