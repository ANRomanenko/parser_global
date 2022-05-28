import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []
header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

HOST = "https://patrik.com.ua/" # Константа

for count in range(1, 1 + 1):
    sleep(1)
    url = f'https://patrik.com.ua/konstruktory/?page={count}'

    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all('div', class_='col-lg-3 col-md-3 col-sm-3 col-xs-6 product-col col-fullwidth')

    for card in data: # Цмкл for (который проходит по html тегам в карточке товаров)

        card_link = card.find('div', class_='product-img img images clearfix').find('a').get('href')
        list_card_url.append(card_link)


for card_link in list_card_url:

    response = requests.get(card_link, headers=header)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find('div', class_='wrappers clearfix')
    title = data.find('div', class_='product-info').find('h1').get_text(strip=True)
    product_code = data.find('div', class_='col-xs-6 col-sm-6 prod-sku').get_text(strip=True)
    try:
        text = data.find('div', class_='tab-pane active').get_text(strip=True)
    except AttributeError:
        continue
    print(title + '\n' + product_code + '\n' + text + '\n\n')






        # title = card.find('div', class_='product-meta-inner').find('a').get_text(strip=True)
        # product_code = card.find('p', class_='sku').get_text(strip=True)
        # price = card.find('div', class_='price').get_text(strip=True)
        # availability = card.find('div', class_='text-in-stock').get_text(strip=True)
        # card_link = card.find('div', class_='product-img img images clearfix').find('a').get('href')
        # card_link_img = card.find('a', class_='img').find('img').get('src')
        #
        # print(title + '\n' + product_code + '\n' + price + '\n' + availability + '\n' + card_link + '\n' + card_link_img + '\n\n')
        # print('Парсинг завершен!', 'собрано', len(data), 'карточек товара!')







# soup = BeautifulSoup(response.text, 'lxml')
#
# item = soup.find_all('div', class_='col-lg-3 col-md-3 col-sm-3 col-xs-6 product-col col-fullwidth')
#
# for card in item:
#
#     code = card.find('p', class_='sku').get_text(strip=True)
#     title = card.find('div', class_='product-meta-inner').find('a').get_text(strip=True)
#     price = card.find('div', class_='price').get_text(strip=True)
#     availability = card.find('div', class_='text-in-stock').get_text(strip=True)
#     link = card.find('div', class_='product-img img images clearfix').find('a').get('href')
#     print(code + '\n' + title + '\n' + price + '\n' + availability + '\n' + link + '\n\n')
