import psycopg2
from psycopg2.extras import RealDictCursor
import time
import pydantic

class Post(pydantic.BaseModel):
    quote: str

while True:
    try:
        conn = psycopg2.connect(host='localhost' , database='quoteapibyfast' , user='postgres',password='newPassword' , cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('database connection is successfull')
        break        
    except Exception as error:
        print('database connection is unsuccessfull')
        print('Error ', error)
        time.sleep(2)

import bs4 as B
from bs4 import BeautifulSoup
import requests
import random

response = requests.get('https://www.goodreads.com/quotes/tag/random').content
#print(response)

soup = BeautifulSoup(response, 'lxml')
info = soup.find('div' , class_ = 'mainContentContainer')

#print(info)
#author = quotes.find_all('span' ,class_ = 'authorOrTitle')
#print(author[0].text.strip())
quotes = info.find_all('div' , class_ = 'quoteText')
quotess = []
for i in range(len(quotes)):
    
    quotess.append(quotes[i].text.split('-')[0].replace('\n','').strip().replace('―','\n  ―').replace(',','\n'))
    
#def loading(post:Post):
#    try:
#        print(post.quote)
#    except Exception as error:
#        print('Error ', error)
#
#
#for i,v in enumerate(quotess):
#    s = {'quote':v}
#    post = Post(**s)
#    loading(post=post)   

for i in range(len(quotess)):
    cursor.execute("""INSERT INTO quotes (quote) VALUES (%s) """,(quotess[i],))
    print('done')
#cursor.execute("""SELECT * FROM quotes""")
#print(cursor.fetchone())
