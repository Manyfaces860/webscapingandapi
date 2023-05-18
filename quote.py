import bs4 as B
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.goodreads.com/quotes/tag/random').content
#print(response)

soup = BeautifulSoup(response, 'lxml')
info = soup.find('div' , class_ = 'mainContentContainer')

#print(info)
#author = quotes.find_all('span' ,class_ = 'authorOrTitle')
#print(author[0].text.strip())
quotes = info.find_all('div' , class_ = 'quoteText')
for i in range(len(quotes)):
    
    print(quotes[i].text.split('-')[0].replace('\n','').strip().replace('―','\n  ―').replace(',','\n'))
    


