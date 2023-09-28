import random


class Player():
    def __init__(self, playernum, playerhand):
      self.playernum = playernum
      self.playerhand = playerhand

    

#previous code Kieran did
def setup(number_of_players, cards_in_hand):

  #Ask for number of players and set hand length to correct length
  
  
  if number_of_players < 5:
    cards_in_hand =  7
  else:
    cards_in_hand = 5
  
  #Create full deck
  values =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  full_deck = []
  for i in range(3):
    for value in values:
      full_deck.append((value))

  #Shuffle full deck 
  random.shuffle(full_deck)
  shuffled_deck = full_deck
  
  #create player hands list
  player_hands = [[0 for i in range(cards_in_hand)] for j in range(number_of_players)]

  #fill each players hands with cards
  for i in range(number_of_players):
    for j in range(cards_in_hand):
      player_hands[i][j] = (shuffled_deck.pop(0))

  #ask for number of players, set up deck, shuffle and draw to players hands,
  return shuffled_deck,player_hands

  
def guess(players,player_guessed, guessed_card, current_player,shuffled_deck):
  #Checks for the guess inputs from the guess function
  player_guessed = eval(input("Which player do you want to ask? : "))
  guessed_card = input("What card do you want to guess? [1,2,K,Q]: ")
    
  if players[player_guessed-1].playerhand.__contains__(guessed_card):
    print("Correct guess")
    players[player_guessed-1].playerhand.remove(guessed_card)
    players[current_player].playerhand.append(guessed_card)
  else:
    print("Go Fish!")
    players[current_player].playerhand.append(shuffled_deck.pop(0))
    
