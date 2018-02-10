from random import randint

#This function prints the board
def print_board(board):
  for row in board:
    print(" ".join(row))

#These two functions set location of battleship
#A number from 0 to 4 is chosen at random in both
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#First, the logo...
print("^"*10 + " "*7 + "^" + " "*6 + "^"*10 + " " + "^"*10 + " " + "^"
      + " "*10 + "^"*10 + " " + "^"*10 + " " + "^" + " "*8 + "^" + " "
      + "^"*10 + " " + "^"*10)
print("^" + " "*9 + "^" + " "*5 + "^" + " " + "^" + " "*9 + "^"
      + " "*10 + "^" + " "*6 + "^" + " "*10 + "^" + " "*10 + "^" + " "*10
      + "^" + " "*8 + "^" + " "*5 + "^" + " "*6 + "^" + " "*8 + "^")
print("*" + " "*9 + "*" + " "*5 + "*" + " " + "*" + " "*9 + "*"
      + " "*10 + "*" + " "*6 + "*" + " "*10 + "*" + " "*10 + "*" + " "*10
      + "*" + " "*8 + "*" + " "*5 + "*" + " "*6 + "*" + " "*8 + "*")
print("*" + " "*8 + "*" + " "*5 + "*" + " "*3 + "*" + " "*8 + "*"
      + " "*10 + "*" + " "*6 + "*" + " "*10 + "*" + " "*10 + "*" + " "*10
      + "*" + " "*8 + "*" + " "*5 + "*" + " "*6 + "*" + " "*8 + "*")
print("@"*9 + " "*6 + "@" + " "*3 + "@" + " "*8 + "@"
      + " "*10 + "@" + " "*6 + "@" + " "*10 + "@"*10 + " "
      + "@"*10 + " " + "@"*10 + " "*5 + "@" + " "*6 + "@"*10)
print("@" + " "*8 + "@" + " "*5 + "@"*5 + " "*8 + "@" + " "*10 + "@"
      + " "*6 + "@" + " "*10 + "@" + " "*19 + "@" + " " + "@" + " "*8
      + "@" + " "*5 + "@" + " "*6 + "@")
print("#" + " "*9 + "#" + " "*4 + "#" + " "*3 + "#" + " "*8 + "#"
      + " "*10 + "#" + " "*6 + "#" + " "*10 + "#" + " "*19 + "#" + " "
      + "#" + " "*8 + "#" + " "*5 + "#" + " "*6 + "#")
print("#" + " "*9 + "#" + " "*4 + "#" + " "*3 + "#" + " "*8 + "#"
      + " "*10 + "#" + " "*6 + "#" + " "*10 + "#" + " "*19 + "#" + " "
      + "#" + " "*8 + "#" + " "*5 + "#" + " "*6 + "#")
print("&" + " "*8 + "&" + " "*5 + "&" + " "*3 + "&" + " "*8 + "&"
      + " "*10 + "&" + " "*6 + "&" + " "*10 + "&" + " "*19 + "&" + " "
      + "&" + " "*8 + "&" + " "*5 + "&" + " "*6 + "&")
print("&"*9 + " "*6 + "&" + " "*3 + "&" + " "*8 + "&"
      + " "*10 + "&" + " "*6 + "&"*10 + " " + "&"*10 + " " + "&"*10 + " "
      + "&" + " "*8 + "&" + " " + "&"*10 + " " + "&")
print("\n")
print("Welcome to Battleship!")
print("\n")
  
