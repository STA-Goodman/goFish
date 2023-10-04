import functions
import os
gameOver = False


number_of_players = eval(input("how many people are going to play?"))
if number_of_players < 5:
    cards_in_hand =  7
else:
    cards_in_hand = 5

shuffled_deck,player_hands = functions.setup(number_of_players,cards_in_hand)

players = []
for number in range(number_of_players):
    #create an instance of player classs with correct cards_in_hand
    players.append(functions.Player(playernum = number,playerhand = player_hands[number]))
#function.guess()
#function.Check_Hand()

#Game loop

currentPlayer = 0
while gameOver == False:
    #skip player if they have no cards
    correct = True
    if len(players[currentPlayer].playerhand) == 0:
        currentPlayer + 1

    

    print("Game is starting")
    #clear screen after player turn
    os.system('cls')
    while correct == True:
        if players[currentPlayer].playerhand == []:
            break
        
        cont = eval(input("Player ,"+ str(currentPlayer + 1) + "'s turn. Press 1 to continiue"))
        
        #print current players hand
        print(players[currentPlayer].playerhand) 
        correct = functions.guess(players,currentPlayer,shuffled_deck)
        
        functions.checkHands(players,currentPlayer)
        print(players[currentPlayer].playerhand)
        print("You have",players[currentPlayer].pairs,"pairs")
    cont = eval(input("Your turn is over. Press 1 to continiue"))
    
    if currentPlayer < number_of_players - 1:
        currentPlayer += 1
    else:
        currentPlayer = 0
        
    
    if len(shuffled_deck) == 0:
        a = 0
        for i in players[currentPlayer]:
            if len(i.playerhand) == 0:
                a += 1
        if a == number_of_players:
            gameOver = True
            break
            

#while True:
    #break