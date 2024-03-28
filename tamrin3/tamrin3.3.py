a=[]
b=[]
while True:
    p1=int(input("enter the numbers:"))
    a.append(p1)
    b.append(p1)
    p2=input("stop?")
    if p2=="stop":
     break
b.sort()
if a==b:
   print("ok")
else:
   print("no")