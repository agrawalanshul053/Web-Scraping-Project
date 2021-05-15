import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(website.text,'html.parser')
first_table = soup.select_one('.wikitable')
# print(first_table)
table_rows = first_table.select('tr')[1:-1]
# print(table_rows[:3])
csv_data = [['Rank','Name','Population','Percentage','Date','Source']]


for row in table_rows:
    rank = row.find('th').text.strip()
    # print(rank)
    # print(row)
    table_data = row.select('td')
    Countryname = table_data[0].find('a').text
    # list = [data.text for data in table_data]
    # print(list)

    # print(Countryname)
    Population = table_data[1].text
    # print(Population)
    Percentage = table_data[2].text
    # print(Percentage)
    Date = table_data[3].text
    # print(Date)
    Source = table_data[4].text.strip().split('[')[0]
    # print(Source)

    csv_data.append([rank,Countryname,Population,Percentage,Date,Source])
# print(csv_data)
with open('countries_population.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)