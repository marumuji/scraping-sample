import requests
from bs4 import BeautifulSoup

response = requests.get('https://tenki.jp/forecast/3/17/4610/14130/')
soup = BeautifulSoup(response.content, 'html.parser')

todayWeather = soup.find(class_='today-weather')
tomorrowWeather = soup.find(class_='tomorrow-weather')
# print(todayWeather)
# print(tomorrowWeather)

# 今日の天気
print('■今日の天気')
print(todayWeather.find(class_ = 'weather-telop').text)

# 今日の天気 (最高・最低気温)
print('■今日の最高・最低気温')
print(todayWeather.find(class_ = 'high-temp sumarry').text, ': ', end='')
print(todayWeather.find(class_ = 'high-temp temp').text)
print(todayWeather.find(class_ = 'low-temp sumarry').text, ': ', end='')
print(todayWeather.find(class_ = 'low-temp temp').text)

# 今日の天気（降水確率）
timeTable = []
rainProbatility = []
for element in todayWeather.find(class_ = 'precip-table').find_all('th'):
  timeTable.append(element.text)

for element in todayWeather.find(class_ = 'rain-probability').find_all('td'):
  rainProbatility.append(element.text)

print('■今日の降水確率')
print(timeTable[1], ':', rainProbatility[0])
print(timeTable[2], ':', rainProbatility[1])
print(timeTable[3], ':', rainProbatility[2])
print(timeTable[4], ':', rainProbatility[3])

print('--------------------------------------------------')

# 明日の天気
print('■明日の天気')
print(tomorrowWeather.find(class_ = 'weather-telop').text)

# 明日の天気 (最高・最低気温)
print('■明日の最高・最低気温')
print(tomorrowWeather.find(class_ = 'high-temp sumarry').text, ': ', end='')
print(tomorrowWeather.find(class_ = 'high-temp temp').text)
print(tomorrowWeather.find(class_ = 'low-temp sumarry').text, ': ', end='')
print(tomorrowWeather.find(class_ = 'low-temp temp').text)

# 明日の天気（降水確率）
timeTable = []
rainProbatility = []
for element in tomorrowWeather.find(class_ = 'precip-table').find_all('th'):
  timeTable.append(element.text)

for element in tomorrowWeather.find(class_ = 'rain-probability').find_all('td'):
  rainProbatility.append(element.text)

print('■明日の降水確率')
print(timeTable[1], ':', rainProbatility[0])
print(timeTable[2], ':', rainProbatility[1])
print(timeTable[3], ':', rainProbatility[2])
print(timeTable[4], ':', rainProbatility[3])

