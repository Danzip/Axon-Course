from random import *
class Card(object):

    allSymbols = ['heart', 'diamond', 'spade', 'club']
    allNumbers = range(2, 11) + ['J', 'Q', 'K', 'A']

    def __init__(self,number=None,symbol=None):
        self.number=number
        self.symbol=symbol

    def __repr__(self):
        return "{}-{}".format(self.number,self.symbol)

    def __ge__(self,other):
        if Card().allNumbers.index(self.number)>=Card().allNumbers.index(other.number):
            return True
        return False

    def __eq__(self,other):
        if Card().allNumbers.index(self.number)==Card().allNumbers.index(other.number):
            return True
        return False

    def __gt__(self,other):
        if Card().allNumbers.index(self.number)>Card().allNumbers.index(other.number):
            return True
        return False


class Deck(object):
    def __init__(self):
        self.cards=[]
        self.create_deck()




    def create_deck(self):

        for symbol in Card().allSymbols:
            for number in Card().allNumbers:
                self.cards.append(Card(number,symbol))
        shuffle(self.cards)

    def draw_card(self):
        return(self.cards.pop())

class Player(object):
    def __init__(self,name=None):
        self.score=0
        self.card=None
        self.name=name
    def add_name(self,name):
        self.name=name
    def set_card(self,card):
        self.card=card
    def increase_score(self):
        self.score+=1

def quit_game(players,player):
    for p in players:
        print "player {} score is {}".format(p.name,p.score)
    print "goodbye player {}".format(player.name)
    players.remove(player)

def decide_winner(players):
    bestPlayers=[players[0]]
    for player in players[1:]:
        if player.card==bestPlayers[0].card :
            bestPlayers.append(player)
        if player.card>bestPlayers[0].card:
                bestPlayers=[player]
    for player in bestPlayers:
        player.increase_score()
        print "congratulations {} you won this round".format(player.name)

def finish_game(players):
    if (len(players)==1):
        print "congratulations {} You won by attrition".format(players[0].name)
    else:
        print "game ended Goodbye"

def warGame():
    players=[]

    while True:
        choice=raw_input("enter your Name Player, press q to stop setting players")
        if choice in ['q','Q','quit','Quit']:
            break
        players.append(Player(choice))


    deck = Deck()
    while True:

        for player in players:
            print_score=raw_input("{} Would you like to see Your score (Y/N)?".format(player.name))

            if print_score in ['Y','y','yes','yup','ok']:
                print "{} your score is {}".format(player.name,player.score)

            quitC=raw_input("{} Would you like to quit the game? q to quit, anything else to continue".format(player.name))
            if quitC=='q':
                quit_game(players,player)
                continue

            player.card=deck.draw_card()
            print "You drew {}".format(player.card)

        if len(players)>1:
            decide_winner(players)
        else:
            finish_game(players)
            break







warGame()

