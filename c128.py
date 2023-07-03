from bs4 import BeautifulSoup
import csv
import time
import requests
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
startable=soup.find('table')
temp_list=[]
table_rows=startable.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)
starname=[]
radius=[]
mass=[]
distance=[]
for i in range(1,len(temp_list)):
    starname.append(temp_list[i][0])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])
    distance.append(temp_list[i][5])
dataframe=pd.DataFrame(list(zip(starname,radius,mass,distance)),columns=['Brown Dwarf','Radius','Mass','Distance'])
print(dataframe)
dataframe.to_csv('star1.csv')
