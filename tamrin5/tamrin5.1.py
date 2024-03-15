inp1=int(input("enter the lengh:"))
inp2=int(input("enter the width:"))
for i in range(inp1):
    for j in range(inp2):
        if (i+j)%2==0:
            print("#",end="")
        else:
            print("*",end="")
    print()