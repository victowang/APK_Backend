# Backend to upload ans list applications

## API endpoints:
* GET http://127.0.0.1:8080/api/applications
* POST http://127.0.0.1:8080/api/applications

## API Postman doc:
* [https://documenter.getpostman.com/view/10031182/SWLh6mvR?version=latest]

## To do:
* Secure uploaded input with a form
* Manage csrf token
* Store media directory path as a variable in settings.py

## Challenges faced:
* Set SECRET_KEY in settings.py as an environment variable
* Use aapt (the aapt Python package did not work for me)
* Send .apk file through http POST request (used curl poorly, switched to Postman)


## Requires:
docker-compose

## Run in project root:
sudo docker-compose up

