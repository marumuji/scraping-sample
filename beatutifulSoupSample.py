import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.ymori.com/books/python2nen/test2.html')
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

# 要素を指定して表示する
# print(soup.find('title').text)
# print(soup.find('h2'))
# print(soup.find('li'))

# 全てのli要素を表示する
# for element in soup.find_all('li'):
#   print(element.text)

# idを指定して、配下のli要素を表示する
chap2 = soup.find(id='chap2')
for element in chap2.find_all('li'):
  print(element.text)
