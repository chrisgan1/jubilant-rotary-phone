import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)

                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        one_card = self.deck.pop(0)
        return one_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE, CHANGE ACE VALUE TO 1 INSTEAD OF 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Enter the amount you would like to bet: "))
        except:
            print("Please enter a valid input!")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips for that bet!")
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:

        x = input("Hit of Stand? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, dealer's turn")
            playing = False
        else:
            print("Sorry, I did not understand. Please enter h or s only!")
            continue
        break

def show_some(player,dealer):

    # SHOW ONE OF DEALERS CARDS AND SHOW ALL PLYAERS CARDS
    print("\nDealer's hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):

    # SHOW ALL PLAYER CARDS AND ALL DEALER CARDS
    # SHOW VALUE OF HAND FOR EACH
    # EXAMPLE 1 AND EXAMPLE 2 BOTH DO THE SAME THING

    # EXAMPLE 1
    print("\nPlayer's hand: ", *dealer.cards, sep='\n')
    print(f"Value of Player's hand is: {player.value}")

    # EXAMPLE 2
    print("\nDealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("BUST DEALER!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie!")

while True:

    print("Welcome to the game!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)
    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

        if player_hand.value < 21:

            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print("\nPlayer total chips are at: {}".format(player_chips.total))

    new_game = input("Would you like to play again? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break

