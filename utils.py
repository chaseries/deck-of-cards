
card_names = [
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
  'ten',
  'jack',
  'queen',
  'king',
  'ace'
  ]

suit_names = [
  'spades',
  'hearts',
  'clubs',
  'diamonds'
  ]

card_ranks = list(range(2,15))

card_rank_reprs = list(map(str, range(2,11))) + (['J', 'Q', 'K', 'A'])

suit_reprs = [ '♠', '♥', '♣', '♦' ]

card_name_rank_map = dict(zip(card_names, card_ranks))

card_rank_repr_map = dict(zip(card_ranks, card_rank_reprs))

suit_name_repr_map = dict(zip(suit_names, suit_reprs))
