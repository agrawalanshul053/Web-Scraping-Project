import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(website.text,'html.parser')
# print(soup)
links = soup.select('.lister-list .titleColumn a')[:5]
# print(links)
for link in links:
    # print(link.attrs['href'])
    movie_link = link.attrs['href']
    website = requests.get(f'https://www.imdb.com{movie_link}')
    soup = BeautifulSoup(website.text, 'html.parser')
    # print(soup.title)
    title = soup.select_one('.title_wrapper > h1').contents[0].strip()  # contents separate the contents inside different html tags
    # print(title)
    runtime = soup.select_one('.subtext > time').text.strip()
    # print(runtime)
    plot = soup.select_one('.summary_text').text.strip()
    rating = soup.find(attrs={'itemprop': 'ratingValue'}).text
    # print(rating)
    rating_count = soup.find(attrs={'itemprop': "ratingCount"}).text
    # print(rating_count)

    cast_list = soup.select('.cast_list tr')[1:5]
    # print(cast_list)
    cast = ''
    for item in cast_list:
        cast += item.select('td')[1].text.strip() + ', '
    # print(cast[:-2])
    print(f'{title}\n{runtime}\n{plot}\n{rating}\n{rating_count}\n{cast}')
    print('======================================================================')
