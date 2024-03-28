import random
p1=int(input("enter the number of arrys:"))
list1=[]
while True:
    roll=random.randint(1,100)
    if roll not in list1:
        list1.append(roll)
        p1-=1
    else:
        continue
    if p1==0:
        print(list1)
        break    