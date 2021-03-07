import requests

s_city = 'Gomel,BY'
city_id = 0
appid = 'b7b37d5d741b1ed6d19943e0f15215a7'
params = {'q' : s_city, 'units' : 'metric', 'lang' : 'ru', 'APPID' : appid}

try:
    res = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
    data = res.json()
    city_id = data['id']
    weather = 'Погода: ' + data['weather'][0]['description']
    temperature = 'Температура: ' + str(data['main']['temp'])
    temp_feels_like = 'Ощущается как: ' + str(data['main']['feels_like'])
    reply = weather + '\n' + temperature + '\n' + temp_feels_like
except Exception as e:
    print('Exception (find):', e)
    pass

   