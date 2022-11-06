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

class Chart(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    bg_color = models.CharField(max_length=25)
    curve_color = models.CharField(max_length=25)


    


