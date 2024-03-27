import random
import time
from colorama import Fore

def check(game):
   for i in range(3):
      if a[i][0]==a[i][1] and a[i][2]==a[i][1]:
         win=a[i][0]
      elif a[0][i]==a[1][i]==a[2][i]==b:
         win=a[0][i]
   if a[0][0]==b and a[1][1]==b and a[2][2]==b:
      win=a[0][0]
   if a[0][2]==b and a[1][1]==b and a[2][0]==b:
      win=a[0][2]    
   return win

def board():
   for i in range(3):
      for j in range(3):
         print(a[i][j],end="")
      print()

start_time = time.time()
end_time = time.time()
a = [["-","-","-"],
   ["-","-","-"],
   ["-","-","-"]]

b="x"
c="o"
win = ''

board()
player=input("pc or player  ? :")
while True:

   while True:
      print("player 1")
      p1=int(input("enter the row:"))
      p2=int(input("enter the col:"))
      if p1>2 or p2>2 or p1<0 or p2<0:
         print("between 0 an 2")
      else:
         if "-" not in a[p1][p2]:
            print("its full")
         else:
            a[p1][p2]=Fore.RED+b    
            break



   win = check(a)   
   if win==b :
      print("player x win")
      break
   elif win==c:
      print("player o win")
      break
   while True:
      if player=="pc":  
        ranr=random.randint(0,2)
        ranc=random.randint(0,2)
        if "-" in a[ranr][ranc]:
            a[ranr][ranc]=Fore.BLUE+c
            break
    
      elif player=="player":
            print("player 2")
            player_inp1 = int(input("enter the row:"))
            player_inp2 = int(input("enter the col:"))
            if player_inp1>2 or player_inp2>2 or player_inp1 <0 or player_inp2<0:
                print ("between 0 an 2")
            else:
                if "-" not in a[player_inp1][player_inp2]:
                    print("its full")
                else:
                    a[player_inp1][player_inp2]=Fore.BLUE+c    
                    break
         
   board()
    
   win = check(a)   
   if win == b :
      print("player x win")
      break
   elif win == c:
      print("player o win")
      break

elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time) 
