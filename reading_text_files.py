#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip() # remove \n
        print(line)
print()

# x = open('DATA/mary.txt')
# # ...
# x.close()

with open('DATA/mary.txt') as mary_in:
    all_contents = mary_in.read()
    print(all_contents)
    print(len(all_contents))
    print(repr(all_contents))
print()

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print()

with open('DATA/mary.txt') as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
    print(all_lines)


with open('DATA/mary.txt', 'r') as mary_in:
    with open('mary2.txt', 'w') as mary_out:
        for line in mary_in:
            mary_out.write(line.upper())

with open('DATA/mary.txt', 'r') as mary_in:
    with open('mary3.txt', 'w') as mary_out:
        for line in mary_in:
            line = line.replace('Mary', 'Beatrice')
            mary_out.write(line.upper())


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


with open('fruitlist.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')


s = "And the Alice drank from the bottle"


if "Alice" in s:
    print("yahooooo")
