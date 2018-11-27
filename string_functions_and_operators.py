#!/usr/bin/env python

actor = "George Clooney"
print(len(actor))
print(type(actor))

print(actor.upper())

actor.upper()

print(actor)

cave_man = 'Barney Rubble'

print(cave_man.count('b'))

print(cave_man.count('B'))

print(cave_man.lower().count('b'))

print(cave_man.find('Rub'))
print(cave_man.find('blech'))

s = "    All my exes live in Texas    "

print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s2 = "xyxxyyxxxyyyAll my exes live in Texasyyyyxxxx"

print("|" + s2.lstrip('xy') + "|")
print("|" + s2.rstrip('xy') + "|")
print("|" + s2.strip('xy') + "|")
print()

data = "Jan 5, 2018"
print(data.split())

more_data = "10:15:AM:IND:False"
print(data.split(':'))




