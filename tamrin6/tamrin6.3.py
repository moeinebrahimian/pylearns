import math
from math import sqrt


def Cubic_equation (a,b,c,d):
    q = ((2 * a **3 ) / 27) - (a * b) /3 + c
    p = b - (a **2)/3
    delta = q**2 / 4 + p**3 / 27
    if delta >0:
        print("x=", -q/2 + sqrt (delta) **(1/3) + -q/2 + sqrt (delta) **(1/3) - a/3)
    elif delta == 0:
        print("x1=",(-2 * (q/2)**(1/3)) - a/3)
    
        print("x2=",(q/2)**(1/3) - a/3 )

        print("x2=",(q/2)**(1/3) - a/3 )
    else:
        print("x1=", (2/sqrt(3)) * sqrt(-p) * math.sin((1/3) * math.asin((3 * sqrt(3) *q ) / (2 * sqrt(-p) **3))) -a/3)
        print("x2=", (2/sqrt(3)) * sqrt(-p) * math.sin((1/3) * math.asin((3 * sqrt(3) *q ) / (2 * sqrt(-p) **3)) + (math.pi / 3)) - a/3 )
        print("x3=", (2/sqrt(3)) * sqrt(-p) * math.sin((1/3) * math.asin((3 * sqrt(3) *q ) / (2 * sqrt(-p) **3)) + (math.pi / 3)) - a/3 )

print("a is not 0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = float(input("d="))
Cubic_equation(a,b,c,d)