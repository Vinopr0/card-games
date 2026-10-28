from deck import Card, Deck
import colorama as c

# game logic and player classes


class Player():
    
    def __init__(self, name, deck=[]):
        self.deck = Deck(deck)
        self.name = name

    def draw(self): # draws from the "top" of the deck.
        return self.deck.pop(0)
    
    def add_card(self, new_card): # only for 1 card.
        self.deck.append(new_card)

    def add_cards(self, new_cards):
        if type(new_cards) != type(list()):
            self.deck += [new_cards]
        else:
            self.deck += new_cards

    def remove_indexed_card(self, index):
        return self.deck.pop(index)

    def number_of_cards(self):
        return len(self.deck)
    
    def __len__(self):
        return len(self.deck)

    def __str__(self): # just colors the name in the terminal, looks pretty.
        return "Player " + c.Fore.MAGENTA + f"{self.name}" + c.Fore.RESET + f" has {len(self.deck)} cards."


main_deck = Deck()

main_deck.create_new_deck()
main_deck.shuffle()

p1_deck, p2_deck = main_deck.split_in_half()

p1 = Player("Jose", p1_deck)
p2 = Player("Mary", p2_deck)

print(p1)
print(p2)

print(p1.draw())