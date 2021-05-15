import requests
from bs4 import BeautifulSoup
import csv
from decimal import Decimal

query = input('Enter product: ')
free_shipping = input('Enter free shipping: ')
max_price = Decimal(input('Enter maximum price : '))
# print(max_price)
for i in range(1,5):
    website = requests.get('https://www.ebay.com/sch/i.html?_nkw='+query+'&_pgn='+str(i)).text
    soup = BeautifulSoup(website, 'html.parser')
    # print(website.status_code)
    # print(soup)

    items = soup.select('.srp-results .s-item')
    # print(items)
    # print("Scraped page "+str(i))
    for item in items:
        # print(item.text)
        title = item.select_one('h3').text
        # print(title)
        price = item.select_one('.s-item__price').text.strip()
        # print(price)
        price_decimal = Decimal(price.split(' to ')[0][1:])
        # print(price)
        # print(price_decimal)
        shipping = item.select_one('.s-item__shipping').text.strip()
        # print(shipping)
        if price_decimal <= max_price:
            if free_shipping == 'y':
                if 'Free' in shipping:
                    print(f'{title}\n{price}\n{shipping}')
                    print('==============================================')
            else:
                print(f'{title}\n{price}\n{shipping}')
                print('==============================================')