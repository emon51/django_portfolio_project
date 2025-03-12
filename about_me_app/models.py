from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length = 50, default = 'About me')
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    age = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 15)
    varsity = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    cgpa = models.CharField(max_length = 5)
    content = models.TextField()

    def __str__(self):
        return self.name

