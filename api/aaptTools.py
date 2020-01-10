import subprocess
import os
#import re
from .serializers import AppSerializer
from rest_framework import status

#TODO protect again directory traversal

def getAppInfo(appName):

    #TODO check for directoru traversal
    #pattern = "\.*\/*"
    #prog = re.compile(pattern)
    #match = prog.match(appName)
    #print(match)
    #if match.span() != (0,0):
    #    print("suspicious file name, might be a directory traversal attempt")
    #    return {}

    appInfoStr = subprocess.getoutput("aapt dump badging " + "./media/" + appName)

    if appInfoStr[:7] == "W/asset":
        print("ERREUR")
        print(appInfoStr)
        return AppSerializer()

    appInfo = {}
    packageStr = appInfoStr.split('\n')[0]
    attrs = packageStr.split(' ')[1:]
    appInfo["application"] = "/media/" + appName
    appInfo["package_name"] = attrs[0][6:-1]
    appInfo["package_version_code"] = attrs[1][13:-1]
    return AppSerializer(appInfo)

def getAllAppInfos():
    """Gets the metadata from all the apk files in the media directory"""
    infos = []
    appNamesStr = subprocess.getoutput("ls -a ./media/*.apk") #TODO eventuellement modifier pour proteger contre directory traversal
    appNameList = appNamesStr.split('\n')
    for appName in appNameList:
        infos.append(getAppInfo(appName[8:]).data)
    return AppSerializer(infos, many=True)

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
    appInfo = getAppInfo(filename)
    return appInfo.data, msg