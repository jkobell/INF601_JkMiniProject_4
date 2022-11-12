from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Exchange
from .models import Currency
from .models import Ticker

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the CHARTS index - for now :) - right?.")

    #pages_list = ['exchanges', 'tickers', 'charts', 'currency']
    pages_list = ['exchange', 'currency', 'ticker']
    #exchange_list = ["red", "white", "blue"]
    #template = loader.get_template('charts/index.html')
    context = {
        'page_name': 'Site Index',
        'pages_list': pages_list,
    }
    return render(request, 'charts/index.html', context=context)

def exchange(request):
    try:
        exchange_list = Exchange.objects.all()
        context = {
            'exchange_list': exchange_list,
            'page_name': 'Available Exchanges',
            'exchange_detail': 'exchange_detail',
        }
    except Exchange.DoesNotExist:
        raise Http404("Exchange does not exist")
    return render(request, 'charts/exchange.html', context=context)

def exchange_detail(request, exchange_id):
    exchange_content = Exchange.objects.filter(id=exchange_id)
    context = {
        'exchange_content': exchange_content,
        'page_name': 'Exchange Details',
    }
    return render(request, 'charts/exchange_detail.html', context=context)

def currency(request):
    currency_list = Currency.objects.all()
    context = {
        'currency_list': currency_list,
        'page_name': 'Available Currencies',
        'currency_detail': 'currency_detail',
    }
    return render(request, 'charts/currency.html', context=context)

def currency_detail(request, currency_id):
    currency_content = Currency.objects.filter(id=currency_id)
    context = {
        'currency_content': currency_content,
        'page_name': 'Currency Details',
    }
    return render(request, 'charts/currency_detail.html', context=context)

def ticker(request):
    ticker_list = Ticker.objects.all()
    context = {
        'ticker_list': ticker_list,
        'page_name': 'Available Tickers',
        'ticker_detail': 'ticker_detail',
    }
    return render(request, 'charts/ticker.html', context=context)

def ticker_detail(request, ticker_id):
    ticker_content = Ticker.objects.filter(id=ticker_id)
    context = {
        'ticker_content': ticker_content,
        'page_name': 'Ticker Details',
    }
    return render(request, 'charts/ticker_detail.html', context=context)
