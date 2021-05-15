import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(website.text,'html.parser')
links = soup.select('.topic-list .md-crosslink')

# print(links)

for link in links[:8]:
    try:
        website = requests.get(link.attrs['href'])
        soup = BeautifulSoup(website.text, 'html.parser')
        name = soup.select_one('h1').text
        description = soup.select_one('.topic-identifier').text
        # print(name)
        # print(description)
        summary = soup.select_one('.topic-paragraph').text
        # print(summary)
        image = soup.select_one('.fact-box-picture img')
        # print(image)
        try:
            img_source = soup.select_one('.fact-box-picture img').attrs['src']
        except AttributeError as error:
            img_source = None
        # print(img_source)

        birth = soup.find(attrs={'data-label': 'born'}).find('dd').get_text(separator='|').split('|')[0]
        # print(birth)
        # print(type(birth))
        death = soup.find(attrs={'data-label': 'died'}).find('dd').get_text(separator='|').split('|')[0]
        # print(death)

        try:
            subjects_of_study = soup.find(attrs={'data-label': 'subjects of study'}).select_one(
                'ul')  # .get_text(separator='|').split('|')[0]
            subjects_items = subjects_of_study.select('li')
            subjects = ''
            for item in subjects_items:
                subjects += item.text.strip() + ','
        except AttributeError as error:
            subjects = None

        # print(subjects)
        # print(subjects_of_study)
        print(f'{name}\n{description}\n{img_source}\n{summary}\n{birth}\n{death}\n{subjects}')
    except:
        print("Something went wrong")
    print('====================================================================')

