#!/usr/bin/env python
import sys

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

# list comprehension
#  [
new_list = [each_element.upper() for each_element in fruits]

# apply(fruits, upper)

print("f1:", new_list, '\n')

# i = 0
# while True:
#     f = fruits[i]
#     # do something
#     i = i + 1
#     if i == len(fruits):
#         break


f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2", f2, '\n')



# NEW_LIST = [EXPRESSION_YOU_WANT for VAR in ITERABLE if CONDITION]
f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2", f2, '\n')

old_names = ['big thing', 'old thing', 'new thing']

new_names = [s.replace(' ', '_') for s in old_names]
print(new_names)

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

files = ['foo.log', 'bar.log', 'blah.txt', '']


x = ['pig', 'dog', 'cat']
y = ['cow', 'horse', 'wolf']

x.append(y)  # append object y

print("x:", x)
x.extend(y) # add each item of iterable y
print("x:", x)

x.extend('bear')
print("x:", x)

# x.extend(5)
# print("x:", x)
x.append('bear')
print("x:", x)

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people if len(p[1]) > 5]
print(last_names, '\n')

last_names = []
for p in people:
    if len(p[1]) > 5:
        last_names.append(p[1])
print()

#  (EXPR for VAR in ITERABLE if CONDITION)
g = (f.upper() for f in fruits)

print(g)

for fruit in g:
    print(fruit)
print()

last_names_gen = (p[1] for p in people)
print(last_names_gen)

for last_name in last_names_gen:
    print(last_name)

print(sys.getsizeof(new_list))
print(sys.getsizeof(g))
