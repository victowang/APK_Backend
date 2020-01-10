FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update -y
RUN apt-get install -y aapt
RUN pip install -r requirements.txt
RUN python manage.py makemigrations api
RUN python manage.py migrate
COPY . /code/
