from math import factorial
inp = int(input("enter the widht:"))-1

for i in range(inp):
    for j in range(i):
        print("",end="")
    print()
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()