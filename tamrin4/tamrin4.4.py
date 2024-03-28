a=[]
while True:
    p1=int(input("enter the numbers:"))
    a.append(p1)
    print(a)
    p2=input("stop?")
    if p2=="stop":
        break
print(a[::-1])