play_again = "y"
while (play_again == "y") or (play_again == "Y"):
  #initialize board
  board = []
  for x in range(5):
    board.append(["O"] * 5)

  #Print out the board
  print_board(board)
    
  #initialize hit count for one player game
  hit_count = 0
    
  #Prompt user(s) to enter number of players
  print("\n")
  print("One player or two players?")

  #Check if player enters anything other than 1 or 2 or ONE or TWO
  player_number = input("Enter '1', '2' 'one' or 'two': ")
  while player_number != "1" and player_number != "2" \
        and player_number != "one" and player_number != "ONE" \
        and player_number != "two" and player_number != "TWO":
    player_number = input("Please enter one or two players: ")
    
  if player_number == "1" or player_number == "ONE" or player_number == "one":
    #Launch one-player game if player enters '1'
    print("\n")
    print("One player!")

    #Ask player how many battleships they want on 5x5 board.
    #Only 5x5 board used for simplicity.
    print("How many battleships do you want on the board?")
    numOfBattleships = input("Enter a numeral 1-12: ")

    #Do checking to see if player entered an invalid answer:
    while numOfBattleships.isdigit() == False or int(numOfBattleships) < 1 \
          or int(numOfBattleships) > 12:
      numOfBattleships = input("Enter a numeral 1-12: ")

    #Ask player how many chances to guess where battleships are they want.
    print("How many chances to guess do you want?")
    numOfChances = input("Enter a numeral " + str(int(numOfBattleships) + 1) + "-25: ")

    #Do checking again to see if player entered an invalid answer:
    while numOfChances.isdigit() == False \
    or int(numOfChances) < (int(numOfBattleships)+1) \
          or int(numOfChances) > 25:
      numOfChances = input("Enter a numeral " + str(int(numOfBattleships) + 1) + "-25: ")
    
    #Create battleships and set rows and columns
    ship_rows = []
    ship_cols = []

    #Fill in coordinates for battleships, being careful not to put same
    #coordinates for two battleships
    for index in range(int(numOfBattleships)):
      if ship_rows.count(index) < 1 and ship_cols.count(index) < 1:
        ship_rows.append(random_row(board)) 
        ship_cols.append(random_col(board))  
            
    # Prompt player to enter coordinates
    print("\n")
    print("You have " + numOfChances + " guesses as to where my " + numOfBattleships + " battleships are.")
    print("Enter rows and columns guesses from numbers 0 to 4.")
    for turn in range(int(numOfChances)):
      print("\n")
      # Print (turn + 1) here!  This counts number of turns spent.
      print("Turn", turn + 1)
      #Prompt player for row and column guess
      guess_row = input("Guess Row: ")
      guess_col = input("Guess Col: ")

      #Check if player entered not a number.  Prompt them to enter row
      #and column again if so.
      while guess_row.isdigit() == False or guess_col.isdigit() == False:
        guess_row = input("Please enter a number 0 to 4 for row: ")
        guess_col = input("Please enter a number 0 to 4 for column: ")
      print("\n")
      #If player enters valid row and column, begin checking row and column
      if int(guess_row) in ship_rows and int(guess_col) in ship_cols:
        if(board[int(guess_row)][int(guess_col)] == "H") or \
          (board[int(guess_row)][int(guess_col)] == "X"):
          print("\n")
          print ("You guessed that one already.")#See if player already
                                                 #guessed that square
          if turn == int(numOfChances)-1:#Check if player runs out of turns
            print("\n")
            print ("Game Over")#Game is over if player runs out of turns
            break
        else:
          print("\n")
          print ("You hit a battleship!")
          board[int(guess_row)][int(guess_col)] = "H"
          #put an 'H' in square to indicate a hit
          hit_count += 1
          print_board(board)
          if hit_count == int(numOfBattleships):
            print("\n")
            print("You sank all the battleships!  Congratulations!")
            #player wins if he hits all battleships
            break
          elif turn == int(numOfChances)-1:
            print("\n")
            print("Game Over")
            break
      elif (int(guess_row) < 0 or int(guess_row) > 4) or (int(guess_col) < 0 or int(guess_col) > 4):
          print("\n")
          print ("Oops, that's not even in the ocean.")
          print_board(board)#Player guesses outside of board
          if turn == int(numOfChances)-1:
            print("\n")
            print("Game Over")
            break
      elif(board[int(guess_row)][int(guess_col)] == "X"):
          print("\n")
          print ("Player already guessed there.")
          print_board(board)#Player guesses same square
          if turn == int(numOfChances)-1:
            print("\n")
            print("Game Over")
            break
      else:
          print("\n")
          print ("No battleships there.")
          board[int(guess_row)][int(guess_col)] = "X"
          print_board(board)#Player misses
          if turn == int(numOfChances)-1:
            print("\n")
            print("Game Over")
            break
  elif player_number == "2" or player_number == "TWO" or player_number == "two":
    #Launch two-player game if user enters '2'
    print("\n")
    print("Two players!")

    #Ask each player how many battleships they want on the board
    #(Limit 6)
    print("How many battleships do you want for both players?")
    battleshipsOne = input("Enter 1-6: ")

    #Do checking if players entered something other than 1-6
    while battleshipsOne.isdigit() == False \
    or ((int(battleshipsOne) < 1 or int(battleshipsOne) > 6)):
      battleshipsOne = input("Please enter digit 1-6: ")

    battleshipsTwo = int(battleshipsOne) 

    #Create battleships for both players and initialize rows and columns
    ship_rows_one = []
    ship_rows_two = []
    ship_cols_one = []
    ship_cols_two = []

    #Set coordinates for battleships for both players, being careful not
    #to give two battleships the same coordinates
    for index in range(battleshipsTwo):
      #Let each row and column appear in each list at least once (< 2)
      if ship_rows_one.count(index) < 2 and ship_rows_two.count(index) < 2 \
         and ship_cols_one.count(index) < 2 and ship_cols_two.count(index) < 2:
          ship_rows_one.append(random_row(board))
          ship_rows_two.append(random_row(board))
          ship_cols_one.append(random_col(board))
          ship_cols_two.append(random_col(board))
    #Ask the players how many guesses they want to have each
    print("How many guesses does each player want to have?")
    numOfGuesses = input("Please enter a digit " + str(int(battleshipsOne) + 1)
                         + "-12: ")

    #Check if players entered a number less than number of battleships for
    #each player, more than 12 (covering the whole board), or not a number
    #at all
    while numOfGuesses.isdigit() == False \
          or int(numOfGuesses) < (int(battleshipsOne)+1) \
          or int(numOfGuesses) > 12:
      numOfGuesses = input("Please enter a digit "
                           + str(int(battleshipsOne) + 1) + "-12: ")
    
    #Explain rules to players and prompt for player one's guess
    print("\n")
    print("You each have " + str(numOfGuesses)
          + " chances to guess where the other player's battleships are.")
    print("Enter rows and columns guesses from numbers 0 to 4. \n")
    print_board(board)
    
    #Initialize hit counts
    player_one_hit_count = 0
    player_two_hit_count = 0
    
    #Start two-player game loop
    for turn in range(int(numOfGuesses)):
      print("\n")
      # Print (turn + 1) here!  This counts number of turns spent.
      print("Turn", turn + 1)
      #Prompt player one for row and column guess
      print("Player one: ")
      guess_row = input("Guess Row: ")
      guess_col = input("Guess Col: ")
      
      #Check if player one entered not a number
      #Have player one reenter rows and columns if they didn't
      while guess_row.isdigit() == False or guess_col.isdigit() == False:
        guess_row = input("Please enter a number 0 to 4 for row: ")
        guess_col = input("Please enter a number 0 to 4 for column: ")
      print("\n")
      #If player enters valid numbers for row and column, check where
             #guess is made
      if int(guess_row) in ship_rows_two and int(guess_col) in ship_cols_two:
        if(board[int(guess_row)][int(guess_col)] == "T"):
          #Player one guesses the same square
          print("\n")
          print ("That battleship already sunken.")
          print_board(board)
        else:#Player one hits player two's battleship
          print("\n")
          print ("Player one hit a battleship!")
          board[int(guess_row)][int(guess_col)] = "T"#put an 'T' in square to indicate a hit
          player_one_hit_count += 1
          print_board(board)
          if player_one_hit_count == int(battleshipsTwo):
            print("Player one wins!")
            break#Game over if player one sinks all of player two's ships
      else:
        if (int(guess_row) < 0 or int(guess_row) > 4) or (int(guess_col) < 0 or int(guess_col) > 4):
          print("\n")
          print ("Oops, that's not even in the ocean.")
          print_board(board)    #player guesses outside of board
        elif(board[int(guess_row)][int(guess_col)] == "X"):
          print("\n")
          print ("There are still no battleships there.")
          print_board(board)    #Player guesses same square
        elif(int(guess_row) in ship_rows_one) and (int(guess_col) in ship_cols_one):
          if(board[int(guess_row)][int(guess_col)] == "T"):
            print("\n")
            print("Player two guessed that square already.")
            print_board(board)#Player guesses same square
          else:
            print("\n")
            print("Ouch!  Player one hit their own boat!")#Put an 'N' on square
            board[int(guess_row)][int(guess_col)] = "N"#to indicate player one
            player_two_hit_count += 1#hit own battleship
            print_board(board)       #Reprint board if this happens
            if player_two_hit_count == int(battleshipsOne):
              print("\n")
              print("Player Two wins!")
              break#Game is over if player one sinks own battleships
        else:
          print("\n")
          print ("Player one misses!")
          board[int(guess_row)][int(guess_col)] = "X"
          print_board(board)
        
      #Prompt player two
      # Print (turn + 1) here!  This counts number of turns spent.
      print("\n")
      print("Turn", turn + 1)
      print("Player two: ")
      guess_row = input("Guess Row: ")
      guess_col = input("Guess Col: ")
      
      #Check if player two entered not a number. Prompt for row and column
      #again if so.
      while guess_row.isdigit() == False or guess_col.isdigit() == False:
        guess_row = input("Please enter a number 0 to 4 for row: ")
        guess_col = input("Please enter a number 0 to 4 for column: ")
        print("\n")
      #Check if player two hit player one's ship
      if int(guess_row) in ship_rows_one and int(guess_col) in ship_cols_one:
        if(board[int(guess_row)][int(guess_col)] == "N"):
          #Player two guesses the same square
          print("\n")
          print ("That battleship already sunken.")
          print_board(board)
        else:
          print("\n")
          print ("Player two hit a battleship!")#put an 'N' in square to indicate a hit
          board[int(guess_row)][int(guess_col)] = "N"
          player_two_hit_count += 1
          print_board(board)
          if player_two_hit_count == int(battleshipsOne):
            print("\n")
            print("Player two wins!")
            break#Game over if player one sinks all of player two's ships
      else:#Do same checking for where player two's guesses land
        if (int(guess_row) < 0 or int(guess_row) > 4) or (int(guess_col) < 0 or int(guess_col) > 4):
          print("\n")
          print ("Oops, that's not even in the ocean.")
          print_board(board)
        elif(board[int(guess_row)][int(guess_col)] == "X"):
          print("\n")
          print ("There are still no battleships there.")
          print_board(board)
        elif(int(guess_row) in ship_rows_two) and (int(guess_col) in ship_cols_two):
          if(board[int(guess_row)][int(guess_col)] == "T"):
            print("\n")
            print("Player one guessed that square already.")
            print_board(board)#Player guesses same square
          else:
            print("\n")
            print("Ouch!  Player two hit their own boat!")#Put a 'T' on square
            board[int(guess_row)][int(guess_col)] = "T"#to indicate player two
            player_one_hit_count += 1#hit own battleship
            print_board(board)
            if player_one_hit_count == int(battleshipsTwo):
              print("\n")
              print("Player one wins!")
              break#Game is over if player one sinks own battleships
        else:
          print("\n")
          print ("Player two misses!")
          board[int(guess_row)][int(guess_col)] = "X"
          print_board(board)

      if turn == int(numOfGuesses)-1:
        print("\n")
        print("Draw!")#Draw if both players don't find each other's ships

  play_again = input("Play again? Enter Y for yes or N for no: ")
  #self-explanatory

