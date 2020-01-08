import os
import subprocess
from .serializers import AppSerializer

def getInfo(fileName):
    apk_file = "./data/" + fileName
    apk_info_str = subprocess.getoutput("aapt dump badging " + apk_file)

    #TODO traiter erreur
    if apk_info_str[:7] == "W/asset":
        print("ERREUR")
        print(apk_info_str)
        return AppSerializer()

    apk_info = {}
    line = apk_info_str.split('\n')[0]
    attrs = line.split(' ')[1:]
    apk_info["application"] = fileName
    apk_info["package_name"] = attrs[0][6:-1]
    apk_info["package_version_code"] = attrs[1][13:-1]
    return AppSerializer(apk_info)