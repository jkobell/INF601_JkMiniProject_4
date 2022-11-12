from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exchange/', views.exchange, name='exchange'),
    path('currency/', views.currency, name='currency'),
    path('ticker/', views.ticker, name='ticker'),
    path('exchange/<int:exchange_id>/', views.exchange_detail, name='exchange_detail'),
    path('currency/<int:currency_id>/', views.currency_detail, name='currency_detail'),
    path('ticker/<int:ticker_id>/', views.ticker_detail, name='ticker_detail'),
]