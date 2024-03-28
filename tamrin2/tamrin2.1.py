import random
score=0
pc=random.randint(10,40)
while True:
 hads=int(input("guees the number:"))
 score+=1
 if hads==pc:
  print("you win and your number of guees:",score)
  break
 if pc>hads:
  print("go up")
  continue
 elif hads>pc:
  print("go down")    
  continue