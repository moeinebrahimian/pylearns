p1=int(input("enter the frist  number:"))
p2=int(input("enter the second number:"))
d=(p1*p2)+1
if p1>p2:
    kmm=p1
if p2>p1:
    kmm=p2
javab=[]
for i in range(kmm,d):
    if i%p1==0 and i%p2==0:
        print(i)
        break