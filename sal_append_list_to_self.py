#!/usr/bin/env python

x = ["bear"]

x.extend(x)

print(x)

print(dir(x))

animals = ['bear', 'otter', 'wolf', 'moose']


print('\n'.join(animals))

# sep.join(SEQUENCE-of-STRINGS)

print("/".join(animals))

for animal in animals:
    print(f"{animal}\n")
