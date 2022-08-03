from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    # pk_9d0b8bcc2b294af6aec535e383f1c077
    import requests
    import json

    if request.method == 'POST':
        stock_input = request.POST['stock_input']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + stock_input + "/quote?token=pk_9d0b8bcc2b294af6aec535e383f1c077")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error in call"
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'stock_input': "Enter company in search bar for stock information."})
    
    #return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')


    else:
        ticker = Stock.objects.all()
        ticker_list = []

        for ticker_items in ticker:
            ticker_list.append(ticker_items.ticker)
        
        ticker_string = ",".join(ticker_list)

        url = "https://cloud.iexapis.com/v1/stock/market/batch?&types=quote&symbols=" + str(ticker_string) + "&token=pk_9d0b8bcc2b294af6aec535e383f1c077"
        api_request = requests.get(url)
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error in call"
        
        return render(request, 'add_stock.html', {'ticker': ticker, 'api': api})


def delete(request, stock_ticker):
    item = Stock.objects.get(ticker=stock_ticker.lower())
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect(add_stock)