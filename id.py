from requests import Session
from bs4 import BeautifulSoup
from time import sleep

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

work = Session()

work.get("https://quotes.toscrape.com/", headers=header)

response = work.get("https://quotes.toscrape.com/login", headers=header)

soup = BeautifulSoup(response.text, "lxml")

token = soup.find('form').find('input').get('value')

data = {"csrf_token": token, "username": "noname", "password": "password"}

result = work.post("https://quotes.toscrape.com/login", headers=header, data=data, allow_redirects=True)
print(result.text)