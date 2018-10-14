#Import the module required to randomise a card from the deck
import random

#Rank of all possible values for cards - with all names shorted to 1character to allow for consistent string manipulation. Such as 10 becoming T or Queen becoming Q
#Rank of suits alphabetically
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

#Allows the card to be stored as a string - allowing string manipulation to calculate value of card and add card to a player/dealer list of cards and total card value
#Basic customisation of data types, reference: https://docs.python.org/2/reference/datamodel.html
  def __str__(self):
    return self.rank + ' of ' + self.suit

#Creation of a deck of playing cards - to be split into dealer cards and player
#Builds a deck organised by primarily value, ascending order through suits alphabetically
#Reference: Python PEP https://www.python.org/dev/peps/pep-0232/
class Deck:
  def __init__(self):
    self.cards = []
    for rank in ranks:
      for suit in suits:
        c = Card(rank, suit)
        self.cards.append(c)

#Function to shuffle cards within the deck
#Reference: https://docs.python.org/3/library/random.html
  def shuffle(self):
    random.shuffle(self.cards)

#Generates a card which is removed from the deck of cards, given to either the player or the dealer
#Pop, reference: https://docs.python.org/2/tutorial/datastructures.html
  def draw_card(self):
    card = self.cards.pop()
    return card
  def show(self):
    for card in self.cards:
        card.show()

#Allows the card to be stored as a string - allowing string manipulation to calculate value of card and add card to a player/dealer list of cards and total card value
  def __str__(self):
    cards = []
    for c in self.cards:
      cards.append(str(c))
    return (str(cards))

#With further expansion and development, I would hope to incorporate a Player class, which has its structure generated here but is not used within the code
class Player:
    def __init__(self, name):
      self.name = name
      self.hand = []

#Would allow a player to draw a card and immediately append it to their hand
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

#Would allow the player to display their cards
    def showHand(self):
        for card in self.hand:
            card.show()

#With further expansion and development, I would hope to incorporate a Dealer class, which has its structure generated here but is not used within the code
class Dealer:
    def __init__(self, name):
      self.name = name
      self.hand = []

#Would allow the dealer to draw a card and immediately append it to their hand
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

#Would allow the dealer to display their cards

    def showHand(self):
        for card in self.hand:
            card.show()


#Calculates the value of a new card dealt through firstly changing the data type of the literal and then uses string indexing/slicing to obtain value of card
def valueCalculator(dealtCard):
    cardHand = []
    cardHand = str(dealtCard)
    cardValue = (cardHand[0])
    if(cardValue == "J" or cardValue == "K" or cardValue == "T" or cardValue == "Q"):
      cardValue = 10
      return(int(cardValue))
    elif(cardValue == "A"):
      cardValue = 11
      return(int(cardValue))
    else:
      return(int(cardValue))

#Beginning of Game Logic

print('---------Deck Before Shuffling----------')
deck = Deck()
print(deck)

#Shuffling deck to fulfill step 3 of the criteria

deck.shuffle()
print('---------Deck After Shuffling----------')
print(deck)

#Player is drawn 2 cards, which are shown to player and value is automatically added up and displayed to user

print("You are drawn two cards \n ")
playerCard1 = deck.draw_card()
playerCard2 = deck.draw_card()
hand = []
#String manipulation to add the newly drawn cards to the player's personal list
print("Your two cards are: \n ")
hand = str(playerCard1) + " // " + str(playerCard2)
print(hand)

#String manipulation and data type changes to calculate values of original 2 cards

value1= (str(playerCard1))
value2= (str(playerCard2))
player_value_First = (value1[0])
player_value_Second = (value2[0])
# Converts the rank of card into a value which is then returned by updating the variable which stores the value of the card
#Calculating value of first player card
if(player_value_First == "J" or player_value_First == "K" or player_value_First == "T" or player_value_First == "Q"):
  player_value_First = 10

elif(player_value_First == "A"):
  player_value_First = 11

else:
  player_value_First = int(player_value_First)
#Calculating value of first second card
if(player_value_Second == "J" or player_value_Second == "K" or player_value_Second == "T" or player_value_Second == "Q"):
  player_value_Second = 10

elif(player_value_Second == "A"):
  player_value_Second = 11
else:
  player_value_Second = int(player_value_Second)

totalValue = int(player_value_First) + int(player_value_Second)
print("The current value of your hand is: \n" + str(totalValue))

#Dealer is drawn 2 cards and value is automatically added up


print("The dealer draws two cards for himself \n")
dealerCard1 = deck.draw_card()
dealerCard2 = deck.draw_card()
dealerHand = []
print("The dealer's first card is: ")
dealerHand = str(dealerCard1) + " // " + str(dealerCard2)
#Displays the dealer's first card only, as per traditional Blackjack - hiding the value of the second card from the user
print(str(dealerCard1))
value3= (str(dealerCard1))
value4= (str(dealerCard2))
dealer_value_First = (value3[0])
dealer_value_Second = (value4[0])
# Converts the rank of card into a value which is then returned by updating the variable which stores the value of the card
#Calculating value of first dealer card
if(dealer_value_First == "J" or dealer_value_First == "K" or dealer_value_First == "T" or dealer_value_First == "Q"):
  dealer_value_First = 10

elif(dealer_value_First == "A"):
  dealer_value_First = 11

else:
  dealer_value_First = int(dealer_value_First)

#Calculating value of second dealer card
if(dealer_value_Second == "J" or dealer_value_Second == "K" or dealer_value_Second == "T" or dealer_value_Second == "Q"):
  dealer_value_Second = 10

elif(dealer_value_Second == "A"):
  dealer_value_Second = 11
else:
  dealer_value_Second = int(dealer_value_Second)
