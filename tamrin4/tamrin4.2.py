mazrab=1
factorial =1
inp=int(input("enter the factorial number :"))
if inp==0 or inp==1:
    print("ok")
while factorial <inp:
    mazrab+=1
    factorial*=mazrab
if inp==factorial :
    print("ok")
    
else:
    print("no")
        
  