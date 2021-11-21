import requests
from bs4 import BeautifulSoup

response = requests.get('https://tenki.jp/forecast/3/17/4610/14130/')
soup = BeautifulSoup(response.content, 'html.parser')

todayWeather = soup.find(class_='today-weather')
print(todayWeather)

# 今日の天気
print(todayWeather.find(class_ = 'weather-telop').text)

# 今日の天気 (最高・最低気温)
print(todayWeather.find(class_ = 'high-temp sumarry').text)
print(todayWeather.find(class_ = 'high-temp temp').text)
print(todayWeather.find(class_ = 'low-temp sumarry').text)
print(todayWeather.find(class_ = 'low-temp temp').text)

# 今日の天気（降水確率）
timeTable = []
rainProbatility = []
for element in todayWeather.find(class_ = 'precip-table').find_all('th'):
  timeTable.append(element.text)

for element in todayWeather.find(class_ = 'rain-probability').find_all('td'):
  rainProbatility.append(element.text)

print(rainProbatility)