#Totals up the value of the dealer's hand
dealer_totalValue = int(dealer_value_First) + int(dealer_value_Second)

#Prints the value of only dealer's first card to the player - as per criteria 10.c
print("Your current knowledge of the dealer's hand is that it has a value of at least: \n" + (str(dealer_value_First)))
#Prints current status of deck - only for purpose of fulfilling criteria - showing that 4 cards (2 belonging to player, 2 belonging to dealer) have been removed from the deck in order to be appended to their respective hands using python's .pop functionality
print("\n ---------Currently the deck looks like--------- \n")
print(deck)
#Deck is shuffled again as per criteria
print("\n ---------The Deck is shuffled again--------- \n")
deck.shuffle()
print(deck)
#Line to indicate end of deck - make this clear for user
print('\n ------------------ \n')
game = ""
#Generates the game logic in a while loop that checks that the game is in existence before initiating loop
while(game != "exit"):

#Check to see if player has been fortunate enough to achieve Blackjack with their 2 cards and ends game
  if(totalValue == 21):
    print("WOW - you got BLACKJACK - you WIN! \n Play again?")
    break
#Check to see if dealer's got BlackJack
  if(dealer_totalValue == 21):
    print("WOAHHH the dealer got BLACKJACK - you LOSE! \n Play again?")
    break

#Gives the option to player to either HIT or STICK as per criteria 6, 7 and 8
#Value of the cards is added and outputted to user as per criteria 9
#Draws new card for player should player choose HIT
#Adds new value of card to hand, displays the value of the updated hand in full

  game = str(input("Do you want to HIT or STICK? "))
  if(game == "HIT"):
        new_card = deck.draw_card()
        print("You received a new card of: ")
        print(new_card)
        hand += (" // " + str(new_card))
        print("Your hand is now: ")
        print(hand)
        third_card=(valueCalculator(new_card))
        totalValue += third_card
        print("The value of your hand is now: ")
        print(totalValue)
  elif(game == "STICK"):
        print("Your current hand is: " + value1 + " // " + value2)
        print("The current value of your hand is: " + str(totalValue))
  else:
        print("I didn't quite get that... Do you want to HIT or STICK?")
        continue
#Check to see if player has gone bust
  if(totalValue > 21):
    print("Your cards add up to more than 21 - you've gone BUST. You LOSE! \n Play again?")
    break
#Check to see if dealer can still 'hit' as per the rules (dealer must stick if card value >= 17)
  if(dealer_totalValue < 17):
    print("The dealer's full hand is: ")
    print(dealerHand)
    print("The value of the dealer's hand is currently: ")
    print(dealer_totalValue)
    print("The dealer draws a new card")
    dealer_new_card = deck.draw_card()
    print("The dealer received a new card of: ")
    print(dealer_new_card)
    print("The dealer's hand is now: ")
    dealerHand += (" // " + str(dealer_new_card))
    print(dealerHand)
    dealer_third_card = (valueCalculator(dealer_new_card))
    dealer_totalValue += dealer_third_card
    print("The value of the dealer's hand is now: ")
    print(dealer_totalValue)
#Check to see if new card has made the dealer go bust
  if(dealer_totalValue > 21):
    print("The dealer went BUST! You win! \n Play again?")
    break

#Check again to see if dealer can still 'hit'
  if(dealer_totalValue < 17):
    print("The dealer's full hand is: ")
    print(dealerHand)
    print("The dealer draws a new card")
    dealer_new_card = deck.draw_card()
    print("The dealer's hand is now: ")
    dealerHand += str(dealer_new_card)
    print(dealerHand)
    dealer_third_card = (valueCalculator(dealer_new_card))
    dealer_totalValue += dealer_third_card
    print("The value of the dealer's hand is now: ")
    print(dealer_totalValue)
#Check to see if new card has made the dealer go bust
  if(dealer_totalValue > 21):
    print("The dealer went BUST! You win! \n Play again?")
    break
#Check again to see if dealer can still 'hit'
  if(dealer_totalValue < 17):
    print("The dealer's full hand is: ")
    print(dealerHand)
    print("The dealer draws a new card")
    dealer_new_card = deck.draw_card()
    print("The dealer's hand is now: ")
    dealerHand += str(dealer_new_card)
    print(dealerHand)
    dealer_third_card = (valueCalculator(dealer_new_card))
    dealer_totalValue += dealer_third_card
    print("The value of the dealer's hand is now: ")
    print(dealer_totalValue)

#Check to see if dealer has gone bust
  if(dealer_totalValue > 21):
    print("The dealer went BUST! You win! \n Play again?")
    break
 #Check to see if both dealer and player have the card value cards. If so, the game is tied
  if(totalValue == dealer_totalValue):
    print("The game is a push - you and the dealer tied with the same value cards! \n Play again?")
 #Check to see if player's cards = 21
  if(totalValue == 21):
    print("WOW - you got BLACKJACK - you WIN! \n Play again?")
    break
 #Check to see if dealer's cards = 21
  if(dealer_totalValue == 21):
    print("WOAHHH the dealer got BLACKJACK - you LOSE! \n Play again?")
    break
#Check to discover winner - whoever has highest card value under 22
  if(totalValue > dealer_totalValue):
    print("The dealer had the cards")
    print(dealerHand)
    print("You beat the dealer, you win! \n Play again?")
    break
 #Check to discover winner - whoever has highest card value under 22
  elif(totalValue < dealer_totalValue):
    print("The dealer had the cards")
    print(dealerHand)
    print("The dealer beat you - you lose! \n Play again?")
    break
  else:
    break

#Option to print remaining deck - commented out
##  print("******The remaining Deck*******")
##  print(deck)
