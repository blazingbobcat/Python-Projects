import pygame as pg
import sys, os
from pygame.locals import *
from random import *
from textprint import *

# Choose-your-own adventure engine
# Josh Klipstein
# Started:  24 November 2020

'''
    A single player must roll to select a State created by a list in the Game
    object.  Then the player must pass through a series of events in a State
    created by an Event object to progress in the game.  Events are related
    to a story being read passage by passage.  At the end of each State, when
    all events are cleared, a treasure is awarded to the player if he or she
    survives.  A roll again determines the outcome of every event.  The player
    must roll at or above the given number to pass an event.  When in possession
    of a treasure, sometimes that will present a lower number to roll to allow
    for passage.  Failure to roll high enough results in one less life for the
    player.  All the player should concern him or herself about is surviving
    each state.  There will be one final State that can not be chosen.  All
    other states must be cleared and then this one will be automatically chosen.
    Recovering the treasure in this State means completion of the game.  Every
    state will have a variable number of events, in this case randomized.  There
    are 3 States in this demonstration and up to five events every State.  The
    Game object simply keeps the flow of the game going until either the player
    dies or recovers all the treasures.
'''

class State(object):
    def __init__(self, complete, number, events):
        self.__ROLL = 20
        self.__HALF_ROLL = self.__ROLL // 2
        self.__MID_ROLL = self.__ROLL * 3 // 4
        self.__MIN_ROLL = 1
        self.__complete = complete #bool
        self.__number = number # Number of state int
        self.__events = events # int
        self.__obstacle = self.__MIN_ROLL # int
        self.__special = self.__HALF_ROLL # int

    def __del__(self):
        pass

    def set_obstacle(self):
        self.__obstacle = randint(self.__MID_ROLL, self.__ROLL)
        self.__special = randint(self.__HALF_ROLL, self.__MID_ROLL)
        
    def get_obstacle(self):
        return self.__obstacle

    def get_special(self):
        return self.__special

    def set_complete(self):
        self.__complete = True

    def get_complete(self):
        return self.__complete

    def get_number(self):
        return self.__number

    def next_event(self):
        self.__events -= 1

    def get_num_events(self):
        return self.__events

class Player(object):
    def __init__(self, health):
        self.__health = health # int
        self.__treasure = [] # strings
        self.__events = 0 # int
        self.__alive = True # bool

    def __del__(self):
        pass

    def get_name(self):
        return self.__name

    def dec_health(self):
        self.__health -= 1

    def get_health(self):
        return self.__health

    def add_treasure(self, treasure):
        self.__treasure.append(treasure)
        
    def get_treasure(self):
        return self.__treasure

    def add_event(self):
        self.__events += 1
        
    def get_events(self):
        return self.__events

    def set_alive(self):
        self.__alive = False

    def get_alive(self):
        return self.__alive

