#This file makes it bug
from django.db import models

class App(models.Model):
    application = models.CharField(max_length=200)
    package_name = models.CharField(max_length=200)
    package_version_code = models.CharField(max_length=200)

    #class Meta:
    #    app_label = 'api.app'

    def __str__(self):
        return self.application