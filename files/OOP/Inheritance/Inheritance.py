from __future__ import print_function, division
import sys
import string
import random


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    #an exercise: to write a sorting method for Deck Class
    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        super().__init__()
        self.cards = []
        self.label = label

# 18.10 Data encapsulation - exercise


class Markov:

    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()


    def process_word(self, word, order=2):
        """Processes each word.
        word: string
        order: integer
        During the first few iterations, all we do is store up the words;
        after that we start adding entries to the dictionary.
        """

        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]

        self.prefix = self.shift(self.prefix, word)

    def random_text(self, n=100):
        """Generates random wordsfrom the analyzed text.
        Starts with a random prefix from the dictionary.
        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))

        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.random_text(n - i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=' ')
            start = self.shift(start, word)


    def process_file(self, filename, order=2):
        """Reads a file and performs Markov analysis.
        filename: string
        order: integer number of words in the prefix
        returns: map from prefix to list of possible suffixes.
        """
        fp = open(filename)
        self.skip_gutenberg_header(fp)

        for line in fp:
            if line.startswith('*** END OF THIS'):
                break

            for word in line.rstrip().split():
                self.process_word(word, order)


    def skip_gutenberg_header(self, fp):
        """Reads from fp until it finds the line that ends the header.
        fp: open file object
        """
        for line in fp:
            if line.startswith('*** START OF THIS'):
                break


    def shift(self, t, word):
        """Forms a new tuple by removing the head and adding word to the tail.
        t: tuple of strings
        word: string
        Returns: tuple of strings
        """
        return t[1:] + (word,)


    def main(self, script, filename='158-0.txt', n=100, order=2):
        try:
            n = int(n)
            order = int(order)
        except ValueError:
            print('Usage: %d filename [# of words] [prefix length]' % script)
        else:
            self.process_file(filename, order)
            self.random_text(n)
            print()
