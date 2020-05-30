from bs4 import BeautifulSoup
import requests

def creator(website):
    source = requests.get(website).text
    soup = BeautifulSoup(source,'html.parser')
    return  soup