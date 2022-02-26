# ***************************************SNAKE WATER GUN*********************************************************************
# Provided below is the source code of Snake water Gun game
# snake wins over water
# water wins over gun 
# and gun wins over snake

import random
lst = ["s","w","g"]
chance= 10
chance_count = 0
computer_point = 0
user_point = 0

print("\t\t\t SNAKE WATER GUN \n\n")
print("Press \n s for Snake \n w for water \n g for gun \n")

#making the game using while
while chance_count < chance:
    user_input = input("Snake Water Gun : \n")
    computer_input = random.choice(lst)

    if user_input == computer_input :
        print("Tie for Both 0 points to each \n")
    
    # if user choose snake
    elif user_input == "s" and computer_input == "w" :
        user_point += 1
        print("You chose snake and computer chose water\n")
        print("You win this round and gets 1 point\n")
        print(f"Computer point is {computer_point} and user point is {user_point}\n")
    
    elif user_input == "s" and computer_input == "g" :
        computer_point += 1
        print(f"You chose {user_input} and computer chose {computer_input} \n")
        print("Compuetr win this round and gets 1 point\n")
        print(f"Computer point is {computer_point} and user point is {user_point} \n")
    
    #if user chooses water
    elif user_input =="w" and computer_input =="s":
        computer_point += 1
        print(f"You chose {user_input} and computer chose {computer_input}\n")
        print("Computer win this round and gets one point\n")
        print(f"user point is {user_point} amd computer point is {computer_point}\n")
    
    elif user_input =="w" and computer_input =="g":
        user_point += 1
        print(f"You chose {user_input} and computer chose {computer_input} \n")
        print("You win this round and gets one point\n")
        print(f"user point is {user_point} and computer point is {computer_point}\n")
    
    # if user chooses gun
    elif user_input =="g" and computer_input =="w":
        computer_point += 1
        print(f"You chose {user_input} and computer chose {computer_input}\n")
        print("Computer win this round and gets one point\n")
        print(f"user point is {user_point} amd computer point is {computer_point}\n")
    
    elif user_input =="g" and computer_input =="s":
        user_point += 1
        print(f"You chose {user_input} and computer chose {computer_input} \n")
        print("You win this round and gets one point\n")
        print(f"user point is {user_point} and computer point is {computer_point}\n")

    else : 
        print("You have given wrong input !!\n")

    chance_count += 1
    print(f"{chance_count} used out of {chance} \n")

print("Game over \n")

if user_point == computer_point :
    print(f"computer point is {computer_point} and user point is {user_point}\n")
    print("Tie\n")

elif user_point > computer_point :
    print(f"computer point is {computer_point} and user point is {user_point}\n")
    print("User wins\n")

elif user_point < computer_point :
    print(f"computer pint is {computer_point} and user point is {user_point}\n")
    print("Computer wins \n")



