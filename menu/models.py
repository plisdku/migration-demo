from django.db import models

# Create your models here.


class MenuCategory(models.Model):
    name = models.CharField(max_length=20)


class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        MenuCategory, on_delete=models.PROTECT, default=None
    )
