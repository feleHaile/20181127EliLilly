#!/usr/bin/env python
import sys

i1 = 123
i2 = 0xABCD
i3 = 0b10011001

f1 = 1.234
f2 = 1.2
f3 = 1.
f4 = .234
f5 = 1.23432e22

c1 = 123j

print(type(c1))
print(c1.conjugate())
print(c1.real)
print(c1.imag)
print()

x = 23
y = 7

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)
print()
#  x++

x = 5
x += 3  # x = x + 3
x /= 2  # x = x / 2
x *= 100  # x = x * 100
print(x)

#  P E M D A S

a1 = 5
a2 = float(5)
print(a1, a2, '\n')
a1 = float(a1)

x = str(a1)
print(x)
print(a1)

print(bool(x))

print(int(4.5345))
print(int("  123   "))

value = "DeadBeef"
print(int(value, 16))
print(int('10011001', 2))

x = 238749238749283749238749283749283749238749287349287349287349287349287349287349827394872394872934872938472983749283749287349283749287349287349827349827349872938472938472983472983749287349287349827349872394

print(x + 1)

print(sys.float_info)


