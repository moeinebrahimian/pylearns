inp1 = float(input("ente your weight(kg): "))
inp2 = float(input("enter your hight(m):"))
bmi = inp1/ inp2**2
if bmi < 18.5:
    print(bmi)
    print("you are under weight")
elif 18.5 <= bmi <= 24.9:
    print(bmi)
    print("you are normal")
elif 25 <= bmi <= 29.9:
    print(bmi)
    print("you are over weight")
elif 30 <= bmi <= 34.9:
    print(bmi)
    print("you are obesity")
elif 35 <= bmi <= 39.9:
    print(bmi)
    print("you are extrme obesity")