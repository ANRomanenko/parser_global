import requests
from bs4 import BeautifulSoup

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

HOST = "https://patrik.com.ua/"

url = 'https://patrik.com.ua/konstruktory/'

r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, 'lxml')

item = soup.find('div', class_='col-lg-3 col-md-3 col-sm-3 col-xs-6 product-col col-fullwidth')

code = item.find('p', class_='sku').get_text(strip=True)
title = item.find('div', class_='product-meta-inner').find('a').get_text(strip=True)
print(code + '\n' + title)
