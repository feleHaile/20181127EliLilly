#!/usr/bin/env python

# display logic (GUI)
def hw():
    print("Hello world")

hw()

# business logic (DATA)
def get_message():
    return "Hello Lilly"

get_message()
m = get_message()
print(m)
print()

def hello(whom):
    print("Hello,", whom)

hello("World")
hello("Bob")
hello(3.1214)

def greet(greeting, *whom):
    print("whom:", whom)
    for w in whom:
        print(greeting, w)

greet("Hi", "Mom")
print()

greet("Hello", "Mom", "Sis", "Aunt Betty")
print()

greet("Hello")



def power(x, y=2):
    return x ** y

a = power(2, 5)
print(a)
a = power(5, 2)
print(a)

if True:
    x = 5

print(power(10))

def spam(x=2, y=5):
    return (x * y) ** y

print(spam())
print(spam(5, 8))
print(spam(7))

sal = 123  # pseudo-constant

def ham():
    actress = 'Kate Winslet'
    # other stuff here ...
    print("sal is", sal)
    return 100


for i in range(5):
    ham()


a = ham()







