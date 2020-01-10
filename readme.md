#H1 Backend to upload ans list applications

requires aapt installed on the host machine

API endpoints:
* GET http://127.0.0.1:8080/api/applications
* POST http://127.0.0.1:8080/api/applications

API Postman doc:
* [https://documenter.getpostman.com/view/10031182/SWLh6SSX?version=latest]

Challenges:
* Set SECRET_KEY in settings.py as an environment variable
* Use aapt (the aapt Python package did not work for me)
* Send .apk file through http POST request (used curl poorly, switched to Postman)