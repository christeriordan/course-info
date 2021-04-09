import requests
from bs4 import BeautifulSoup

def getTitle(webpage):
    page = requests.get(webpage)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[0]
    head = list(html.children)[1]
    return print(head.get_text())

getTitle("http://www.pythonscraping.com/pages/page1.html")

