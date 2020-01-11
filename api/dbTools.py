from .models import App

def getAppInfo(appName):
    app = App.objects.get(application=appName)
    return app

def getAllAppInfo():
    all_apps = App.objects.values().all()
    return all_apps

def uploadAppInfo(data):
    app = App(application = data['application'], package_name = data['package_name'], package_version_code = data['package_version_code'])
    app.save()
    return

def updateAppInfo(data):
    app = App.objects.get(application=data['application'])
    app.package_name = data['package_name']
    app.package_version_code = data['package_version_code']
    app.save()
    return

def deleteAppInfo(appName):
    return App.objects.filter(application=appName).delete()

