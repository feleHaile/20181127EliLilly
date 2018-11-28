#!/usr/bin/env python

list1 = list()

places = ['Indianapolis', 'Vincennes', 'Terre Haute',
    'Muncie', 'Columbia', 'Lafayette', 'Nashville',
          'Angola', 'South Bend', 'Jackson Center']
list2 = []

colors = 'red purple yellow orange'.split()
print(places, '\n')
print(colors, '\n')

places.append('Gary')

print(places, '\n')

places.insert(0, "Carmel")

print(places, '\n')

places.insert(5, "Fishers")

print(places, '\n')

more_cities = ['Bloomington', 'Westfield']

places.extend(more_cities)

print(places, '\n')

# x = ['a', 'b', 'c']
# places.append(x)
# print(places, '\n')

del places[12]
print(places, '\n')

places.remove('Terre Haute')
print(places, '\n')

if 'Muncie' in places:
    print("Go Muncie!", '\n')

x = places.pop()
print(x)
print(places, '\n')

x = places.pop(2)
print(x)
print(places, '\n')

print(places[0])
print(places[10])
print(places[-1])
print(places[len(places)-1])

#  S[START:STOP]  S[:STOP]  S[START:] S[:]
#  S[START:STOP:STEP]
x = places[0:3]
print(x)
print(places[3:7])
print(places[:])
print(places[-3:])

print(places[-6:-3])

actress  = "Kate Winslet"
print(actress[:4])
print(actress[5:8])
print(actress[-4:])


print(places, '\n')

for place in places:
    print(place.upper())

print(f"place is {place}")
print()


print(list(enumerate(places)))
# for place in places:
#     print(place.upper())


for i, place in enumerate(places):
    print(i, place.upper())
print()

for i, place in enumerate(places):
    print(i, place.upper())
print()

#  range(STOP)  range(START, STOP)
#  range(START, STOP, STEP)
for i in range(5, 11):
    print(i)

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')


s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for ch in s[1::2]:
    print(ch)

r = range(1000000000000)

print(r)
