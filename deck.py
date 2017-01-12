import utils
import random


class Card:

  def __init__(self, name, suit, discarded=False):
    self.name = name
    self.suit = suit
    self.rank = utils.card_name_rank_map[name]
    self.discarded = discarded

  def __repr__(self):
    return "{} {}".format(utils.card_rank_repr_map[self.rank], 
                          utils.suit_name_repr_map[self.suit])

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

  def __init__(self):
    self.cards = [ 
      Card(n, s) 
      for s in utils.suit_names 
      for n in utils.card_names 
    ]

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
