name=input("Type your name: ")
print("Welcome ",name," to this adventure!")

answer=input("You are on a dirt road, it has come to an end and you can go left or right . Which way you would go? ").lower()


if answer == "Left":
    answer=input("You come to a river , you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer=="swim":
        print("You swim across and you were eaten by an alligator.")
    elif answer=="walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
         print("Not a valid option . You lose.")

elif answer == "right":
   answer = input("You come to the bridge , it looks wobbly, do you want to cross it or head back (cross/back)? ")
   if answer=="back":

        print("You go back to main road.")
   elif answer=="cross":
      answer=input("You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)? ")
       
      if answer=="yes":
        print("You talk to the stranger and you win")
      elif answer=="no":
        print("you ignore the string and you lose")   
      else:
            print("Not a valid option . You lose.")

   else:
         print("Not a valid option . You lose.")
else:
    print("Not a valid option . You lose.")

print("Thank you for trying", name)