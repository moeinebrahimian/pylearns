import instaloader

file = open("unflow.txt" , "r")
old=[]
for i in file:
    old.append(i)
file.close()

insta = instaloader.instaloader()
user_name = input("please enter your user name:")
pasword = input("enter the password:")
insta.login(user_name,pasword)
print("ok shod")
user_name2 = input("enter your user name:")
profile = instaloader.profile.from_username(insta.context,user_name2)

new = []
for new_fllower in profile.get_fllowers():
    new.append(new_fllower)

for new_fllower in new:
    if new_fllower not in old:
        print("your new fllower are:", new_fllower)

file = open("unflow.txt","w")
for f in new:
    file.write(f + "/n")
file.close
