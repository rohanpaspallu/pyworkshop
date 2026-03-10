import json
with open('cities.json', 'r') as file:
    cities = json.load(file)
    print(cities)

from pprint import pprint
pprint(cities)