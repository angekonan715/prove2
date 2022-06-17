
import random
class Cards:
    ''' this class contains all the state of our cards. 
        It consists of the current_card and the next_card methods
    '''
    def __init__(self):
        self.cards = []
    
    def individual_card(self):
        for i in range(1, 14):
            self.cards.append(i)
        return self.cards   
     #current card display its value  
    def current_card(self):
        self.individual_card()
        return random.choice(self.cards)
    
    # next card display its value
    
    def next_card(self):
        self.individual_card()
        return random.choice(self.cards)
