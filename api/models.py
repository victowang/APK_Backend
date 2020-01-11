#This file makes it bug
from django.db import models

class App(models.Model):
    id = models.AutoField(primary_key=True)
    application = models.CharField(max_length=200)
    package_name = models.CharField(max_length=200)
    package_version_code = models.CharField(max_length=200)

    class Meta:
        db_table = u'api_app'

    def __str__(self):
        return self.application