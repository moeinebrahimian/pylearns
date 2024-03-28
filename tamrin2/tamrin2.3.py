sum=0
miangin=0
while True:
    i=int(input("enter the number:"))
    miangin+=1
    sum+=i
    stop=input("exit?")
    if stop=="exit":
        mian=sum/miangin
        print("score is : ",mian)
        break