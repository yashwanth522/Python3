import requests

resp = requests.get('http://api.openweathermap.org/data/2.5/weather?id=5368361&appid=b18f2edd9b923cb53111e72b5e87d60e')
if resp.status_code != 200:
    # This means something went wrong.
    raise IOError('GET /data/ {}'.format(resp.status_code))
else:
    print("There is a response")

todo_item = resp.json()
main_data = todo_item['main']

temp_fahrenheit = main_data['temp']*1.8-459.67
temp_celsius = main_data['temp'] - 273.15

# print("............Complete JSON Response is..........\n",todo_item)

print("Weather of %s is %s in Kelvin" %(todo_item['name'], main_data['temp']))
print("Weather of %s is %s in Fahrenheit" %(todo_item['name'], temp_fahrenheit))
print("Weather of %s is %s in Celsius" % (todo_item['name'], temp_celsius))
