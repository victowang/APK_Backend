Backend to upload ans list applications

requires aapt

API:

GET http://127.0.0.1:8080/api/applications
curl http://127.0.0.1:8080/api/applications

POST http://127.0.0.1:8080/api/applications
curl -d "@demo.apk" -X POST http://127.0.0.1:8080/api/applications