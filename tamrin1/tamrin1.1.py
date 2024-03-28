
import math

num1=float(input("enter the number:"))
p1=input("what do you want(+,-,/,,*,//,sqrt,cos,sin,cot,tan,factorial):")
if p1 in("+","-","/","*"):
 num2=float(input("enter the second number:"))
if p1=="+":
   print(num1+num2)
elif p1=="-":
   print(num1-num2)
elif p1=="*":
   print(num1*num2) 
elif p1=="/":
   print(num1/num2)  
elif p1=="sqrt":
   print(math.sqrt(num1))   
elif p1=="cos":
   x1=(math.cos(num1))
   print(x1*math.pi/180)
elif p1=="sin":
   x2=(math.sin(num1))
   print(x2*math.pi/180)
elif p1=="tan":
   x3=(math.tan(num1))
   print(x3*math.pi/180)
elif p1=="factorial":
   print(math.factorial(num1)) 
elif p1=="cot":
  c1=math.cos(num1)/math.sin(num1)
  print(c1*math.pi/180)