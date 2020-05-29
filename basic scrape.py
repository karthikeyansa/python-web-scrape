from bs4 import BeautifulSoup
import requests
#basic web scraping
with open('simple.html') as html:
    soup = BeautifulSoup(html,'lxml')
#view source code
print(soup.prettify())

#search for tag
match= soup.title.text
print(match)
#(or)
match = soup.find('div',class_='body')
print(match)

#grab text
match = soup.find('div',class_='body')
text = match.h2.a.text
t2 = match.h2.a.text
print(text,t2)