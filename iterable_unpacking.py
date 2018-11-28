#!/usr/bin/env python

# iterable unpacking
person = 'Bill', 'Gates', 'Microsoft'

first_name, last_name, product = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft', 'Seahawks'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft', 'Gates Foundation'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'git'),
    ('John', 'Strickler'),
]

print(people[0])
print(people[0][0])
print(people[0][0][0])
print(people[0][0][0][0][0][0][0][0][0])

first_name, last_name, product = people[0]
print(first_name, last_name, '\n')
print()

for first_name, last_name, *product in people:
    print(first_name, last_name, product)
print()
