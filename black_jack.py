import random
import time
# Object oriented Black Jack.
# From each class several objects may be created.
# TODO implement proper Black Jack rules.
# https://en.wikipedia.org/wiki/Playing_cards_in_Unicode

# A single card object in a deck of cards.
class Card():

    # Create a card object with specified suit and value
    # self refers to the Card object
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # string representation of card
    def __str__(self):
        as_string = ""
        if self.value == 1:
            as_string += 'A'
        elif self.value == 11:
            as_string += 'J'
        elif self.value == 12:
            as_string += 'D'
        elif self.value == 13:
            as_string += 'K'
        else:
            as_string += str(self.value)
        as_string += self.suit
        return as_string
    
    # To be able to print a list of cards
    # like a list of int:s or str:s
    def __repr__(self):
        return str(self)

# A deck of cards
class Deck():

    # Creat a deck object with 52 cards.
    # self refers to the Deck object
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    # renew deck    
    def create_deck(self):
        self.cards = []
        for i in range(1, 14):
            # spade - unicode
            self.cards.append(Card('\u2660', i))
            # heart - unicode
            self.cards.append(Card('\u2665', i))
            # diamond - unicode
            self.cards.append(Card('\u2666', i))
            # club - unicode
            self.cards.append(Card('\u2663', i))

    # print used for debugging      
    def print(self):
        print(self.cards)

    # shuffle deck
    def shuffle(self):
        random.shuffle(self.cards)

    # draw top most card of deck
    def draw_card(self):
        card = self.cards.pop()
        return card

# A players cards or hand
class Hand():

    # Create a hand object to hold cards
    # for the specified player
    # self refers to the Hand object or the instance of Hand
    def __init__(self, player_name):
        self.cards = []
        self.name = player_name

    # add a card to the hand
    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        return self.name + " hand: " + str(self.cards)

    # To be able to print a list of cards
    # like a list of int:s or str:s
    def __repr__(self):
        return str(self)

    # calculate sum of hand
    def sum(self):
        s = 0
        for card in self.cards:
            s += card.value
        return s

    # empty hand
    def clear(self):
        self.cards = []

# The game Black Jack
class BlackJack():

    # Create the game Black Jack
    # self referes to the Black Jack object
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand("Player")
        self.computer_hand = Hand("Computer")

    # play Black Jack
    def play(self):       
        # start main loop of Black Jack
        play_again = "j"
        while play_again == "j":
            # new game
            self.player_hand.clear()
            self.computer_hand.clear()

            # give player two cards
            self.player_hand.add(self.deck.draw_card())
            self.player_hand.add(self.deck.draw_card())

            # give computer one card
            self.computer_hand.add(self.deck.draw_card())

            # print hands
            print(self.computer_hand)
            print(self.player_hand)

            choice = input("choose hit or stand ")

            while choice == "hit":
                # hit
                self.player_hand.add(self.deck.draw_card())
                print(self.player_hand)
                choice = input("choose hit or stand")

            # stand
            # => computers turn
            while self.computer_hand.sum() < 17:
                self.computer_hand.add(self.deck.draw_card())
                print(self.computer_hand)
                # wait 1 second
                time.sleep(1)

            # final print of hands and sum
            print(self.computer_hand, "sum: ", self.computer_hand.sum())
            print(self.player_hand, "sum: ", self.player_hand.sum())

            # who winns?
            if self.player_hand.sum() > self.computer_hand.sum():
                print(self.player_hand.name, "wins")
            else:
                print(self.computer_hand.name, "wins")
                
            # stay or leave main game loop
            play_again = input("Vill du spela igen? (j/n) ")


# create a black jack object
black_jack = BlackJack()
# run the game
black_jack.play()

