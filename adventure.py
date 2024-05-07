name = input("Type your name: ")

print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road! It has come to an end! You can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type WALK to walk around or SWIM to swim accross").lower()
    if answer == "swim":
        print("You swam accross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game")  
    else:
        print("Not a valid option. You lose")      

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? Choose one (CROSS/BACK)").lower()
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (YES / NO) ? ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You Win!")
        elif answer == "no":
            print("You ignored the stranger, they are offended and you lose.")
        else:
            print("Not a valid option. You lose")        
    else:
        print("Not a valid option. You lose")        

else:
    print("Not a valid option. You lose.")  

print("Thank you for trying", name)      