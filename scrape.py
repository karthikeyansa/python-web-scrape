from bs4 import BeautifulSoup
import requests


website = 'https://vigneshwarravichandran.ml/'
source = requests.get(website).text

soup = BeautifulSoup(source,'lxml')
#source code
#print(soup.prettify())
#Extract all relative links
#matches = soup.find_all('a',href = True)
#for match in matches:
#    print(website+match['href'],end='\n',sep='\n')
#print('done')
#to go and see first post content
firstpost = soup.find('div',class_='post').a['href']
#to go
#print('Click this link->',end='')
#print(website+firstpost)
#see content
link = website+firstpost
context = requests.get(link).text
soup = BeautifulSoup(context,'lxml')
print(soup.prettify())
content = soup.find('div',class_='content container').text
print(content)

