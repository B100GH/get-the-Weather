import os
import requests
#useing the open weather api
API_KEY = os.environ['apikey']
URL ='http://api.openweathermap.org/data/2.5/weather'
c = input('City to pull data for? -- ')
b = f"{URL}?appid={API_KEY}&q={c}"
a = requests.get(b)

if a.status_code == 200:
  d = a.json()
  #print(d)
  w = d['weather'][0]['description']
  t = (d['main']['temp'])
  t = (t - 237.15)# * 1.8
  print(str(w) + ' ' + str(round(t,3)))
  #quit()

elif a.status_code == 404:
  print('Error city not found code 404')

else:
  print('Error code '+str(a.status_code))