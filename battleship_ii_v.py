from random import randint, choice
from time import sleep
    
#Battleship class
class Battleship:

  def __init__(self):
    self.coords = []
    self.hit_points = 4

  #Set coordinates for battleship upon creation
  def set_coords(self,*coords):
    self.coords.extend(coords)
    
  #Check if battleship is hit
  def isHit(self, guess_row, guess_col):
    hit = False
    for i in range(4):
      if int(guess_row) == self.__coords[i][0] \
         and int(guess_col) == self.__coords[i][1]:
        hit = True
    return hit

  #Get hit points for battleship every time it is hit
  def get_hit_points(self):
    return self.hit_points

  def decrease_hit_points(self):
    self.hit_points = self.hit_points - 1

  #Check to see if ship is sunken every time it is hit
  def isSunken(self):
    if self.hit_points == 0:
      return True
    else:
      return False

#These two functions set location of battleship
#A number from 0 to the length/width of the board is chosen at random in both
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)
    
#This function prints the board
def print_board(board):
  for row in board:
    print(" ".join(row))

#Difficulty decorator
def difficulty_mode(diff):
  memo={}
  def difficulty_decorator(f):
    def function_wrapper(board):
      if diff == "E" or diff == "e":
        #Easy CPU will just guess randomly, even outside board
        res = f(board)
        return [choice([res[0]-1,res[0],res[0]+1]),
                choice([res[1]-1,res[1],res[1]+1])]
      elif diff == "I" or diff == "i":
        #Intermediate CPU will guess randomly, but not outside board.
        #It will also not guess squares already revealed to have battleships
        res = f(board)
        while board[res[0]][res[1]] == 'P' or board[res[0]][res[1]] == 'C' or res[0] in memo and memo[res[0]] == res[1]:
          res = f(board)
        if res[0] not in memo:
          memo[res[0]] = res[1]        
        return res
      else:
        #Hard CPU has a copy of player's battleship coordinates and will
        #guess right every time
        o = battleships_player[randint(0, len(battleships_player)-1)]
        while board[res[0]][res[1]] == 'P' or board[res[0]][res[1]] == 'C':
          res = choice(o.coords)
        return res
      return memo[res[0]]
    return function_wrapper
  return difficulty_decorator

#Battleship 2.0 logo, with 2.5 title
with open("battleship_ii.txt") as logo:
  for line in logo:
    print(line, end=' ')
print("Battleship v2.5")
  
#Show instructions to user
docstring = """
INSTRUCTIONS

This game is played on a board of the users' choosing of
at least 8 (but not 9) squares.  The battleships are 4x1
or 1x4 entities that are randomly arranged across the board.
Neither player will know where their battleships are located.
Players must guess correctly the coordinates of
all four parts of an enemy battleship to sink it.
Coordinates range from 0 to however many rows or
columns there are minus one.  The first player to
sink all of the other player's battleships wins.

The users may choose to play a one- or two-player game.
In the one-player game, one user will face a CPU opponent,
and in the two-player game, two users will face each other
trying to sink the other's battleships first. This updated
version has three difficulty settings for the CPU in the one-
player game:  easy, intermediate and hard.  The easy CPU
will guess randomly, even outside the board, the intermediate
CPU will guess inside the board, and never on a square already
guessed; and the hard CPU already knows where the player's
battleships are.
"""
print(docstring)

