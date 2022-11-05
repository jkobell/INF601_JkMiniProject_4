from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Ticker(models.Model):
    is_active = models.BooleanField()
    symbol = models.CharField(max_length=5)#NYSE 1-5 chars long
    name = models.CharField(max_length=150)
    exchange = models.CharField(max_length=25)
    currency_code = models.CharField(max_length=3)#ISO 4217
    currency_country = models.CharField(max_length=25)
    currency_name = models.CharField(max_length=50)
    currency_number = models.PositiveSmallIntegerField()
    industry = models.CharField(max_length=25)
    sector = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    


