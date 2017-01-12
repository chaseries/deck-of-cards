#!/usr/local/bin/python3
from utils import *

import random


class Card:

  def __init__(self, name, suit, discarded=False):
    self.name = name
    self.suit = suit
    self.rank = card_name_rank_map[name]
    self.discarded = discarded

  def __repr__(self):
    repr_ = "<Card object> Name: {}, Suit: {}".format(self.name, self.suit)
    return repr_

  # This might be better on Deck
  def discard(self):
    self.discarded = True
  
  def __eq__(self, other):
    raise NotImplementedError

  def __ne__(self, other):
    raise NotImplementedError

  def __lt__(self, other):
    raise NotImplementedError

  def __gt__(self, other):
    raise NotImplementedError


class Deck:

  suit_names = [ 'diamonds', 'clubs', 'hearts', 'spades' ]

  def __init__(self):
    self.cards = [ Card(n, s) for s in self.suit_names for n in card_names ]

  def __repr__(self):
    raise NotImplementedError # Not sure yet

  def __iter__(self):
    for card in self.cards:
      yield card

  def shuffle(self):
    random.shuffle(self.cards)

  @property
  def discard_pile(self):
    return filter(lambda c: c.discarded, self)

  def _wrap_as_suit(self, suit_name):
    class Suit: pass
    _sfcb = lambda suit: lambda card: card.suit == suit
    suit, cards = Suit(), filter(_sfcb(suit_name), self)
    for card in cards:
      setattr(suit, card.name, card)
    return suit

  @property
  def diamonds(self):
    return self._wrap_as_suit('diamonds')

  @property
  def clubs(self):
    return self._wrap_as_suit('clubs')

  @property
  def hearts(self):
    return self._wrap_as_suit('hearts')

  @property
  def spades(self):
    return self._wrap_as_suit('spades')
