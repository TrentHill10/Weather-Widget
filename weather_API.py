import json
import requests

api_file = open("api.key", 'r')
key = api_file.read()

zip_code = str(22192)

#print('What is your zip code?')
#zip_code = input()

api_status = requests.get('http://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + zip_code + '&aqi=no')

api_info = api_status.text

#print(api_info)

parse_json = json.loads(api_info)

location = parse_json['location']
current = parse_json['current']
condition = current['condition']