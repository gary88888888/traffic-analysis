from django.shortcuts import render
import requests
from requests.models import Response
API_KEY = '6499830617274f538a929714de262794'

# Create your views here.

def news(request):
    url = f'https://newsapi.org/v2/top-headlines?country=tw&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articlesi = data['articles']

    contexti = {
        'articles' : articlesi
    }
        
    return render(request, 'news_api/news.html', contexti)

# def news(request):
#     url = f'https://newsapi.org/v2/top-headlines?country=tw&category=health&apiKey={API_KEY}'
#     response = requests.get(url)
#     data = response.json()

#     articlesj = data['articles']

#     contextj = {
#         'articles' : articlesj
#     }
        
#     return render(request, 'news_api/news.html', contextj)

# def news(request):
#     url = f'https://newsapi.org/v2/top-headlines?country=tw&category=sports&apiKey={API_KEY}'
#     response = requests.get(url)
#     data = response.json()

#     articlesk = data['articles']

#     contextk = {
#         'articles' : articlesk
#     }
        
#     return render(request, 'news_api/news.html', contextk)


    # context = print(type(data['articles']))
    # print(data)

    # for i in data['articles']: #yes
    #     print(i['source'])

    # for i in data['articles']: #yes
    #     print(i['description'])

    # for item in data['articles']['description']: #shit
    #     print(item)

    # for item in data['articles']: #yes
    #     for item2 in item:
    #         print(item2)

    # for description in data['articles']: #yes
    #     print(i['description'])

