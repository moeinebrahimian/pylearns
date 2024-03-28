p1=float(input("enter the frist number:"))
p2=float(input("enter the second number:"))
p3=float(input("enter the third number:"))
x1=p2+p3
x2=p1+p3
x3=p1+p2
if p1==p2 and p1==p3:
    print("its curect")
if p1>p2 and p1>p3:
    if x1>p1:
     print("its curect")
    else:
       print("its not")
if p2>p1 and p2>p3:
    if x2>p2:
     print("its curect")
    else:
       print("its not")
if p3>p2 and p3>p1:
    if x3>p3:
     print("its curect")
    else:
       print("its not")

