import functions

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
print(players[1].playerhand,players[0].playerhand)
##function.guess()
#function.Check_Hand()

#Game loop
while gameOver == False:
    currentPlayer = 0
    print("Game is starting")
    cont = eval(input("Player ,"+ currentPlayer + "'s turn. Press 1 to continiue"))
    if cont == 1:
        break
    else:
        print("Invalid input")
    
    print(players[currentPlayer].playerhand) 
    functions.guess(players,)

#while True:
    #break