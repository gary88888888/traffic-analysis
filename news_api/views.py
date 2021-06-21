from django.shortcuts import render
import requests
from requests.models import Response
API_KEY = '6499830617274f538a929714de262794'

# Create your views here.

def news(request):
    url = f'https://newsapi.org/v2/top-headlines?country=tw&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    articles = data['articles']


    context = {
        'articles' : articles
    }

    return render(request, 'news_api/news.html', context)

    # articles = data['articles']

    # context = {
    #     'articles' : articles
    # }


    # title = articles['title']

    # context = {
    #     'title' : title
    # }

    # return render(request, 'news_api/news.html', context)