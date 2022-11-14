# INF601 - Advanced Programming in Python
# James Kobell
# Mini Project 4
from django.db import models

class Timezone(models.Model): #foreign key in Exchange
    timezone = models.CharField(max_length=25)
    abbr = models.CharField(max_length=10)
    abbr_dst = models.CharField(max_length=10)

    def __str__(self): # replaces Object(1) in displayed name 
        return 'Timezone: ' + self.timezone

class Currency(models.Model): #foreign key in Exchange
    code = models.CharField(max_length=15)#
    symbol = models.CharField(max_length=25)
    name = models.CharField(max_length=50)

    def __str__(self):# replaces Object(1) in displayed name
        return 'Currency: ' + self.name

class Exchange(models.Model): #foreign key for Ticker
    timezone = models.ForeignKey(Timezone, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)#
    acronym = models.CharField(max_length=25)
    market_id = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    country_code = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self):# replaces Object(1) in displayed name
        return 'Exchange: ' + self.name

class Ticker(models.Model): #foreign key for Chart
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)    
    is_active = models.BooleanField()
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=10)
    has_intraday = models.BooleanField() 
    has_eod = models.BooleanField()

    def __str__(self):# replaces Object(1) in displayed name
        return 'Ticker: ' + self.name
    
class Chart(models.Model): #active trading and historical data 
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    bg_color = models.CharField(max_length=25)
    curve_color = models.CharField(max_length=25)

    def __str__(self):# replaces Object(1) in displayed name
        return 'Chart: ' + self.name

class Intraday(models.Model): #for active trading charts
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)#
    acronym = models.CharField(max_length=25)
    market_id = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    country_code = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    datetime = models.DateTimeField()
    
    def __str__(self):# replaces Object(1) in displayed name
        return 'Intraday: ' + self.name


    