#Start main loop
while True:
  #initialize board
  board = []
  print("\nPlease enter the size of the board desired (must be at least 4 sqaures one way).")
  rows = input("Please enter number of rows: ")
  cols = input("Please enter number of columns: ")
  #Do checking to see if user entered an invalid answer:
  while rows.isdigit() == False or cols.isdigit() == False \
        or int(rows)*int(cols) < 8 or int(rows)*int(cols) == 9:
    if rows.isdigit() == False or cols.isdigit() == False:
      rows = input("Please enter a numeral for rows: ")
      cols = input("Please enter a numeral for columns: ")
    elif int(rows)*int(cols) or int(rows)*int(cols) == 9:
      print("Your board is too small.")
      rows = input("Please enter number of rows: ")
      cols = input("Please enter number of columns: ")

  #Create board
  for x in range(int(rows)):
    board.append(["O"] * int(cols))

  #Set the table for available coordinates for all ships
  available_coords = []
  for i in range(int(rows)):
    for j in range(int(cols)):
      available_coords.append([i,j])
    
  #Prompt user(s) to enter number of players
  print("\nOne player or two players?")

  #Check if user enters anything other than 1 or 2 or ONE or TWO
  player_number = input("Enter '1', '2' 'one' or 'two': ")
  while player_number.isdigit() == False or int(player_number) > 2 \
        or int(player_number) < 0:
    player_number = input("Please enter one or two players: ")
    
  if player_number == "1" or player_number == "ONE" or player_number == "one":
    #Launch one-player game if user enters '1'
    print("\nOne player!")

    #Ask user how many battleships he or she wants on board
    #If board is minimum size, skip this step
    if int(rows)*int(cols) == 8:
      print("We each have one battleship.")
      numOfBattleships = 1
    else:
      print("\nHow many battleships do you want each player to have?")
      numOfBattleships = input("Enter a numeral 1-{0:d}: ".format((int(rows)*int(cols))//8))

      #Do checking to see if user entered an invalid answer:
      while numOfBattleships.isdigit() == False or int(numOfBattleships) < 1 \
            or int(numOfBattleships) > (int(cols)*int(rows))//8:
        numOfBattleships = input("Enter a numeral 1-{0:d}: ".format((int(rows)*int(cols))//8))

    #Ask user for difficulty mode for one-player game
    print("\nHow difficult do you want the CPU to be?")
    difficulty = input("E for easy, I for intermediate, H for hard: ")

    #Check if user entered valid input for difficulty
    while difficulty != "e" and difficulty != "E" and difficulty != "I" \
          and difficulty != "i" and difficulty != "H" and difficulty != "h":
      difficulty = input("Please enter E for easy, I for intermediate," \
                         + " or H for hard: ")
      
    #This function selects a random row AND column for computer to guess,
    #based on the computer's difficulty
    @difficulty_mode(difficulty)
    def random_row_and_col(board):
      return [randint(0, len(board) - 1), randint(0, len(board[0]) - 1)]

    #Initialize battleship lists
    battleships_player = []
    battleships_cpu = []

    #Create battleships for player and CPU:
    z=0
    while z <= int(numOfBattleships)-1:
      c = random_row(board) #Random row
      d = random_col(board) #Random col
      #Player
      if randint(1,10) >= 1 and randint(1,10) < 3:
        if [c,d] in available_coords \
           and [c+1,d] in available_coords\
           and [c+2,d] in available_coords\
           and [c+3,d] in available_coords:
          battleships_player.append(Battleship())
          battleships_player[z].set_coords([c,d],[c+1,d],[c+2,d],[c+3,d])
          for k in range(4):
            available_coords.remove([c+k,d])
          z+=1
              
      elif randint(1,10) >= 3 and randint(1,10) < 6:
        if [c,d] in available_coords \
          and [c,d+1] in available_coords\
          and [c,d+2] in available_coords\
          and [c,d+3] in available_coords:
          battleships_player.append(Battleship())
          battleships_player[z].set_coords([c,d],[c,d+1],[c,d+2],[c,d+3])
          for k in range(4):
            available_coords.remove([c,d+k])
          z+=1

      elif randint(1,10) >= 6 and randint(1,10) < 8:
        if [c,d] in available_coords \
          and [c-1,d] in available_coords\
          and [c-2,d] in available_coords\
          and [c-3,d] in available_coords:
          battleships_player.append(Battleship())
          battleships_player[z].set_coords([c,d],[c-1,d],[c-2,d],[c-3,d])
          for k in range(4):
            available_coords.remove([c-k,d])
          z+=1
          
      else:
        if [c,d] in available_coords \
          and [c,d-1] in available_coords\
          and [c,d-2] in available_coords\
          and [c,d-3] in available_coords:
          battleships_player.append(Battleship())
          battleships_player[z].set_coords([c,d],[c,d-1],[c,d-2],[c,d-3])
          for k in range(4):
            available_coords.remove([c,d-k])
          z+=1      

    z=0
    while z <= int(numOfBattleships)-1:
      c = random_row(board)
      d = random_col(board)
      #CPU
      if randint(1,10) >= 1 and randint(1,10) < 3:
        if [c,d] in available_coords \
           and [c+1,d] in available_coords\
           and [c+2,d] in available_coords\
           and [c+3,d] in available_coords:
          battleships_cpu.append(Battleship())
          battleships_cpu[z].set_coords([c,d],[c+1,d],[c+2,d],[c+3,d])
          for k in range(4):
            available_coords.remove([c+k,d])
          z+=1
              
      elif randint(1,10) >= 3 and randint(1,10) < 6:
        if [c,d] in available_coords \
          and [c,d+1] in available_coords\
          and [c,d+2] in available_coords\
          and [c,d+3] in available_coords:
          battleships_cpu.append(Battleship())
          battleships_cpu[z].set_coords([c,d],[c,d+1],[c,d+2],[c,d+3])
          for k in range(4):
            available_coords.remove([c,d+k])
          z+=1

      elif randint(1,10) >= 6 and randint(1,10) < 8:
        if [c,d] in available_coords \
          and [c-1,d] in available_coords\
          and [c-2,d] in available_coords\
          and [c-3,d] in available_coords:
          battleships_cpu.append(Battleship())
          battleships_cpu[z].set_coords([c,d],[c-1,d],[c-2,d],[c-3,d])
          for k in range(4):
            available_coords.remove([c-k,d])
          z+=1
          
      else:
        if [c,d] in available_coords \
          and [c,d-1] in available_coords\
          and [c,d-2] in available_coords\
          and [c,d-3] in available_coords:
          battleships_cpu.append(Battleship())
          battleships_cpu[z].set_coords([c,d],[c,d-1],[c,d-2],[c,d-3])
          for k in range(4):
            available_coords.remove([c,d-k])
          z+=1      

    #Start game loop
    while len(battleships_player) != 0 and len(battleships_cpu) != 0:
      
      # Prompt player to enter coordinates
      sleep(2)
      print("\nYour turn!")
      guess_row = input("Guess Row: ")
      guess_col = input("Guess Col: ")

      #Check if player entered not a number.  Prompt them to enter row
      #and column again if so.
      while guess_row.isdigit() == False or guess_col.isdigit() == False:
        guess_row = input("Please enter a number for row: ")
        guess_col = input("Please enter a number for column: ")
        
      #If player enters valid row and column, begin checking row and column
      for b in battleships_cpu:
        if [int(guess_row),int(guess_col)] in b.coords:
            if(board[int(guess_row)][int(guess_col)] == 'C'):
              print ("Battleship already hit there.")#See if player already
                                                     #guessed that square
              break
            else:
              #Player hits a battleship, so hit points for battleship go down
              print ("\nYou hit a battleship!")
              #put an 'C' in square to indicate a hit
              board[int(guess_row)][int(guess_col)] = 'C'
              #Decrease hit points for battleship
              b.decrease_hit_points()
              print_board(board)
              if b.isSunken() == True:
                #Check if battleship lost all hit points.
                #If so, it is sunken.
                print("My battleship is sunken!")
                battleships_cpu.remove(b)
              break
      else:
        #Alternative cases for player's guess
            
        #Player guesses outside of board
        if (int(guess_row) < 0 or int(guess_row) > int(rows)-1) \
          or (int(guess_col) < 0 or int(guess_col) > int(cols)-1):
            print ("\nOops, that's not even in the ocean.")
            print_board(board)
          
        else:
          for a in battleships_player:
            #Player guesses own square
            if [int(guess_row),int(guess_col)] in a.coords:
              if(board[int(guess_row)][int(guess_col)] == 'P'):
                #Battleship already hit
                print ("Battleship already hit there.")
                break
              else:
                print ("\nOuch!  You hit your own battleship.")
                #Put a 'P' where player is hit
                board[int(guess_row)][int(guess_col)] = 'P'
                a.decrease_hit_points()
                print_board(board)
                if a.isSunken() == True:
                  #Check if battleship lost all hit points.
                  #If so, it is sunken.
                  print("I sank your battleship!")
                  battleships_player.remove(a)
                break
          else:
            print("No battleships there.")

      #player wins if he hits all battleships    
      if len(battleships_cpu) == 0:
        sleep(2)
        print("\nYou sank all the battleships!  Congratulations!")
        break
      elif len(battleships_player) == 0:
        sleep(2)
        print("\nI sank all your battleships!  You lose!")
        break
            
      #CPU's turn to attack
      sleep(2)
      print("\nMy turn!")
      sleep(2)
      
      #CPU guesses row and column
      cpu_guess_row_and_col = random_row_and_col(board)
      
      print("My guess is {0:d} {1:d}".format(cpu_guess_row_and_col[0],\
                                             cpu_guess_row_and_col[1]))
      sleep(2)

      #Check if CPU hit a ship.
      for a in battleships_player:
        if cpu_guess_row_and_col in a.coords:
          if(board[cpu_guess_row_and_col[0]][cpu_guess_row_and_col[1]] == 'P'):
            #See if CPU already guessed that square
            print ("Battleship already hit there.")
            break
            
          #CPU hits player
          else:
            print ("\nI hit a battleship!")
            #put a 'P' in square to indicate a hit
            board[cpu_guess_row_and_col[0]][cpu_guess_row_and_col[1]] = 'P'
            #and decrease hit points on battleship
            a.decrease_hit_points()
            print_board(board)
            if a.isSunken() == True:
              #Check if battleship lost all hit points.
              print("I sank your battleship!")
              battleships_player.remove(a)
            break

      else:
        #Alternative cases for CPU's guess
            
        #CPU guesses outside of board
        if (cpu_guess_row_and_col[0] < 0 or cpu_guess_row_and_col[0] > int(rows)-1) \
          or (cpu_guess_row_and_col[1] < 0 or cpu_guess_row_and_col[1] > int(cols)-1):
            print ("\nOops, I fired a shot outside the ocean.")
            print_board(board)
            
        else:
          #CPU guesses own square
          for b in battleships_cpu:
              if cpu_guess_row_and_col in b.coords:
                if(board[cpu_guess_row_and_col[0]][cpu_guess_row_and_col[1]] == 'C'):
                  #Battleship already hit
                  print ("Battleship already hit there.")
                  break
                else:
                  print("\nOuch!  Hit my own battleship.")
                  #Put a 'C' in the square to indicate a hit
                  board[cpu_guess_row_and_col[0]][cpu_guess_row_and_col[1]] = 'C'
                  b.decrease_hit_points()
                  print_board(board)
                  #Decrease CPU's battleship hit points
                  if b.isSunken() == True:
                    #Check if battleship lost all hit points.
                    print("My battleship is sunken!")
                    battleships_cpu.remove(b)
                  break
          else:
            print("No battleships there.")
            
      #player loses if CPU hits all battleships
      if len(battleships_player) == 0:
        sleep(2)
        print("\nI sank all your battleships!  You lose!")
        break
      elif len(battleships_cpu) == 0:
        sleep(2)
        print("\nYou sank all the battleships!  Congratulations!")
        break
            
  elif player_number == "2" or player_number == "TWO" or player_number == "two":
    #Launch two-player game if user enters '2'
    print("\nTwo players!")

    #Ask user how many battleships he or she wants on board
    #If board is minimum size, skip this step
    if int(rows)*int(cols) == 8:
      print("You each have one battleship.")
      numOfBattleships = 1
    else:
      print("\nHow many battleships do you want each player to have?")
      numOfBattleships = input("Enter a numeral 1-{0:d}: ".format((int(rows)*int(cols))//8))

      #Do checking to see if user entered an invalid answer:
      while numOfBattleships.isdigit() == False or int(numOfBattleships) < 1 \
            or int(numOfBattleships) > (int(cols)*int(rows))//8:
        numOfBattleships = input("Enter a numeral 1-{0:d}: ".format((int(rows)*int(cols))//8))
    #Create battleships for players:
    battleships_one = []
    battleships_two = []
      
    #Place battleships on board
    z=0
    while z <= int(numOfBattleships)-1:
      c = random_row(board) #Random row
      d = random_col(board) #Random col
      #Player One
      if randint(1,10) >= 1 and randint(1,10) < 3:
        if [c,d] in available_coords \
           and [c+1,d] in available_coords\
           and [c+2,d] in available_coords\
           and [c+3,d] in available_coords:
          battleships_one.append(Battleship())
          battleships_one[z].set_coords([c,d],[c+1,d],[c+2,d],[c+3,d])
          for k in range(4):
            available_coords.remove([c+k,d])
          z+=1
              
      elif randint(1,10) >= 3 and randint(1,10) < 6:
        if [c,d] in available_coords \
          and [c,d+1] in available_coords\
          and [c,d+2] in available_coords\
          and [c,d+3] in available_coords:
          battleships_one.append(Battleship())
          battleships_one[z].set_coords([c,d],[c,d+1],[c,d+2],[c,d+3])
          for k in range(4):
            available_coords.remove([c,d+k])
          z+=1

      elif randint(1,10) >= 6 and randint(1,10) < 8:
        if [c,d] in available_coords \
          and [c-1,d] in available_coords\
          and [c-2,d] in available_coords\
          and [c-3,d] in available_coords:
          battleships_one.append(Battleship())
          battleships_one[z].set_coords([c,d],[c-1,d],[c-2,d],[c-3,d])
          for k in range(4):
            available_coords.remove([c-k,d])
          z+=1
          
      else:
        if [c,d] in available_coords \
          and [c,d-1] in available_coords\
          and [c,d-2] in available_coords\
          and [c,d-3] in available_coords:
          battleships_one.append(Battleship())
          battleships_one[z].set_coords([c,d],[c,d-1],[c,d-2],[c,d-3])
          for k in range(4):
            available_coords.remove([c,d-k])
          z+=1
            
    z=0
    while z <= int(numOfBattleships)-1:
      c = random_row(board) 
      d = random_col(board)
      #Player two
      if randint(1,10) >= 1 and randint(1,10) < 3:
        if [c,d] in available_coords \
           and [c+1,d] in available_coords\
           and [c+2,d] in available_coords\
           and [c+3,d] in available_coords:
          battleships_two.append(Battleship())
          battleships_two[z].set_coords([c,d],[c+1,d],[c+2,d],[c+3,d])
          for k in range(4):
            available_coords.remove([c+k,d])
          z+=1
              
      elif randint(1,10) >= 3 and randint(1,10) < 6:
        if [c,d] in available_coords \
          and [c,d+1] in available_coords\
          and [c,d+2] in available_coords\
          and [c,d+3] in available_coords:
          battleships_two.append(Battleship())
          battleships_two[z].set_coords([c,d],[c,d+1],[c,d+2],[c,d+3])
          for k in range(4):
            available_coords.remove([c,d+k])
          z+=1

      elif randint(1,10) >= 6 and randint(1,10) < 8:
        if [c,d] in available_coords \
          and [c-1,d] in available_coords\
          and [c-2,d] in available_coords\
          and [c-3,d] in available_coords:
          battleships_two.append(Battleship())
          battleships_two[z].set_coords([c,d],[c-1,d],[c-2,d],[c-3,d])
          for k in range(4):
            available_coords.remove([c-k,d])
          z+=1
          
      else:
        if [c,d] in available_coords \
          and [c,d-1] in available_coords\
          and [c,d-2] in available_coords\
          and [c,d-3] in available_coords:
          battleships_two.append(Battleship())
          battleships_two[z].set_coords([c,d],[c,d-1],[c,d-2],[c,d-3])
          for k in range(4):
            available_coords.remove([c,d-k])
          z+=1

    #Start game loop
    while len(battleships_one) != 0 and len(battleships_two) != 0:
      
      #Player one's turn
      # Prompt player one to enter coordinates
      sleep(2)
      print("\nPlayer One's turn!")
      guess_row = input("Guess Row: ")
      guess_col = input("Guess Col: ")

      #Check if player entered not a number.  Prompt them to enter row
      #and column again if so.
      while guess_row.isdigit() == False or guess_col.isdigit() == False:
        guess_row = input("Please enter a number for row: ")
        guess_col = input("Please enter a number for column: ")
        
      #Check if player one hit one of player two's battleships
      for b in battleships_two:
        if [int(guess_row),int(guess_col)] in b.coords:
            if(board[int(guess_row)][int(guess_col)] == 'T'):
              print ("Battleship already hit there.")#See if player already
                                                     #guessed that square
              break
            else:
              #Player one hits a battleship, so hit points for battleship go down
              print ("\nPlayer One hit a battleship!")
              #put a 'T' in square to indicate a hit
              board[int(guess_row)][int(guess_col)] = 'T'
              #Decrease hit points for battleship
              b.decrease_hit_points()
              print_board(board)
              if b.isSunken() == True:
                #Check if battleship lost all hit points.
                #If so, it is sunken.
                print("Player Two lost a battleship!")
                battleships_two.remove(b)
              break
      else:
        #Alternative cases for player one's guess
            
        #Player one guesses outside of board
        if (int(guess_row) < 0 or int(guess_row) > int(rows)-1) \
          or (int(guess_col) < 0 or int(guess_col) > int(cols)-1):
            print ("\nOops, that's not even in the ocean.")
            print_board(board)
          
        else:
          for a in battleships_one:
            #Player one guesses own square
            if [int(guess_row),int(guess_col)] in a.coords:
              if(board[int(guess_row)][int(guess_col)] == 'N'):
                #Battleship already hit
                print ("Battleship already hit there.")
                break
              else:
                print ("\nOuch!  Player One hit own battleship.")
                #Put a 'P' where player is hit
                board[int(guess_row)][int(guess_col)] = 'N'
                a.decrease_hit_points()
                print_board(board)
                if a.isSunken() == True:
                  #Check if battleship lost all hit points.
                  #If so, it is sunken.
                  print("Player One lost a battleship!")
                  battleships_one.remove(a)
                break
          else:
            print("No battleships there.")

      #Player one wins if all player two's battleships are sunken    
      if len(battleships_two) == 0:
        sleep(2)
        print("\nPlayer One wins!")
        break
      elif len(battleships_one) == 0:
        sleep(2)
        print("\nPlayer Two wins!")
        break
            
      #Player two's turn
      sleep(2)
      # Prompt player two to enter coordinates
      print("\nPlayer Two's turn!")
      guess_row = input("Guess Row: ")
      guess_col = input("Guess Col: ")

      #Check if player entered not a number.  Prompt them to enter row
      #and column again if so.
      while guess_row.isdigit() == False or guess_col.isdigit() == False:
        guess_row = input("Please enter a number for row: ")
        guess_col = input("Please enter a number for column: ")

      #Check if player two hit a battleship.
      for a in battleships_one:
        if [int(guess_row),int(guess_col)] in a.coords:
          if(board[int(guess_row)][int(guess_col)] == 'N'):
            #See if player already guessed that square
            print ("Battleship already hit there.")
            break
            
          #Player one is hit
          else:
            print ("\nPlayer Two hit a battleship!")
            #put a 'P' in square to indicate a hit
            board[int(guess_row)][int(guess_col)] = 'N'
            #decrease hit points on battleship
            a.decrease_hit_points()
            print_board(board)
            if a.isSunken() == True:
              #Check if battleship lost all hit points.
              print("Player One lost a battleship!")
              battleships_one.remove(a)
            break

      else:
        #Alternative cases for player two's guess
            
        #Player two guesses outside of board
        if (int(guess_row) < 0 or int(guess_row) > int(rows)-1) \
          or (int(guess_col) < 0 or int(guess_col) > int(cols)-1):
            print ("\nOops, that's not even in the ocean.")
            print_board(board)
            
        else:
          #Player two guesses own square
          for b in battleships_two:
              if [int(guess_row),int(guess_col)] in b.coords:
                if(board[int(guess_row)][int(guess_col)] == 'T'):
                  #Battleship already hit
                  print ("Battleship already hit there.")
                  break
                else:
                  print("\nOuch!  Player Two hit own battleship.")
                  #Put a 'C' in the square to indicate a hit
                  board[int(guess_row)][int(guess_col)] = 'T'
                  b.decrease_hit_points()
                  print_board(board)
                  #Decrease battleship hit points
                  if b.isSunken() == True:
                    #Check if battleship lost all hit points.
                    print("Player Two lost a battleship!")
                    battleships_two.remove(b)
                  break
          else:
            print("No battleships there.")
            
      #player loses if CPU hits all battleships
      if len(battleships_one) == 0:
        sleep(2)
        print("\nPlayer Two wins!")
        break
      elif len(battleships_two) == 0:
        sleep(2)
        print("\nPlayer One wins!")
        break
          
  play_again = input("Play again? Enter Y for yes or N for no: ")
  if play_again == 'n' or play_again == 'N':
    break
  #self-explanatory

