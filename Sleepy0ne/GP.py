def deathinsta():
  hits = 1
  dmg = 80
  hp = 50
  hp -= dmg
  print('Attack # ',hits,' DMG',dmg,'  HP',hp)
  hits += 1
  dmg += 4
  if hp <=0:
    print("GAME OVER!")
    print("Try again?")
    retry=input("(Yes),(No)")
    if "Yes" in retry:
      print(choice)
    if "No" in retry:
      print("Wh-What? You weren't suppose to just give up!")
      print("Please, Try again!")
      retry2 =input("(Yes),(Yes),(No)")
      if "Yes" in retry2:
         (choice)
      if "No" in retry2:
        print("Fine, We can sit here. All day.")
        import time
        time.sleep(8)
        print("Bored yet? Or is just sitting around more fun then playing the game?")
        time.sleep(10)
        print("I'm bored.Are you?")
        time.sleep(2)
        print("No? I guess I'll wait.")
        time.sleep(12)
        print("Sure would be nice to do something...")
        print("If this game of my is not SO inteseting. Then let's look at other games.. like.. This.")
        time.sleep(1)
        print("Give it a second...")
        time.sleep(4)
        print("(You are given a finget spinner.)")
        time.sleep(3)
        SPIN = input("(Do you wish to spin the Finget spinner.) YES or no")
        if "YES" in SPIN:
          print("Congrats. You now are holding a spinning Finget spinner.")
          time.sleep(2)
          print("You wanna do it again?")
          Spin2 = input("(Yes or No)")
          if "Yes" in Spin2:
            print("(You watch it spin faster)") 
            time.sleep(3)
            print("This must be so funnn...")
            print("You have fun with that")
            sping=1
            while sping < 10:
              spin5=input("Spin?")
              if "Yes" in spin5:
                print("You spin it.")
                sping += 1
                if sping==10:
                  print("Done?")
                  print("Don't brother answering. I'm tired already of watching you mess with one of those.. Spinners...")
                  time.sleep(3)
                  print("Why are they popular anyways? They are so... Eh. All you do is spin it. There's no real joy in doing it.")
                  time.sleep(4)
                  print("How about something else.. Hm...")
                  time.sleep(6)
                  print("Here, How about some Rochambeau.")
                  

                  import random
                  CHOICES = 'rps'
                  def get_player_choice():
                    """Get user input and validate it is one of the choices above"""
                    player_choice = None
                    while player_choice is None:
                        player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
                        if player_choice.lower() not in CHOICES:
                          player_choice = None
                    return player_choice.lower()


                  def get_computer_choice():
                    """Have the computer pick one of the valid choices at random"""
                    computer_choice = random.randint(0, 2)
                    computer_choice = CHOICES[computer_choice]
                    return computer_choice


                  def is_draw(player_choice, computer_choice):
                    """Check if game was a draw"""
                    if player_choice == computer_choice:
                        return True


                  def print_winner(player_choice, computer_choice):
                    """Check to see who won"""
                    if player_choice == 'r' and computer_choice == 's':
                        print('Player wins!')
                    elif player_choice == 's' and computer_choice == 'p':
                        print('Player wins!')
                    elif player_choice == 'p' and computer_choice == 'r':
                        print('Player wins!')
                    else:
                        print('Computer wins!')
                        print('%s beats %s' % (computer_choice, player_choice))


                  def play_game():
                    """play the game"""
                    player_choice = get_player_choice()
                    computer_choice = get_computer_choice()
                    if is_draw(player_choice, computer_choice):
                      print("It's a draw, both players picked %s: " % player_choice)
                    else:
                      print("Computer picked: %s" % computer_choice)
                      print("Player picked: %s" % player_choice)
                      print_winner(player_choice, computer_choice)


                    if __name__ == "__main__":
                      play_game


def Player_stats(player):
  hp = 50
  Def = 20
  Attack = 15
  print("Hp: " + str(hp) + "Def: " + str(Def) + "Ak: " + str(Attack))
color_checker = [
  "Red", "orange", "yellow", "green", "blue", "indigo", "violet" ,"Black", "white" , "pink"
  ]
def color_list(): 
  print("Red, orange, yellow, green, blue, indigo, violet ,Black, white,pink.")
def green(color):
   x = 0
   while color not in color_checker:
    print("Try again")
    color = input("Different color.")
    x += 1
    if x == 10:
      return color
  
  
#The start

name = input("Welcome, To begin. Please enter a Name. Let be known you will use this name all throught the game. ")

yesorno = input(name + ", Are you sure this is the name you want? (Can't go back after you decide!)")

if "yes" in yesorno.lower():
 color_list()
 color = input("Good, Now. What color? (Please pick from the Rainbow. Black and white are a choice too.)")
 green(color)
 
 print(color + (". Thank you for your time. Lets. Begin."))
 
 print("You wake awaken deep in forest agaisnt a tree. It seems you've forgotten everything but you name. Your name is " + name + ". You look around a bit to notice large claw marks agaisnt the trees and dirt.")
 
 choice = input("What do you do? (run away, Look around more, investigate)")
 if "run away" is choice:
  print("You enter fight or filght. But at the sight of the claw marks. You Book it in a random direction")
 
 if "Look around more" is choice:
  print("You take a better look at your surroundings. You find that on the ground are dead bodies in armor. The ground is burnt from a fire of sorts.")
  choice2 = input("What do you do?")
 if "investigate" is choice:
   print("You take a look at the marks. You have no idea what they are. You sit staring at them wondering what they are. You so focus on trying to firgure out what they are you don't notices what's behind you until you feel a cut go down the middle of your body.")
   deathinsta()
   