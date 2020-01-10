# Backend to list and upload Android applications

## API endpoints:
* GET /api/applications
* POST /api/applications

## API documentation generated with Postman:
* https://documenter.getpostman.com/view/10031182/SWLh6SSX

## Before running:
_Set SECRET_KEY environment variable by creating a file named .env in project/ containing SECRET_KEY='#####'_  
_Where '#####' is a 50 character string_

echo "SECRET_KEY='examplesecretkey0a%qp8^^d*d+qt0b3%+h177l0_7y3=+#el'" > project/.env

## Run directy:
_Check requirements.txt for needed Python packages, run:_  
pip install -r requirements.txt  

_Check if aapt is installed, if not run:_  
apt-get install aapt  

python manage.py runserver

_Call api endpoints at http://127.0.0.1/8080/api/applications_

## Run with docker compose:
sudo docker-compose up

_Call api endpoints at http://0.0.0.0/8000/api/applications_


## Future improvements:
* Secure uploaded input with a form
* Manage csrf token
* Store media directory path as a variable in settings.py
* Give feedback if POST request has failed (check if the file already exists?)

## Challenges faced:
* Set SECRET_KEY in settings.py as an environment variable
* Use aapt (the aapt Python package did not work for me)
* Send .apk file through http POST request (used curl poorly, switched to Postman)

