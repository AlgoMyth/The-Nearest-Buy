from email.policy import default
from django.db import models
class Shop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    # city = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=100,default="")
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name