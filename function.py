import random

#previous code Kieran did
def setup():
  number_of_players = eval(input("how many people are going to play?"))
  number_of_players = int(number_of_players)
  if number_of_players < 5:
    cards_in_hand =  7
  else:
    cards_in_hand = 5

  suits = ['Spades','Clubs','Hearts','Diamond']
  values =['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
  full_deck = []
  for suit in suits:
    for value in values:
      full_deck.append((value,suit))

  shuffled_deck = random.shuffle(full_deck)
  
  player_hands = [[0 for i in range(number_of_players)] for j in range(cards_in_hand)]

  for i in range(number_of_players):
    for j in range(cards_in_hand):
      player_hands.append[i-1[shuffled_deck.pop()]]  
    print(player_hands[i-1])
  
  
  
  #ask for number of players, set up deck, shuffle and draw to players hands,
  return shuffled_deck,player_hands

# def Draw_Card(shuffled_deck, player_hands):
#   #Draw card from the top of shuffled deck and append to players hand

def guess():
    #No input just return the player that is being checked and the card check
    player_guessed = input("Which player do you want to ask? : ")
    guessed_card = input("What card do you want to guess? : ")
    return player_guessed,guessed_card
  
def Check_Hand(player_hands, guessed_card):
  #Checks for the guess inputs from the guess function
  guess_correct = False
  return guess_correct

