#!/usr/bin/env python
from collections import defaultdict

def zero():
    return 0

d = defaultdict(zero)




d1 = dict()
d2 = {'red': 5, 'purple': 9, 'white': 3}
print(d2)
d3 = {}
d4 = dict(red=5, purple=9, white=3)
d4['black'] = 1
d4['orange'] = 2
print(d4)

for k, v in d4.items():
    print(k, v)
print()

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

airports['IND'] = 'Indianapolis'
print(airports, '\n')

del airports['ABQ']
print(airports, '\n')


data = {
    'jan': (31, 'January'),
    'feb': (28, 'February'),
    'mar': (31, 'March'),
}

print(data['jan'])
print(data['jan'][0])
print()
print(data.get('jan'))
print(data.get('apr'))
print(data.get('apr', ('30', 'April')))
#
print(data.setdefault('apr', ('30', 'April')))

print("oct" in data)
print(data['apr'])
print("feb" in data)

print(data)

print(data.keys())
print(data.values())


print(airports)

more_airports = {'ANG': 'Angola', 'HEL': 'Helena',
    'ELM': 'Elmira/Corning', 'MCO': 'Disneyland'}

airports.update(more_airports)

print(airports, '\n')


for abbr, airport_name in airports.items():
    print(abbr, airport_name)
print()
print(airports.items(), '\n')


for abbr, airport_name in sorted(airports.items()):
    print(abbr, airport_name)
print()

# non-pythonic: (Guido won't like you)
for abbr in sorted(airports):
    print(abbr, airport[abbr])


