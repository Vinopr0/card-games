from deck import Card, Deck
import colorama as c

# game logic and player classes


class Player():
    
    def __init__(self, name, deck=Deck()):
        self.deck = deck
        self.name = name

    def draw_whole_deck(self):
        whole_deck = self.deck.deck
        self.deck = Deck()
        return whole_deck

    def draw(self): # draws from the "top" of the deck.
        return self.deck.pop(0)
    
    def add_card(self, new_card): # only for 1 card.
        self.deck.append(new_card)

    def add_cards(self, new_cards):
        if type(new_cards) != type(list()):
            self.deck.append(new_cards)
        else:
            self.deck.extend(new_cards)

    def remove_indexed_card(self, index):
        return self.deck.pop(index)

    def number_of_cards(self):
        return len(self.deck)
    
    def __len__(self):
        return len(self.deck)

    def __str__(self): # just colors the name in the terminal, looks pretty.
        return "Player " + c.Fore.MAGENTA + f"{self.name}" + c.Fore.RESET + f" has {len(self.deck)} cards."



class War():
    
    def __init__(self, cards_to_draw_on_war_event=3):
        self.war_draw = cards_to_draw_on_war_event # self-explanatory?

    def war_matchup(self, player1, player2, cards1, cards2):
        total_value_cards1 = sum([card.get_value() for card in cards1]) # total value of card draw
        total_value_cards2 = sum([card.get_value() for card in cards2])
        if total_value_cards1 > total_value_cards2:
            player1.add_cards(cards1 + cards2)
            return player1.name # indicates who won at index 1, and the new card set.
        elif total_value_cards2 > total_value_cards1:
            player2.add_cards(cards1 + cards2)
            return player2.name
        return None

    def war_event(self, player1, player2, cards1=None, cards2=None):
        cards1 = [] if cards1 is None else cards1 # clears the list, so the cards don't spill over to the next war.
        cards2 = [] if cards1 is None else cards2

        if len(player1.deck) < self.war_draw: # win check
            player1.add_cards(cards1 + cards2 + player2.draw_whole_deck()) # adds the cards from the war, along with the rest of the other player's deck
            return player2.name
        elif len(player2.deck) < self.war_draw:
            player1.add_cards(cards1 + cards2 + player2.draw_whole_deck())
            return player1.name

        # automatically draws cards
        cards1 += [player1.draw() for _ in range(0, self.war_draw)]
        cards2 += [player2.draw() for _ in range(0, self.war_draw)]
        war = self.war_matchup(player1, player2, cards1, cards2)

        if war is None: # repeats the war until there is a winner, recursive
            return self.war_event(player1, player2, cards1, cards2)
        elif war[0] == player1.name:
            player1.add_cards(war[1])
        elif war[0] == player2.name:
            player2.add_cards(war[1])
        return None


    def compare_cards(self, player1, player2, card1, card2):
        if card1.get_value() > card2.get_value():
            player1.add_cards([card1, card2])
        elif card2.get_value() > card1.get_value():
            player2.add_cards([card1, card2])
        else:
            return self.war_event(player1, player2, [card1], [card2])



# game setup for 2 CPUs

main_deck = Deck() # instance of deck
game_on = True

# 52 card deck created!
main_deck.create_new_deck()
main_deck.shuffle()

# splits deck in half, distributes to 2 new decks
p1_deck, p2_deck = main_deck.split_in_half() 

# creates P1 and P2 instance
p1 = Player("Jose", p1_deck)
p2 = Player("Mary", p2_deck)

WAR_GAME = War()

turn_number = 0

while game_on:
    turn_number += 1
    print(c.Fore.CYAN + f"\nTurn {turn_number}")

    turn_state = WAR_GAME.compare_cards(p1, p2, p1.draw(), p2.draw())
    p1.deck.print_deck_by_suit(p1.name)
    print(c.Fore.BLACK + str(p1.deck))
    p2.deck.print_deck_by_suit(p2.name)
    print(c.Fore.BLACK + str(p2.deck))

    if len(p2.deck) == 0:
        print(f"{p1.name} wins!")
        game_on = False
    elif len(p1.deck) == 0: 
        print(f"{p2.name} wins!")
        game_on = False
    else:
        p1.deck.shuffle()
        p2.deck.shuffle()
    