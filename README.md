# DeckOfCards

A deck of cards implemented in Python.

Hi, Austin. This is my version. I changed some stuff around that I can explain to you on the phone if you'd like. I spent some time on it because I thought it was a pretty interesting little challenge. Managing the state `Card` and `Deck` while the API depends on some abstract idea of a suit was an interesting little challenge.

So, if you're interested, check out the code in `deck.py`.


## Your bug

I did figure out what was going on (after an hour). Here's the minimum viable example:

```
$    a_list = [1,2,3,4]
$ 
$    for i in a_list:
...    a_list.remove(i)

$    a_list
>    [2,4]
```

The [relevent documentation](https://docs.python.org/2/reference/compound_stmts.html#the-for-statement) (see the **Note**).
