from django.db import models

# Create your models here.

class Skills(models.Model):
    content = models.TextField()
    languages = models.CharField(max_length = 100)
    dbms = models.CharField(max_length = 100)
    softwares = models.CharField(max_length = 100)