class Story(object):
    # Story class
    def __init__(self, screen, states, textPrint):
        self.__screen = screen # Game screen
        self.__BLACK = pg.Color('black')
        self.__WHITE = pg.Color('white')
        self.__THOUSAND = 1000 # One second
        self.__MAX_ROLL = 20 # Maximum roll number
        self.__MIN_ROLL = 1 # Minimum roll number
        self.__FPS = 60
        self.__STATES = states # States list
        self.__clock = pg.time.Clock() # Clock object
        self.__number = 0 # State completion tally
        self.__textPrint = textPrint # Text print object
        self.__rolls = 0 # Rolls number
        self.__roll = 1 # Roll variable

    def __del__(self):
        pass

    # Rolling function
    def roll_dice(self):
        self.__roll = randint(self.__MIN_ROLL, self.__MAX_ROLL)
        
    # Screen printing function
    def print(self, string):
        self.__textPrint.tprint(self.__screen, string)

    # Line printing function
    def print_line(self, string):
        self.__textPrint.tprint(self.__screen, string)
        pg.display.flip()
        self.__clock.tick(self.__FPS)

    # Function to show intro to game
    def intro(self):
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit() # Quit game at any time
                if event.type == pg.KEYDOWN:
                    # Get key input
                    keys = pg.key.get_pressed()
                    if keys[pg.K_ESCAPE]:
                        self.quit() # Same quitting mechanism
                    elif keys[pg.K_SPACE]:
                        done = True # Skip introduction
            self.__screen.fill(self.__WHITE)
            self.__textPrint.reset()
            self.print("Welcome to the choose-your-own adventure engine!")
            self.print("How this essentially works is like interactive fiction.")
            self.print("You select a State out of many (in this case, 3) and pass")
            self.print("a series of events by rolling a 20-sided die.  The minimum")
            self.print("number to roll for each event will vary, as will the number")
            self.print("of events per state.  At the end of each State, if you survive,")
            self.print("you will recover a treasure hidden in the state.  This may grant you")
            self.print("a special ability to pass events at times with a lower")
            self.print("minimum number to roll.  But if you fail to roll high enough,")
            self.print("you will lose life.  You have 10 lives in this demonstration.")
            self.print("The player will be shown their remaining lives if they lose any.")
            self.print("The game ends if either you lose all your lives or collect")
            self.print("all possible treasures.  Note that the final State (in this case, 3rd)")
            self.print("is inaccessible until the player clears all the other States.  You")
            self.print("will automatically move to this state upon completion of the others.")
            self.print("States already completed are also inaccessible.")
            self.print("Please press space to continue.")
            pg.display.flip()
            self.__clock.tick(self.__FPS)

    # Obstacle function
    def obstacle(self, number, special, player):
        done = False
        while not done:
        # Print out event and prompt for roll
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                elif event.type == pg.KEYDOWN:
                    keys = pg.key.get_pressed()
                    # Get key input
                    if keys[pg.K_ESCAPE]:
                        self.quit()
                    elif keys[pg.K_SPACE]:
                        self.roll_dice() # Get roll
                        self.print_line("You rolled {}".format(self.__roll))
                        self.__rolls += 1 # add on to total rolls
                        pg.time.delay(self.__THOUSAND)

                        # Roll checking
                        if (len(player.get_treasure()) > 0 and self.__roll >= special):
                            self.print_line("Player has successfully circumvented this obstacle.") # Give player event
                            pg.time.delay(self.__THOUSAND)
                        elif self.__roll >= number:
                            self.print_line("Player has successfully circumvented this obstacle.") # Regular roll
                            pg.time.delay(self.__THOUSAND)
                        else:
                            self.print_line("Ouch! Player gets hurt by this obstacle.") # Take away player health
                            player.dec_health()
                            self.print_line("Player's health is {}".format(player.get_health()))
                            pg.time.delay(self.__THOUSAND)
                            if (player.get_health() <= 0):
                                self.print_line("Player has lost all lives.  Game over.") # Print game over message if player health 0
                                pg.time.delay(2 * self.__THOUSAND)
                                self.quit()

                        done = True

    # Read event function
    def story(self, state, player):
        # The game is driven by the story.  Events unfold with every roll.
        self.__screen.fill(self.__WHITE)
        self.__textPrint.reset()

        # Roll dice output
        self.print("Number of rolls: {}".format(self.__rolls))
        
        # Check if State is finished
        if state.get_num_events() == 0:
            self.print_line("You've recovered the treasure.") # Show message to player
            pg.time.delay(self.__THOUSAND * 2)
            player.add_treasure(str(self.__number)) # Give player treasure
            self.__number += 1
        else:      
            self.print_line("Passage from story...") # Passage from story
            pg.time.delay(2 * self.__THOUSAND // 2)
            self.print_line("Obstacle!") # Obstacle
            pg.time.delay(self.__THOUSAND // 2)
            state.set_obstacle() # Set up minimum number to roll for regular and special
            self.print_line("Roll {} to get around obstacle yourself.".format(state.get_obstacle())) # Regular roll
            pg.time.delay(self.__THOUSAND // 2)
            if (len(player.get_treasure()) > 0 and random() > 0.5):
                self.print_line("Roll {} to use special ability".format(state.get_special())) # Special roll
            self.obstacle(state.get_obstacle(), state.get_special(), player)

        return self.__number

    # Function to clear game
    def win(self):
        self.print_line("You've recovered all the treasures!  Congratulations!.") # Print out win message
        pg.time.delay(5 * self.__THOUSAND)
        self.quit()

    # Quitting function
    def quit(self):
        pg.quit()
        sys.exit()
    
class Game(object):
    # Game class
    def __init__(self):
        self.__BLACK = pg.Color('black')
        self.__WHITE = pg.Color('white')
        self.__THOUSAND = 1000
        self.__WIDTH = 500
        self.__HEIGHT = 500
        self.__FPS = 60
        self.__TITLE = "Choose-Your-Own Adventure Engine!"
        self.__MAX_STATES = 3 # Maximum number of states
        self.__MAX_EVENTS = 5 # Maximum number of events
        self.__MIN_EVENTS = 1 # Minimum number of events
        self.__MAX_ROLL = 20
        self.__MIN_ROLL = 1
        self.__PLAYER = Player(10) # Player
        self.__STATES = [State(False, x,
                               randint(self.__MIN_EVENTS,
                                       self.__MAX_EVENTS)) for x in range(self.__MAX_STATES)] # list
        self.__clock = pg.time.Clock()
        self.__events = None # Event object
        self.__last = False # Variable if last state is accessible
        self.__state = None # Temp variable for state
        self.__tally = 0 # State completion variable

        # Start up window
        pg.init()
        self.__screen = pg.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pg.display.set_caption(self.__TITLE)

        self.__textPrint = TextPrint()  # Text print object
        self.__story = Story(self.__screen, self.__STATES, self.__textPrint) # Story object

    def __del__(self):
        pass

    def set_last(self):
        self.__last = True

    def get_events(self):
        return self.__state.get_num_events()

    # Rolling function
    def roll_dice(self):
        self.__roll = randint(self.__MIN_ROLL, self.__MAX_ROLL)

    def print(self, string):
        self.__textPrint.tprint(self.__screen, string)

    def print_line(self, string):
        self.__textPrint.tprint(self.__screen, string)
        pg.display.flip()
        self.__clock.tick(self.__FPS)

    # Introduction function
    def new(self):
        self.__story.intro() # Show introductory text
                            
        self.next_state() # Go to next state function

        return # Go back to program

    # Function to roll for new state
    def next_state(self):
        done = False
        while not done:
            self.__screen.fill(self.__WHITE)
            self.__textPrint.reset()
        
            # Ask players to roll for state
            if (self.__state is not None):
                self.print("State {} is finished.".format(self.__state.get_number() + 1))
            if (self.__last):
                self.__roll = len(self.__STATES) # Set roll variable to last
                done = True
            else:
                self.print_line("Please hit spacebar to roll for state.  Roll {0}-{1}.".format(1, len(self.__STATES) - 1))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.quit()
                    elif event.type == pg.KEYDOWN:
                        keys = pg.key.get_pressed()
                        if keys[pg.K_ESCAPE]:
                            self.quit()
                        elif keys[pg.K_SPACE]:
                            self.roll_dice()
                            if (self.__roll > len(self.__STATES) - 1):
                                self.print_line("You rolled {}.  Please roll again.".format(self.__roll))
                                pg.time.delay(self.__THOUSAND)
                            elif (self.__STATES[self.__roll-1].get_complete()):
                                self.print("You rolled {}.".format(self.__roll))
                                self.print("State {} is already complete.  Please roll again.".format(self.__roll))
                                pg.display.flip()
                                self.__clock.tick(self.__FPS)
                                pg.time.delay(self.__THOUSAND)
                            else:
                                done = True

        self.__STATES[self.__roll-1].set_complete()
        self.__state = self.__STATES[self.__roll-1] # Hold temp variable
        
        if self.__tally > 0:
            self.print_line("State {}...".format(self.__state.get_number() + 1))  # Tell player which state they're in
        else:
            self.print_line("Your journey starts in state {}.".format(self.__state.get_number() + 1))
        pg.time.delay(2 * self.__THOUSAND)

        return
    
    # Game loop
    def main(self):
        while True:
            
            self.__tally = self.__story.story(self.__state, self.__PLAYER) # Go to event reading function in story class
            print("Tally: {}".format(self.__tally)) # DEBUG

            if (self.get_events() > 0):
                # Check for events complete or state complete
                self.__state.next_event()
            else:   
                # Check to see if all states but last one are complete
                if self.__tally == len(self.__STATES) - 1:
                    self.set_last() # Set last state variable
                elif self.__tally == len(self.__STATES):
                    self.__story.win() # Go to win function in Story
                    self.quit()
                self.__rolls = 0 # Reset num of rolls
                self.next_state() # Call next state function
                
    # Quitting function
    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    g = Game()
    g.new()
    g.main()
