from email.policy import default
from django.db import models
class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=100,default="")
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name