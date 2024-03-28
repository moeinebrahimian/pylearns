def diamond(widht):

 for i in range(1, width):
    for j in range(1,width-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

 for i in range(width-1,0, -1):
    for j in range(1,width-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

width = int(input('Enter number of width: '))
diamond(width)