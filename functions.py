import random
from collections import Counter

class Card():
    def __init__(self, value):
      self.value = value

    def printCard(cards):
      suit = ['♠', '♦', '♥', '♣']
      lines = [[] for i in range(9)]
      space  = ' '

      for index, card in enumerate(cards):

        # add the individual card on a line by line basis
        if card == '10':
          lines[0].append('┌─────────┐')
          lines[1].append('│{}       │'.format(card))  # use two {} one for char, one for space or char
          lines[2].append('│         │')
          lines[3].append('│         │')
          lines[4].append('│    {}    │'.format(suit[random.randint(0,3)]))
          lines[5].append('│         │')
          lines[6].append('│         │')
          lines[7].append('│       {}│'.format(card))
          lines[8].append('└─────────┘')
        else:
          lines[0].append('┌─────────┐')
          lines[1].append('│{}{}       │'.format(card,space))  # use two {} one for char, one for space or char
          lines[2].append('│         │')
          lines[3].append('│         │')
          lines[4].append('│    {}    │'.format(suit[random.randint(0,3)]))
          lines[5].append('│         │')
          lines[6].append('│         │')
          lines[7].append('│       {}{}│'.format(space,card))
          lines[8].append('└─────────┘')

      result = []
      for index, line in enumerate(lines):
          result.append(''.join(lines[index]))
      return result

class Player():
    def __init__(self, playernum, playerhand, pairs = 0):
      self.playernum = playernum
      self.playerhand = playerhand
      self.pairs = pairs

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

  
def guess(players,current_player,shuffled_deck):
  #Checks for the guess inputs from the guess function
  valid_cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  player_guessed = eval(input("Which player do you want to ask? : "))
  while player_guessed == current_player + 1 or player_guessed > len(players) or player_guessed < 1:
    player_guessed = eval(input("You silly goose! You cant guess that. Which player do you want to ask? : "))
  guessed_card = input("What card do you want to guess? [1,2,K,Q]: ").upper()
  while guessed_card not in valid_cards:
    guessed_card = input("What card do you want to guess? [1,2,K,Q]: ").upper()
    
  if players[player_guessed-1].playerhand.__contains__(guessed_card):
    print("\n")
    print("Correct guess".center(100))
    players[player_guessed-1].playerhand.remove(guessed_card)
    players[current_player].playerhand.append(guessed_card)
    return(True)
  else:
    print("\n")
    print("Go Fish!".center(100))
    print("You drew a {}".format(shuffled_deck[0]).center(100))
    players[current_player].playerhand.append(shuffled_deck.pop(0))
    return(False)
    
def checkHands(players,currentPlayer):
  counter = Counter(players[currentPlayer].playerhand)
  result = [i for i, j in counter.items() if j > 1]
  for i in result:
    players[currentPlayer].playerhand.remove(i)
    players[currentPlayer].playerhand.remove(i)
    players[currentPlayer].pairs += 1

def printScoreboard(players):
  print("\n")
  print("Scoreboard".center(100))
  for i in range(len(players)):
    print("Player {} has {} pairs".format(i+1,players[i].pairs).center(100))
  print("\n")