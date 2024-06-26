
from gtts import gTTS
from os import path

words_bank=[]
def read_from_file():
    if path.exists("tamrin8/translate.txt"):
        f=open("tamrin8/translate.txt","r")
        temp=f.read().split("\n")
        for i in range(0,len(temp),2):
            my_dict={"en":temp[i],"fa":temp[i+1]}
            words_bank.append(my_dict)

        f.close()
    else:
        print("not found")



def show_menu():
    print("1--->  english to persian")
    print("2--->  persian to english")
    print("3---> add a new word")
    print("4---> exit")


def translate_english_to_persian():
    user_text=input("Enter your text: ")
    list_user_word=user_text.split(" ")
    output=""
    for word in list_user_word:
        for item in words_bank:
            if word == item["en"]:
                output=output+item["fa"]+" "
                break
        else:
            output=output+word+" "
    
    print(output)

    voice=gTTS(output,lang="en")
    voice.save("tamrin8/Voice.mp3")


def translate_persian_to_english():
    user_text=input("Enter your text: ")
    list_user_word=user_text.split(" ")
    output=""
    for word in list_user_word:
        for item in words_bank:
            if word == item["fa"]:
                output=output+item["en"]+" "
                break
        else:
            output=output+word+" "
    
    print(output)

    voice=gTTS(output,lang="en")
    voice.save("tamrin8/Voice.mp3")




def add_a_new_word_to_database():
    
    english=input("write english word: ")
    persian=input("write persian word: ")
    f= open("tamrin8/translate.txt","a")
    f.write("\n")
    f.write(english)
    f.write("\n")
    f.write(persian)
    f.close()
    print("your word is successfully added")




while True:
    read_from_file()
    show_menu()
    choice=int(input("Enter your choice: "))
    if choice==1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        add_a_new_word_to_database()
    elif choice == 4:
        print("thank you for using my translate ")
        break