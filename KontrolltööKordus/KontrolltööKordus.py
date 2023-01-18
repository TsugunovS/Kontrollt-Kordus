from math import * 
from random import * 
#5 (3)
randint(1,10)
int(input())






#5 (2)
positive=0
negative=0
a1=int(input("Sisestage number1: "))
a2=int(input("Sisestage number2: "))
a3=int(input("Sisestage number3: "))
if a1>0: positive +=a1 
elif a2<0: negative +=a2
int(input(a1*a2*a3))
print("Positive", positive, "Negative", negative)





#5 (1)
for i in range(2):
    x=str("   /v\ "*i)
    print(x, end="")
    print()
for i in range(2):
    x=str("  / v \ "*i)
    print(x, end="")
    print()
for i in range(2):
    x=str(" / v v \ "*i)
    print(x, end="")
    print()
for i in range(2):
    x=str("/vv v vv\ "*i)
    print(x, end="")
    print()



