import random
letters=["book","ali","moein","bag","case"]
word=random.choice(letters)
mistake=0
win=len(word)       
good_guess=[]
bad_guess=[]
while mistake<6:
    for i in range(len(word)):
        if word[i] in good_guess:
            print(word[i],end="")
        else:
            print(". ",end="")
    if win==0:
        print(" you win")
        break
    inp=input("enter your guess:")
    if len(inp)==1:
        if inp in word:
            print("well done")
            good_guess.append(inp)
            win-=1
        else:
            print("wrong!")
            bad_guess.append(inp)
            mistake-=1
    else:
        print("just 1 word")
if mistake==6:
    print("you lose") 
