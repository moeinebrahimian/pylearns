name=input("enter your frist name and your family:")
while True:
    p1=float(input("enter your math status:"))
    p2=float(input("enter your Science status:"))
    p3=float(input("enter your Specialized lesson status:"))
    x=(p1+p2+p3)/3
    if p1<=0 or p2<=0 or p3<=0 or p1>20 or p2>20 or p3>20:
        print("please choice higher than 1  or lower than 20")
        continue
    else:
        if x>=17:
            print("your name is :",name,)
            print(" and your status is good")
            break
        elif 17>x>=12:
            print("your name is :",name,)
            print("you are normal ")
            break
        elif x<12:
            print("your name is :",name,)
            print("your are fail")  
            break  