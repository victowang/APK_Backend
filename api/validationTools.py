import re

def isValidName(appName):
    """check that appName ends with .apk and does not change path"""
    print(appName)
    isValid = True
    if len(appName) <= 6:
        print("name too short, might be missing .apk extension")
        isValid = False
    if appName[-4:] != ".apk":
        print("Missing .apk extension")
        isValid = False
    p1 = re.compile("(\.*\/*)*")  # checking input with . and / at the beginning
    p2 = re.compile(".*\/") # checking '/' characters in appName
    if p1.match(appName).end() != 0 or p2.match(appName) != None:
        print("Might lead to directory traversal")
        isValid = False
    return isValid

def test():
    tests = ["demo.apk", "new.app.apk", "a", ".apk", "../demo.apk", "newdir/appName.apk"]
    for appName in tests:
        print(appName, isValidName(appName))
        print(" --- --- ---")
    return

if __name__ == "__main__":
    test()