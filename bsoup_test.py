

#from bs4 import BeautifulSoup
#file open('name.html')
#html = file.read()
#soup = BeautifulSoup(html, html.parser')
#l = soup.findAll('h2')
#for item in l:
#    print item.txt

from bs4 import BeautifulSoup
import requests
url = 'https://dragonage.fandom.com/wiki/Category:Characters?from=C'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href','class'))
l = soup.find('c')
print (l.text)
