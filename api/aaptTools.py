import os
import subprocess
from .serializers import AppSerializer

#TODO protect again directory traversal

def getAppInfo(fileName):
    appFile = "./media/" + fileName
    appInfoStr = subprocess.getoutput("aapt dump badging " + appFile)

    #TODO traiter erreur
    if appInfoStr[:7] == "W/asset":
        print("ERREUR")
        print(appInfoStr)
        return AppSerializer()

    appInfo = {}
    packageStr = appInfoStr.split('\n')[0]
    attrs = packageStr.split(' ')[1:]
    appInfo["application"] = fileName
    appInfo["package_name"] = attrs[0][6:-1]
    appInfo["package_version_code"] = attrs[1][13:-1]
    return AppSerializer(appInfo)

def getAllAppInfos():
    """Gets the metadata from all the apk files in the media directory"""
    infos = []
    appNamesStr = subprocess.getoutput("ls ./media/*.apk")
    appNameList = appNamesStr.split('\n')
    for appName in appNameList:
        infos.append(getAppInfo(appName).data)
    return AppSerializer(infos, many=True)