import requests
from bs4 import BeautifulSoup

page = 1
next_button = True
while next_button:
    website = requests.get('https://quotes.toscrape.com/'+str(page))
    soup = BeautifulSoup(website.text, 'html.parser')
    next_button = soup.select_one('.next > a')
    quotes = soup.select('.qoute')
    print("Scrapped page"+str(page))
    for quote in quotes:
        text = quote.select_one('.text')
        author = quote.select_one('.author')
        print(text.text)
        print(author.text)
        tags = quote.select('.tag')
        for tag in tags:
            print(tag.text)
        print("=========================================================")
    page += 1

