import subprocess
import os

def getAppInfo(appName):
    """Gets the metadata from the apk file with matching name in the media directory
        parses the output from the aapt command to extract the app metadata
    """
    appInfoStr = subprocess.getoutput("aapt dump badging " + "./media/" + appName)

    if appInfoStr[:7] == "W/asset":
        print("ERREUR")
        print(appInfoStr)
        return {}

    appInfo = {}
    packageStr = appInfoStr.split('\n')[0]
    attrs = packageStr.split(' ')[1:]
    appInfo["application"] = "/media/" + appName
    appInfo["package_name"] = attrs[0][6:-1]
    appInfo["package_version_code"] = attrs[1][13:-1]
    return appInfo

def getAllAppInfo():
    """Gets the metadata from all the apk files in the media directory"""
    infos = []
    appNamesStr = subprocess.getoutput("ls -a ./media/*.apk") #TODO eventuellement modifier pour proteger contre directory traversal
    appNameList = appNamesStr.split('\n')
    for appName in appNameList:
        infos.append(getAppInfo(appName[8:]).data)
    return infos

def handle_uploaded_file(file, filename):
    """Saves the uploaded file in the media directory, returns http status ok if there was an existing file with the same name, http status created otherwise"""
    if not os.path.exists('media/'):
        os.mkdir('media/')
    if os.path.isfile('media/'+filename):
        status_code = "HTTP_200_OK" # OK
    else:
        status_code = "HTTP_201_CREATED" # CREATED

    with open('media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    appInfo = getAppInfo(filename)
    return appInfo, status_code