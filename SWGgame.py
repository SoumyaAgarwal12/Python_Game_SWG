# An Awesome project created by :--- SoumyaAgarwal
import random

print("Welcome to our game! Snake, Water, Gun")
print("Instructions : \n1. There are 5 sets in a match. \n2. In each set, the player picks either snake, water, or gun, and the computer does the same. \n3. Snake beats water, gun beats snake, and water beats gun. \n4. Whoever wins more sets wins the match.\n")

while True:
    chance=5
    computer=0
    you=0
    while chance!=0:
        chance -= 1
        option=["Snake","Water","Gun"]
        choose=random.choice(option)
        # print(choose)
        comp_ch=choose
        user_ch=input("Choose : 'S' or 'W' or 'G' ").capitalize()
        def show():
            print(f"Computer's Choice : {comp_ch}")
            if user_ch=="S":
                user_p="Snake"
            elif user_ch=="W":
                user_p="Water"
            elif user_ch=="G":
                user_p="Gun"
            print(f"Your Choice : {user_p}")
        if comp_ch=="Snake":
            if user_ch=="W":
                show()
                print(f"Shhhhh... The {comp_ch} drank all the water. You lose!")
                computer+=1
            elif user_ch=="G":
                show()
                print(f"Bang! You killed the {comp_ch}. You win!")
                you+=1
            elif user_ch=="S":
                show()
                print("Draw Match! You both picked the same option!")
            else:
                print("Invalid Choice. The set goes to the computer.")
                computer+=1
        elif comp_ch=="Water":
            if user_ch=="W":
                show()
                print("Draw Match! You both picked the same option!")
            elif user_ch=="G":
                show()
                print(f"Ohh... Your gun malfunctions in the {comp_ch}. You lose!")
                computer += 1
            elif user_ch=="S":
                show()
                print(f"Ahh... Your snake drank all the water. You win!")
                you += 1
            else:
                print("Invalid Choice. The set goes to the computer.")
                computer+=1
        elif comp_ch=="Gun":
            if user_ch=="W":
                show()
                print(f"Ohh... His {comp_ch} malfunctioned in the water. You win!")
                you += 1
            elif user_ch=="G":
                show()
                print("Draw Match! You both picked the same option!")
            elif user_ch=="S":
                show()
                print(f"Oohh... His {comp_ch} killed your snake. You lose!")
                computer += 1
            else:
                print("Invalid Choice. The set goes to the computer.")
                computer+=1
        print("\n")
    
    print(f"Score: \n Computer: {computer} \n You: {you}")
    if computer>you:
        print("Too bad! You lost!")
    elif computer<you:
        print("Congratuations! You won!")
    
    replay= input("\n DO YOU WANT TO PLAY AGAIN ? enter y/n \n").lower()
    if replay == "y":
        continue
    elif replay == "n":
        print("THANKS FOR PLAYING! BYE!")
        exit()
    else:
       exit()
