
def double(x):
    return x*2

a=map(double,[1,2,3,4])

print(a)


b=list(map(double,[1,2,3,4]))

print(b)

print("--------------------------------------------------------")




map(lambda x : x**2,(1,2,3,4,5,6,7,8,9,10))

a=list(map(lambda x : x**2,(1,2,3,4,5,6,7,8,9,10)))

print(a)


print("--------------------------------------------------------")

lis1=[1,3,5,7,9]
lis2=[2,4,6,8,10]

lis4=list(map(lambda x,y:x*y,lis1,lis2))

print(lis4)

print("--------------------------------------------------------")

from functools import *

def toplam(x,y):
    return x + y

a=reduce(toplam, [2,34,5,6])

print(a)

print("--------------------------------------------------------")

from functools import *

def toplam(x,y):
    return x + y

a=reduce(toplam, [2,34,5,6])

print(a)


b=reduce(lambda x,y: x*y, [2,5,6,7])

print(b)

print("--------------------------------------------------------")

from functools import *
def maksimum(x,y):
    if (x>y):
        return x
    else:
        return y

a=maksimum(3,4)

print(a)

print("--------------------------------------------------------")

from functools import *
def maksimum(x,y):
    if (x>y):
        return x
    else:
        return y


b=reduce(maksimum,[-2,3,1,6,4])

print(b)

print("--------------------------------------------------------")

a=list(filter(lambda x: x % 2==0,[1,2,3,4,5,6]))

print(a)

print("--------------------------------------------------------")

def PrimeNumber(x):
    a=2
    if x==1:
        return False
    elif x==2:
        return True
    else:
        while(a<x):
            if (x % a == 0):
                return False
            a+=1
        return True

print(PrimeNumber(7))

b=list(filter(PrimeNumber,range(1,1000)))

print(b)








