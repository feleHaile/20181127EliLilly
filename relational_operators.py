#!/usr/bin/env python


#  == != < > <= >=

# and or not

print(12 and 5)  # bool(12) and bool(5)
print(5 and 12)
print(0 and 22)
print(None and 22)

print(True)
print(int(True), int(False))

# if x == True: ....
# same as if x == 1: ....
# if bool(x) == True: ....
# if x: ....

# False
#  if X is numeric:  when X is 0

# if X is a container (list, str, tuple):
#  when len(X) is 0
print()

a = 5
b = 0

print(a and b)
print(b and a)

print(a or b)
print(b or a)
print(not a)
print(not b)

if (a > 0) and (b < 100):
    print("This is good enough for me")

x = "abc"
y = "abc"
z = "abcde"

print(x == y)
print(x == z)

print(x > y)
print(x > z)

m = "mmmmm"

print(x < m)
print(x < z)
