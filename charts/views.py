from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache
from .models import Exchange
from .models import Currency
from .models import Ticker

@never_cache
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Registration successful. Please log in.')    
            return redirect('login_request')
        #else: 
           # messages.error(request, f'is form valid: {form.is_valid()}') #uncomment to see if form is valid 
    else:
        if request.user.is_authenticated:
            logout(request)
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'charts/register.html', context)

@never_cache
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'charts/login.html', context)

@never_cache
def logout_request(request):    
    logout(request)
    #messages.info(request, f"You are now logged out.")
    return redirect('index')
            
#index list view
def index(request):
    pages_list = ['exchange', 'currency', 'ticker']
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
        #raise Http404 #uncomment to test try/except
    except Exchange.DoesNotExist:
        raise Http404() #if settings DEBUG=False, browser displays: Not Found The requested resource was not found on this server. [preferred]
    return render(request, 'charts/exchange.html', context=context)

def exchange_detail(request, exchange_id):
    try:
        exchange_content = Exchange.objects.filter(id=exchange_id)
        context = {
            'exchange_content': exchange_content,
            'page_name': 'Exchange Details',
        }
    except Exchange.DoesNotExist:
        raise Http404()
    return render(request, 'charts/exchange_detail.html', context=context)

def currency(request):
    try:
        currency_list = Currency.objects.all()
        context = {
            'currency_list': currency_list,
            'page_name': 'Available Currencies',
            'currency_detail': 'currency_detail',
        }
    except Exchange.DoesNotExist:
        raise Http404()
    return render(request, 'charts/currency.html', context=context)

def currency_detail(request, currency_id):
    try:
        currency_content = Currency.objects.filter(id=currency_id)
        context = {
            'currency_content': currency_content,
            'page_name': 'Currency Details',
        }
    except Exchange.DoesNotExist:
        raise Http404()
    return render(request, 'charts/currency_detail.html', context=context)

def ticker(request):
    try:
        ticker_list = Ticker.objects.all()
        context = {
            'ticker_list': ticker_list,
            'page_name': 'Available Tickers',
            'ticker_detail': 'ticker_detail',
        }
    except Exchange.DoesNotExist:
        raise Http404()
    return render(request, 'charts/ticker.html', context=context)

def ticker_detail(request, ticker_id):
    try:
        ticker_content = Ticker.objects.filter(id=ticker_id)
        context = {
            'ticker_content': ticker_content,
            'page_name': 'Ticker Details',
        }
    except Exchange.DoesNotExist:
        raise Http404()
    return render(request, 'charts/ticker_detail.html', context=context)
