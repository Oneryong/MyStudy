#!/usr/bin/env python

def A():
    a = 10
    print("A a:", a)
    print(id(a))
    c = B(a)
    print("c:", c)
    print(id(c))
    print("A a:", a)
    print(id(a))  
    
def B(a):
    a = 20
    print("B a:", a)
    print(id(a))
    return a
    
if __name__ == "__main__":
    A()

input("Press <enter>")
