from cards import Cards
class Player:
    ''' An object that the responsibilties to guess higher/lower, 
        to decide if the player wants to continue
        to make the player loose or earn points
        to decide that the game is over once the the total points is 0
    '''   
    def __init__(self):
        self.points = 300
        self.score = 0
        self.is_playing = True
        self.is_guess = True
    
        
#A method that prompt the user to guess either the current card is higher/lower than the next value.       
    def input_guess(self):
        guess = input("Higher or Loyer [h/l]").lower()
        self.is_guess = (guess == 'h')

#a method Keep_playing that prompt to the user either he/she wants to continue and store self.is_playing to True if teh attribute paying == "y"
    def keep_playing(self):
        playing = input("Play again [y/n] ? ").lower()
        self.is_playing = (playing == 'y')

 # define a method called play_game that will lunch our game   
    def play_game(self):
        print("")
        print("================ Welcome To Hilo Game =================")
        print("")
        
        while self.is_playing: 
            cards = Cards()
            current_card = cards.current_card()
            print("The card is : {}".format(current_card))
            self.input_guess()
            next_card = cards.next_card()
            if not self.is_guess:
                if (current_card < next_card):
                    self.points += 100
                else:
                    self.points -= 75
            else:
                if (current_card < next_card):
                    self.points -= 75
                else:
                    self.points += 100
    
            print("Next card was: {}".format(next_card))
            self.score = self.points
            if(self.score > 0):
                print("Your score is : {}".format(self.score))
            else:
                self.score = 0
                print("")
                print("Game is Over")
                break
            self.keep_playing()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("============ Game is Over. Thanks ============")
