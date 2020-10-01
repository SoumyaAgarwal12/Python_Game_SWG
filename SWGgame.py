# An Awesome project created by :--- SoumyaAgarwal
import random
chance=5
computer=0
you=0
print("Welcome to our Game! Snake, Water, Gun")
print("Instructions : \n1. The game was played by 5 times.\n2. Those player who has more number of wins will win.\n")
while chance!=0:
    chance -= 1
    option=["Snake","Water","Gun"]
    choose=random.choice(option)
    # print(choose)
    comp_ch=choose
    user_inp=input("Choose : 'S' or 'W' or 'G' : ")
    user_ch=user_inp.capitalize()
    def show():
        print(f"His Choice : {comp_ch}")
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
            print(f"Shhhhh.....I am {comp_ch} I've drunk the water. You Lose")
            computer+=1
        elif user_ch=="G":
            show()
            print(f"Dichkiauu....You've kill the {comp_ch}. You win")
            you+=1
        elif user_ch=="S":
            show()
            print("Draw Match! You both have same thing")
        else:
            print("Invalid Choice. Computer gets +1 point")
            computer+=1
    elif comp_ch=="Water":
        if user_ch=="W":
            show()
            print("Draw Match! You both have same thing")
        elif user_ch=="G":
            show()
            print(f"Ohh....Your weapon has drown in {comp_ch}. You Lose")
            computer += 1
        elif user_ch=="S":
            show()
            print(f"Ahh....Your Snake has drunk the whole water.You Win")
            you += 1
        else:
            print("Invalid Choice. Computer gets +1 point")
            computer+=1
    elif comp_ch=="Gun":
        if user_ch=="W":
            show()
            print(f"Yeahh....His weapon {comp_ch} has drown in your water. You Win")
            you += 1
        elif user_ch=="G":
            show()
            print("Draw Match! You both have same thing")
        elif user_ch=="S":
            show()
            print(f"Oohh....His weapon({comp_ch}) killed your Snake. You Lose")
            computer += 1
        else:
            print("Invalid Choice. Computer gets +1 point")
            computer+=1
    print("\n")
print(f"Computer's win : {computer}")
print(f"Your's win : {you}")
if(computer>you):
    print("You Lose!")
elif(computer<you):
    print("Congratuations!You win")
else:
    print("Draw Match")
