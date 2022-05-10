import random

class Card:
    def __init__(self, id, name, suit, value, visibility = True):

        self.id = id
        self.suit = suit
        self.visibility = visibility
        
        if 1< id< 10:
            self.name = name + "of " + suit
        
        else:
            self.name = "{name} of ".format(name = ("Ace" if id == 1 else "Jack" if id ==11 else "Queen" if id == 12 else "King")) + suit

        if 1<id<10:
            self.value = id
        elif id == 1:
            value == 11
            self.value = value
        else:
            value = 10
            self.value = value

    def __repr__(self):
        if self.visibility == False:
            return "Hidden"
        else:
            return self.name

def generate_cards():
    cards = []
    suits = ["Spades", "Diamonds", "Hearts", "Clovers"]

    for i in range(1, 13):
        for suit in suits:

            card_i = Card(i,str(i),suit,i)
            cards.append(card_i)
    
    return cards

def shuffle_deck():
    deck = random.sample(generate_cards(),len(generate_cards()))

    return deck

def deal_cards(hand, deck):

    dealt_card = deck.pop(0)
    hand.append(dealt_card)

    return hand

def count_hand(hand):
    count_list =[]
    for card in hand:
        count_list.append(card.value)
        count_sum = sum(count_list)
    
    while 11 in count_list:
        if count_sum > 21:
            for i in range(len(count_list)):
                if count_list[i] == 11:
                    count_list[i] = 1
                    count_sum = sum(count_list)
                    break
        else:
            for i in range(len(count_list)):
                if count_list[i] == 11:
                    count_list[i] = 11
                    count_sum = sum(count_list)
                    break

    return count_sum
        
def dealer_decision(hand, deck):
 
    if count_hand(hand) < 18:
        deal_cards(hand, deck)
        for i in range(len(hand)):
            if i > 0:
                hand[i].visibility = False
             
    else:
        return hand

def welcome():
    welcome_rug = input("Welcome to Blackjack :D \n To continue, press Enter.")

    if welcome_rug == "":
        return game()
    else:
        print("\n")
        print("ERROR! Please check your input.")
        return welcome()

def game():
    my_hand = []
    dealer_hand = []
    deck = shuffle_deck()

    deal_cards(my_hand, deck)
    deal_cards(dealer_hand, deck)

    print("\n")
    print("Your hand: "), print(my_hand)
    print("Dealer's hand: "), print(dealer_hand)
    busted = False

    while busted == False:
        print("\n")
        choice = input("Type: 'go' to be dealt another card. Type: 'no' to stop here.")
        
        if choice == "go":
            deal_cards(my_hand, deck)
            dealer_decision(dealer_hand, deck)
        elif choice == "no":
            dealer_decision(dealer_hand, deck)   
        else:
            print("\n")
            print("ERROR!! Please type either 'go' or 'no'")
            pass
        
        print("\n")
        print("Your hand: "), print(my_hand)
        print("Dealer's hand: "), print(dealer_hand)

        if count_hand(my_hand) > 21 or count_hand(dealer_hand) >21:
            busted = True
            break
        elif choice == "no" and count_hand(dealer_hand) >= 18:
            busted = True
            break
        else:
            busted = False



    if count_hand(my_hand) > 21 and count_hand(dealer_hand) <= 21 :
        for card in dealer_hand:
            if card.visibility == False:
                card.visibility = True
        print("\n")
        print("This is the Dealer's hand: "), print(dealer_hand)
        print("You are BUSTED!\nYou Lose!")
    elif count_hand(my_hand) <=21 and count_hand(dealer_hand) > 21:
        for card in dealer_hand:
            if card.visibility == False:
                card.visibility = True
        print("\n")
        print("This is the Dealer's hand: "), print(dealer_hand)
        print("The dealer is BUSTED! \nYou Win!")
    elif count_hand(my_hand) >21 and count_hand(dealer_hand)>21:
        for card in dealer_hand:
            if card.visibility == False:
                card.visibility = True
        print("\n")
        print("This is the Dealer's hand: "), print(dealer_hand)
        print("Both of you are BUSTED! \nNobody Wins :(")
    else:
        for card in dealer_hand:
            if card.visibility == False:
                card.visibility = True
        print("\n")
        print("This is the Dealer's hand: "), print(dealer_hand)

        if count_hand(my_hand)> count_hand(dealer_hand):
            if count_hand(my_hand) ==21:
                print("BlackJack!\n You Win! :D")
            else:
                print("You Win! :D")
        elif count_hand(my_hand) < count_hand(dealer_hand):
            if count_hand(dealer_hand) == 21:
                print("BlackJack!\n The dealer Won! :D")
            else:
                 print("The dealer Won! :D")
        else:
            print("Tie")   
    restart()

def restart():
    question = input("If you'd like to play again, press Enter. If not, press anything else")

    if question == "":
        print("Welcome Back!")
        return game()

    else:
        print("Thank you for playing! Have a good day! :) ")
        

welcome()

    







