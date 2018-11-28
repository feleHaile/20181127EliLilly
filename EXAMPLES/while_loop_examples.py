#!/usr/bin/env python

print("Welcome to ticket sales\n")

while x > 5:  # <1>
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # <2>
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break
    if raw_quantity.isdigit():
        quantity = int(raw_quantity)
        print("sending {} ticket(s)".format(quantity))
    else:
        print("Please enter a number")


i = 0
while i < 5:
    print(i)
    i += 1
print()
