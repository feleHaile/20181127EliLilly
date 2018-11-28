#!/usr/bin/env python


def spam(p1, p2, p3):
    print(p1, p2, p3)
    return "blech"


x = spam(1, 2, 3)
print(x)

x = spam(p3=3, p1=14, p2=9)

def ham(p1, p2, *, p3=None):
    print(p1, p2, p3)

ham(5, 6, p3=7)
ham(p2=9, p1=18, p3=37)
ham(10, 20)

def toast(*values):
    print(values)

toast()
toast(1, 2, 3)
toast(5, 8, 9, 11)


#        |<==pos====>| |<===named ==>|
#          REQ    OPT    REQ    OPT
def wacky(p1, p2, *p3, p4, p5, **p6):
    pass


def still_wacky(p1, p2, **p6):
    print(p6)


still_wacky('a', 5, file='foo.txt', repeat=5)

