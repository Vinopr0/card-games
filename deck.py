import colorama as c
import random
c.init() # starts colorama

class Card():

    # ranks and suites (T = 10)
    # i made T = 10 because i like it better when they all have the same padding, 
    # and i'd have to sacrifice all others just for the sake of 10.  
    ranks = [f"{n}" for n in range(2, 10)] + ["T", "J", "Q", "K", "A"] # 2 -> A
    suites = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = {v: i + 2 for i, v in enumerate(ranks)} # 2 -> 2 points, Ace -> 14 points

    # for colorama to use for the terminal styling.
    # if you'd rather have RED for both Hearts and Diamonds,
    # and WHITE for both Clubs and Spades, go ahead!

    suites_styling = {
        "Spades": ("♠", c.Fore.WHITE),
        "Hearts": ("♥", c.Fore.RED),
        "Diamonds": ("♦", c.Fore.YELLOW),
        "Clubs": ("♣", c.Fore.BLUE),
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        symbol, color = Card.suites_styling[self.suit]
        return color + f"|{self.rank}{symbol}|" # for terminal

class Deck():

    def __init__(self, deck=[]):
        self.deck = deck

    def create_new_deck(self): # create 52 card deck and clears previous deck
        self.deck = []
        for suit in Card.suites:
            for rank in Card.ranks:
                self.deck.append(Card(rank, suit)) 
    
    def shuffle(self): # shuffles cards, unorders them
        random.shuffle(self.deck)

    def split_in_half(self): # splits deck in half
        return [
            Deck(self.deck[0:26]), # card 1 to card 26
            Deck(self.deck[26:]) # card 27 to card 
            ]

    def print_deck_by_suit(self):
        for suit in Card.suites:
            suit_deck = [card for card in self.deck if card.suit == suit]
            [print(card, end=' ') for card in suit_deck]
            print(f"({len(suit_deck)})")
    
    def print_deck_by_rank(self):
        pass

    def print_deck_unordered(self):
        for card in self.deck:
            print(card, end=' ')
    
    def total_points_in_deck(self):
        return sum([Card.values[card.rank] for card in self.deck])

    def __len__(self):
        return len(self.deck)
    
    def __str__(self):
        return f"This deck has {len(self.deck)} cards that total {self.total_points_in_deck()} points."


aceOfSpades = Card("A", "Spades")
aceOfHearts = Card("A", "Hearts")

new_deck = Deck()
new_deck.create_new_deck()

new_deck.shuffle() 

p1_deck, p2_deck = new_deck.split_in_half()

print(c.Fore.RESET + f"Player 1 has {len(p1_deck.deck)} cards.")
print(p1_deck.total_points_in_deck())
p1_deck.print_deck_by_suit()

print()

print(c.Fore.RESET + f"Player 2 has {len(p2_deck.deck)} cards.")
print(p2_deck.total_points_in_deck())
p2_deck.print_deck_by_suit()

c.Fore.RESET


