from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
from random import randint
import json
import time
import os.path as pt
from exceptions import TelegramNotify


def reviews() :

    url = 'https://outmaxshop.ru/testimonials?start=60'
    headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'    
        }
    cookie = {
        '412f84eb148c7a71272db3b09795154a' : '87f734490158c965a729d84dd78163b6',
        'regionality_city' : 'chelyabinsk'
    }


    html = requests.get(url, headers= headers, cookies=cookie)
    html.encoding = 'utf-8'
    text = html.text
    
    photosList = {}

    photosCount = 17

    soup = BeautifulSoup(text, 'lxml')

    blocks = soup.find_all('div', class_='col-md-12')

    for item in blocks :
        try:
            title = item.find('div', class_='block-reviews__item-title').text
            if 'кроссовки' in title.lower() :
                photos = item.find_all('a',class_='block-reviews__img')
                links = []
                for photo in photos :
                    link = 'https://outmaxshop.ru' + photo['href']
                    links.append(str(link))
                photosList[photosCount] = links
                photosCount += 1
                links = []
            else:
                continue
        except AttributeError:
            kk = 0

    with open(pt.abspath('reviews.json'), 'w') as file :
        data = json.dumps(photosList)
        file.write(data)
reviews()