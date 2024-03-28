p1=int(input("enter the frist number:"))
p2=int(input("enter the second number:"))
if p1>p2:
    bmm=p1
else:
    bmm=p2
for i in range (bmm,0,-1):
    if p1%i==0 and p2%i==0:
        print(i)
        break