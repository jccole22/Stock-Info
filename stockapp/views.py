from django.shortcuts import render

def home(request):
    # pk_9d0b8bcc2b294af6aec535e383f1c077
    import requests
    import json

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_9d0b8bcc2b294af6aec535e383f1c077")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error in call"
    
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})