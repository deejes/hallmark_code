# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The 
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart 
# or diamond.

import itertools

def five_card_combo(hand):
    # takes 7 card hands, returns a list of all possible 5 card hands
    hand_list = []
    hand_list += itertools.combinations(hand,5)
    return hand_list
    

def replace_joker(hands):
     # takes a 5 card hand, returns list of hands it could be if there are jokers.
    njokers = ""
    jokers = []
    hand_list= []
    second_hand_list = []
    for x in hands: 
    # separates jokers and non jokers
        if x[0] != "?":
            njokers += x + " "
        else:
            jokers.append(x)
    if not jokers:
        hand_list.append(hands)
        return hand_list
    if jokers:
        if jokers.pop()  == "?B":
            for x in "23456789TJQKA":
                for y in ("SC"):
                    hand_list.append(njokers + x+y)
        else:
            for x in "23456789TJQKA":
                for y in ("DH"):
                    hand_list.append(njokers + x+y)
    if jokers:
        i = 0
        while 26 > i:
            if jokers[0]  == "?B":
                for x in "23456789TJQKA":
                    for y in ("SC"):
                        second_hand_list.append(str(hand_list[i]) + " "+x+y)
                i += 1
            else:
                for x in "23456789TJQKA":
                    for y in ("DH"):
                        second_hand_list.append(str(hand_list[i])  + " " + x+y)
                i += 1
        hand_list = second_hand_list
    return hand_list
    
def best_wild_hand(hand):
    #takes a 7 card hand and return best 5 card hand
    hand_list = []
    five_card_combinations =  five_card_combo(hand)
    for x in five_card_combinations:
        if len(replace_joker(x)) == 1:
            hand_list.append(x)
        else:
            for y in replace_joker(x):
                hand_list.append(tuple(y.split()))
    val = 0
    best_hand = ""
    for x in hand_list:
        if hand_rank(x) > val and len(set(x)) == 5:
            val = hand_rank(x)
            best_hand = x
    return best_hand
    
def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 
        

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

