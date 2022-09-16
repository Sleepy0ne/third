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
    if "Yes" in retry.lower():
      return(choice)
    if "No" in retry.lower():
      print("Wh-What? You weren't suppose to just give up!")
      print("Please, Try again!")
      retry2 =input("(Yes),(Yes),(No)")
      if "Yes" in retry2.lower():
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
        if "YES" in SPIN.lower():
          
          print("Congrats. You now are holding a spinning Finget spinner.")
          time.sleep(2)
          
          print("You wanna do it again?")
          Spin2 = input("(Yes or No)")
          if "Yes" in Spin2.lower():
            
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


def Player_stats():
  hp = 50
  Def = 20
  Attack = 15
  print("Hp:" + str(hp) + " Def:" + str(Def) + " Ak:" + str(Attack))
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
import time
name = input("Welcome, To begin. Please enter a Name. Let be known you will use this name all throught the game. ")

yesorno = input(name + ", Are you sure this is the name you want? (Can't go back after you decide!)")
if "no" in yesorno.lower():
  print("Try again")
  time.sleep(2)
  name3 = input("Name?")
  color_list()
  color = input("Good, Now. What color? (Please pick from the Rainbow. Black and white are a choice too.)")
  green(color)
 
  print(color + (". Thank you for your time. Lets. Begin."))
  time.sleep(4)
  print("You wake awaken deep in forest agaisnt a tree. It seems you've forgotten everything but you name. Your name is " + name3 + ". You look around a bit to notice large claw marks agaisnt the trees and dirt.")
 
  choice = input("What do you do? (run away, Look around more, investigate)")
  time.sleep(3)
  if "run away" == choice.lower():
    
    print("You enter fight or filght.") 
    time.sleep(2)
    
    print("But at the sight of the claw marks. You Book it in a random direction.")
    time.sleep(4)
    
    print("You hear something giving chase from behind!") 
    time.sleep(3)
    
    print("Your start running faster! Watch out!")
    time.sleep(2)
    
    print("(type whatever letter shows up!)")
    
    import threading
    
    import time

    def tt(name, num):
        while True:
          num += 0.5
          print('thread ' + str(name) + ' at time ' + str(num))
          time.sleep(0.5)


    for i in range(3):
      t=threading.Thread(target=tt, args=(i, 0))
      setDaemon()
      t.start()
      t.join(timeout=1)

    
    import random
    time.sleep(2)
    l = ["w", "a", "s", "d"]
    dodge=input(random.choice(l)) + ("\n ")
    
      
    if dodge is dodge == dodge:
      
      print("test")
    if dodge is not dodge == dodge:
      
      print("You try dodge out the wait but you fall trip.")
      time.sleep(3)
      
      print("Now, you turn over to see this beast. It looks to be a mix of serveal animals.")
      time.sleep(4)
      
      print("You crowd if fear as this beast swings down at you.")
      time.sleep(3)
      
      print("Everything..Goes...Dark..")
      time.sleep(3)
      
      deathinsta()
    
     

 
  if "Look around more" == choice:
    
    print("You take a better look at your surroundings. You find that on the ground are dead bodies in armor. The ground is burnt from a fire of sorts.")
    
    time.sleep(3)
    
    print("You hear as somethings gets near...")
    
    time.sleep(3)
    
    print("Your ready yourself for combat!")
    
    Player_stats()  
  
  if "investigate" == choice:
   
   print("You take a good look at the marks.") 
   time.sleep(3)
   
   print("You have no idea what they are.") 
   time.sleep(2)
   
   print("You sit puzzled.") 
   time.sleep(1)
   
   print("Your so focused you lost track on what going on around you. It's too late now. Your slashed from behind by something heavy.")
   time.sleep(5)
   
   print("You begin to bleed out as you fall to the ground.")
   time.sleep(3)
   
   print("You no longer can feel the lower half of your body... It starts getting...Dark.")
   time.sleep(5)
   deathinsta()
   
   
if "yes" in yesorno.lower():
 color_list()
 color = input("Good, Now. What color? (Please pick from the Rainbow. Black and white are a choice too.)")
 
 print(color + (". Thank you for your time. Lets. Begin."))
 time.sleep(4)
 print("You wake awaken deep in forest agaisnt a tree. It seems you've forgotten everything but you name. Your name is " + name + ". You look around a bit to notice large claw marks agaisnt the trees and dirt.")
 
 choice = input("What do you do? (run away, Look around more, investigate)")
 time.sleep(3)
 if "run away" == choice.lower():
  print("You enter fight or filght. But at the sight of the claw marks. You Book it in a random direction")
 
 if "Look around more" == choice.lower():
  
  print("You take a better look at your surroundings. You find that on the ground are dead bodies in armor. The ground is burnt from a fire of sorts.")
  
  time.sleep(3)
  
  print("You hear as somethings gets near...")
  
  time.sleep(3)
  
  print("Your ready yourself for combat!")
  
  Player_stats()
  
  FIGHT = input("(Slash: -15, Double tab: -35, Heavy Swing: -30.)")
  
  
  
 if "investigate" == choice.lower():
   print("You take a good look at the marks.") 
   time.sleep(3)
   
   print("You have no idea what they are.") 
   time.sleep(2)
   
   print("You sit puzzled.") 
   time.sleep(1)
   
   print("Your so focused you lost track on what going on around you. It's too late now. Your slashed from behind by something heavy.")
   time.sleep(5)
   
   print("You begin to bleed out as you fall to the ground.")
   time.sleep(3)
   
   print("You no longer can feel the lower half of your body... It starts getting...Dark.")
   time.sleep(5)
   deathinsta()
   