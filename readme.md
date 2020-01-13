# Backend to list and upload Android applications

## API endpoints:
* GET /api/applications
* POST /api/applications

## API documentation generated with Postman:
* https://documenter.getpostman.com/view/10031182/SWLh6SSX

## Before running:
##### Set SECREY_KEY as an environment variable :  
_Create a file named .env in project/ containing :  
SECRET_KEY='#####'  
where '#####' is a 50 character string_
##### Example :
echo "SECRET_KEY='examplesecretkey0a%qp8^^d*d+qt0b3%+h177l0_7y3=+#el'" > project/.env

## Run directy:
##### If needed, install required packages:   
pip install -r requirements.txt  

##### If needed install aapt:  
apt-get install aapt  

##### When running for the first time :  
* python manage.py makemigrations
* python manage.py migrate  
##### Launch :  
python manage.py runserver

## Run with docker compose:
##### When running for the first time :  
* sudo docker-compose run web python manage.py makemigrations
* sudo docker-compose run web python manage.py migrate  
##### Launch :  
sudo docker-compose up

## Future improvements:
* Manage csrf token
* Store media directory path as a variable in settings.py
* Give feedback if request has failed

## Challenges faced:
* Set SECRET_KEY in settings.py as an environment variable
* Use aapt (the aapt Python package did not work for me)
* Send .apk file through http POST request (used curl poorly, switched to Postman)

