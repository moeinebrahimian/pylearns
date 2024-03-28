p1=int(input("enter the number:"))
while True:
    if p1%2==0:
     print("#",end="")
     p1-=1
    else:
       print("*",end="")
       p1-=1
    if p1==0:
       break