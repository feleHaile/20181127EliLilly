#!/usr/bin/env python

c1 = ['red', 'blue', 'purple', 'black', 'green']
c2 = ['green', 'blue', 'white', 'brown', 'pink']

s1 = set(c1)
s2 = set(c2)
s2.add('taupe')

print('red' in s1)
print(s1)

print("both:", s1 & s2)
print("either:", s1 | s2)
print("just one:", s1 ^ s2)
print("s1 only:", s1 - s2)
print("s2 only:", s2 - s1)
