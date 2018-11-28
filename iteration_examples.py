#!/usr/bin/env python

colors = ['purple', 'green', 'blue']

# iterate over elements of sequence
for color in colors:
    print(color)
print()

# for i in range(len(colors)):
#     print(colors[i])

for i, color in enumerate(colors):
    print(i, color)
