import random
score = 0

print("Let's play Rock-Paper-Sicssors")

user_choice = input("Choose your weapon")
if user_choice.lower() == "rock":
    user_choice = 0
elif user_choice.lower() == "paper":
    user_choice = 1
elif user_choice.lower() == "sicssors":
    user_choice = 2
else:
    print("that is not a proper input")

computer_choice_num = random.randint(0,2)

if user_choice == computer_choice_num:
    print("DRAW")
elif user_choice > computer_choice_num:
    print("YOU WIN")
elif user_choice < computer_choice_num:
    print("YOU LOSE")
    
