from django.shortcuts import render

def home(request):  
    import requests
    import json
    # in here going to grab the data for prices
    price_request= requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,:TC&tsyms=USD')
    price=json.loads(price_request.content)
#https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR
#https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD,EUR
    #in here I am grabbing 
    api_request= requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api=json.loads(api_request.content)
    return render(request, 'home.html',{'api':api,'price':price})

    