from django.db import models

# Create your models here.


class Person(models.Model):
    person_name = models.CharField(max_length=20)
    age = models.IntegerField(default=40)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
