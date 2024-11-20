from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.serializer import OrderSerializer
from django.http import HttpResponse
from main.models import News

import requests
from bs4 import BeautifulSoup
def index(request):
    return HttpResponse("hello world11")
class OrderView(ModelViewSet):

    def get():
        url = 'https://rtyva.ru/'
        page = requests.get(url).text
        # Turn page into BeautifulSoup object to access HTML tags
        soup = BeautifulSoup(page)
        # Находим все элементы с классом 'news-item'
        news_items = soup.find_all(class_='news-item')

        # Обработка найденных элементов
        for item in news_items[1:10]:
            news_name = item.find(class_='news-name').find('b').get_text()
            news_text = item.find(class_='news-text').find(class_='news-preview-text').find('p').get_text()
            try:
                News.objects.create(name=news_name, text=news_text)
            except:
                continue

    get()
    queryset = News.objects.all()
    serializer_class = OrderSerializer