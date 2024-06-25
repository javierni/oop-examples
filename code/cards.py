#cards.py

from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]
    def add_card(self,card):
        self.cards.append(card)

queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
deck = Deck([queen_of_hearts, ace_of_spades])
king_of_diamonds = PlayingCard('K', 'Diamonds')
deck.add_card(king_of_diamonds)
deck

