#welcone to the colour combo game
import random


def generate_pattern(length,variables):
    pattern = ''
    for i in range(length):
        random_integer= random.randint(0,variables-1)
        colourlist= ["A","B","C","D","E","F","G","H","I","J",
                    "K","L","M","N","O","P",
                    "Q","R","S","T","U","V","W","X","Y","Z"]
        pattern += colourlist[random_integer]
    return pattern

def game(pattern,set_chances,set_len):
    chance = 1 # keeps track of chances taken
    while True:
        if chance == set_chances+1:
            print ("DEFEAT \n The original set was ", pattern, "\n Better luck next time")
            break
        else:
            print ("Enter the set", chance )
            n=input(":")
            n=n.upper()
            l_n=list(n)
            if n == "REVEAL":
                print (f"The correct answer is {pattern}")
                break
            if len(n) == len(pattern):
                r=0
                w=0
                for i in range (0,set_len):
                    if n[i]== pattern[i]:
                        r+=1
                for i in pattern:
                    if l_n.count(i)>0:
                        l_n.remove(i)
                        w+=1
                w -= r
                if r == set_len:
                    print ("BOOYAH! You made it in" , chance,"chances" )
                    break
                else:
                    print ("Positions = ", r, "Colours= ", w)
                    chance+=1
            else:
                print ("Invalid input")

print ("WELCOME TO THE COLOUR COMBO GAME")
print ("COLOUR CODES: \n A=RED \n B=BLUE \n C=GREEN \n D=YELLOW \n E=PINK \n F=ORANGE")


# SETTING DEFAULT VALUES

set_len=4  # Size of the combination
set_chances=10  # Max number of chances
set_variables=6  # Number of variables

while True:
    print ("Enter \n [0] to exit \n [1] to start \n [2] to know How to Play \n [3] for settings")
    choice=input(": ")

    if choice == "1": # The game starts
        print ("Enter \n [0] to exit \n [1] to start with a random set \n [2] to start with a custom set ")
        choice_1=input(": ")

        if choice_1=="0":
            continue

        elif choice_1=="1":

            pattern = generate_pattern(set_len,set_variables) #Generates a pattern
            game(pattern,set_chances,set_len)


        elif choice_1=="2":
            pattern = input("Enter a Pattern: " ) #original set
            pattern = pattern.upper()
           
            if len(pattern) == set_len:
                print (".\n" *30)
                game(pattern,set_chances,set_len)
            else:
                print ("Invalid input \nExpected length:",set_len)
        else:
            print ("Invalid input")

    elif choice == "0" :
        break
    elif choice=="3":

        while True:
            print ("Enter \n [0] to exit"
                   "\n [1] to change the size of the pattern"
                   "\n [2] to change number of chances"
                   "\n [3] to change number of variables"
                   "\n [4] for default settings")
            choice_3=input(": ")        
            if choice_3 == "0":
                break
            elif choice_3== "1":
                set_len = int(input("Enter a new size : "))
            elif choice_3=="2":
                set_chances = int(input("Enter the new chances : ")) 
                continue
            elif choice_3=="4":
                set_len=4
                set_chances=10
                set_variables=6
                continue
            elif choice_3=="3":
                n_set_variables=int(input("Enter the new number of variables: "))
                if n_set_variables >=26:
                    n_set_variables = 26
                set_variables = n_set_variables               
            else:
                print ("Invalid input")
    
    elif choice=="2":
        print ('''
How to Play:
1. You need to guess the correct pattern.
2. You win if you guess the correct pattern successfully.
3. You loose if you fail to guess the correct pattern.
4. "Positions" tells number correct positions and colours you guessed.
5. "Colours" tells number of colours you guessed correct but are not in right position.
                ''')
    else:
        print ("Invalid input")

    

print ("Thank you for playing")
print ("THE END")
