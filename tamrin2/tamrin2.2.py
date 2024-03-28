import random
pc_score=0
m_score=0
pc1=["rock","siccer","paper"]
while True:
    m=input("what did you want ?rock,paper,siccer:")
    pc=random.choice(pc1)
    if m==pc:
        print(pc)
        print("draw")
    elif m=="rock" and pc=="paper":
        print(pc)
        pc_score+=1
        print("pc score is:",pc_score)
        print("your score is:",m_score)
        print("pc win")
    elif m=="rock" and pc=="siccer":
        print(pc)
        m_score+=1
        print("pc score is:",pc_score)
        print("your score is:",m_score)
        print("you win")
    elif m=="siccer" and pc=="rock":
            print(pc)
            pc_score+=1
            print("pc score is:",pc_score)
            print("your score is:",m_score)
            print("pc win")
    elif m=="siccer" and pc=="paper":
            print(pc)
            m_score+=1
            print("pc score is:",pc_score)
            print("your score is:",m_score)
            print("you win")
    elif m=="paper" and pc=="siccor":
            print(pc)
            pc_score+=1
            print("pc score is:",pc_score)
            print("your score is:",m_score)
            print("pc win")
    elif m=="paper" and pc=="rock":
            print(pc)
            m_score+=1
            print("pc score is:",pc_score)
            print("your score is:",m_score)
            print("you win")
    
    if pc_score==5 :
         print("you lose") 
         break
    elif m_score==5:
          print("you just win")     
          break