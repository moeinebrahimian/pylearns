def zarb(num1,num2):
 for i in range(1,num1):
    print("----------------------------")
    for j in range(1,num2):
        print(i,"*",j,"=" , i*j)
num1 = int(input("enter the coefficient:"))+1
num2 = int(input("enter the constans:"))+1
zarb(num1,num2)