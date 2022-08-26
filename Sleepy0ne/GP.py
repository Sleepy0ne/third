def Player():
  hp = 30
  print(hp)
 
 #player = 30
 #def(enemy)
  #enemy = 20
  #def(sword)
   #sword = -15   
#The start
name = input("Welcome, To begin. Please enter a Name. Let be known you will use this name all throught the game. ")
yesorno = input(name + ", Are you sure this is the name you want? (Can't go back after you decide!)")
if "yes" in yesorno:
  print("Then let's begin.")
  print("You wake awaken deep in forest agaisnt a tree. It seems you've forgotten everything but you name. Your name is " + name + ". You look around a bit to notice large claw marks agaisnt the trees and dirt.")
  choice = input("What do you do?")
  if "Run away" in choice:
    print(Player())
else:
    name2 = input("Enter name: ")
    print(name2 + ", Hopefully this is what yu wanted. Let's begin." )
    print("You wake awaken deep in forest agaisnt a tree. It seems you've forgotten everything but you name. Your name is " + name2 + ". You look around a bit to notice large claw marks agaisnt the trees and dirt.")

