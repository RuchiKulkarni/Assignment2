import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('python.db')
cursor=conn.cursor()
cursor.execute("CREATE TABLE if not exists scrapping (question TEXT,answer TEXT,url TEXT);")
url='https://www.udemy.com/topic/python/'
page = requests.get(url)
a1=page.content
soup=BeautifulSoup(a1,'html.parser')
a=soup.find_all('div',class_='panel--panel--3uDOH')
for data in a:
    question=data.find('span',class_='udlite-accordion-panel-title').text
    answer=data.find('div',class_='udlite-text-sm questions-and-answers--answer--2PMFk').text
    url = data.find('a',href=True)
    url=url['href']
    cursor.execute('insert into scrapping values(?,?,?)',(question,answer,url))
cursor=conn.cursor()
conn.commit() 
print("Data is inserted")
cursor.close()
conn.close()