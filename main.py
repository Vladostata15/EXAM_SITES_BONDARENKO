import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent


url = 'https://allo.ua/ua/roboty-pylesosy/'
headers = {'fake-user': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
products = soup.find_all('div', class_ = 'product-card')

class Main:
    def __init__(self):

        for product in products:
            title_product = product.find('a', class_ = 'product-card__title')
            print(title_product.text)
            old_price = product.find('div', class_ = 'v-pb')
            if old_price.text != "":
                print(old_price.text)
            with open('products' , 'a', encoding='utf-8') as file:
                file.write(f'{title_product.text}\n {old_price.text}\n')


obj = Main()

