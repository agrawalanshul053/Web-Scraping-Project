import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(website.text,'html.parser')

# print(soup)
# print('\n\n\n\n')
# print(soup.prettify())

# title = soup.find('title')
# print(title.text)

link = soup.find('a')
title = soup.find('title')
# print(link)

# get element using class

quote = soup.find(class_='text')
# print(quote)

#find many elements as an array using tag

links = soup.find_all('a')  # list will be formed
# print(links)
# print(links.text) # error will come because we are extracting text from list
# for elem in links:
#     print(elem.text)


#find many elements as an array using class

quotes = soup.find_all(class_='text')   #return list of elements of class named as text
# print(quotes)


#find element using link address

login_link = soup.find(href='/login')
# print(login_link.text)


#parent cheldren
Quote = soup.find(class_='quote')
quote_text = Quote.find(class_='text')
quote_author = Quote.find(class_='author')
# print(quote_text.text)
# print(quote_author.text)

#Extraction using CSS selector

quote_text = soup.select_one('.text')
# print(quote_text.text)
quote_author = soup.select_one('.author')
# print(quote_author.text)

quotes = soup.select('.text') # returns list
# print(quotes)


quotes = soup.select(".quote")

for quote in quotes:
    text = quote.select_one('.text')
    author = quote.select_one('.author')
    tags = quote.select('.tag')
    print(text.text)
    print(author.text)
    for tag in tags:
        print(tag.text)
    print('============================================')