#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:53:00 2020

@author: jeancho
"""
    ###########################################################
    #  ex8b.py: War 
    #
    #  Algorithm
    #    opens cards.py (classes)
    #    calls function that creates and displays hands for player 1 and 2
    #    click enter to start battle or 'n' to end
    #    loop while gameon = True (if 'n' or game over, gameon = False)
    #       call function to start and play new round
    #       output the hands
    #     gameover when player runs out of cards or when 'n' entered
    ###########################################################

import cards

#Distributing cards
def distribute_cards(the_deck):
    '''
    Parameters
    ----------
    the_deck : Deck from cards.py

    Returns
    -------
    p1hand : list of cards
        player 1's hand.
    p2hand : list of cards
        player 2's hand.
    '''
    
    p1hand = []
    p2hand = []
    
    for i in range(26):
        p1hand.append(the_deck.deal())
        p2hand.append(the_deck.deal())
    return (p1hand, p2hand)

#new round        
def new_round(p1hand, p2hand):
    '''
    Parameters
    ----------
    p1hand : list of cards
        player 1's hand.
    p2hand : list of cards
        player 2's hand.

    Returns
    -------
    endoutp : string
        update on round.
    p1hand : list of cards
        player 1's hand.
    p2hand : list of cards
        player 2's hand.

    '''
    #Reverse hands to be able to use .pop() func
    p1hand = p1hand[-1::-1]
    p2hand =p2hand[-1::-1]
    #Cards
    p1card = p1hand.pop()
    p2card = p2hand.pop()
    #Output string
    endoutp = ''
    
    #check for ace
    p1rank = p1card.rank()
    p2rank = p2card.rank()
    
    if 'A' in str(p1card):
        p1rank = 14
    elif 'A' in str(p2card):
        p2rank = 14
    
    #Round
    if p1rank == p2rank: #stalemate
        p1hand = p1hand[-1::-1]
        p2hand =p2hand[-1::-1]
        endoutp = f'Battle was P1: {p1card} P2: {p2card} \
              Stalemate.'
    elif p1rank > p2rank: #player 1 wins
        p1hand = p1hand[-1::-1]
        p2hand =p2hand[-1::-1]
        p1hand.append(p2card)
        p1hand.append(p1card)
        
        endoutp = f'Battle was P1: {p1card} P2: {p2card}. Player 1 wins battle.'
    else:                 #player 2 wins
        p1hand = p1hand[-1::-1]
        p2hand =p2hand[-1::-1]
        p2hand.append(p1card)
        p2hand.append(p2card)
        
        endoutp = f'Battle was P1: {p1card} P2: {p2card}. Player 2 wins battle.'  
    return(endoutp, p1hand, p2hand)



def winner_check(p1hand, p2hand):    
    '''    
    Parameters
    ----------
    p1hand : list of cards
        player 1hand.
    p2hand : list of cards
        player 2 hand.

    Returns
    -------
    endoutp : string
        winner announcement
    '''
    endoutp = ''
    if len(p1hand) > len(p2hand):
        endoutp ='Player 1 wins!'
    else:
        endoutp = 'Player 2 wins!'
    return(endoutp)   

        
def main():
    # Create the deck of cards
    the_deck = cards.Deck()
    the_deck.shuffle()
    
    hands = distribute_cards(the_deck)
    p1hand = hands[0]
    p2hand = hands[1]
    print('===Starting hands===')
    print('Player1 hand: ', p1hand)
    print()
    print('Player2 hand: ', p2hand)
    
    #Round start
    
    roundnum = 0 #for winner checking
    gameon = True #loop
    
    while gameon == True:
        startround = input('To battle press "enter" key. To stop enter "n"')
        if startround.lower() == 'n':
            if roundnum > 0:
                print(winner_check(p1hand, p2hand))
            gameon = False
        else:
            roundnum += 1 
            print() #spacing
            new_round_returns = new_round(p1hand, p2hand)
            nr_endoutp = new_round(p1hand, p2hand)[0]
            nr_p1hand = new_round(p1hand, p2hand)[1]
            nr_p2hand = new_round(p1hand, p2hand)[2]
            print(nr_endoutp)
            print('Player 1 hand: ', nr_p1hand)
            print('Player 2 hand: ', nr_p2hand)
            p1hand = nr_p1hand
            p2hand = nr_p2hand
            
        if len(p1hand) == 0 or len(p2hand) == 0: #if someone ran out of cards:
            print(winner_check(p1hand, p2hand))
            gameon = False

            

if __name__ == '__main__':
    main()



































        
        
        