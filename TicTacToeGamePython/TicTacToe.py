#TicTacToe board is built using dictionary. Each position on board is marked with symbol & stored as key in dictionary
#Initial each position on TicTacToe board is empty i.e. in dictionary it is filled with space & stored as key's value
#From start, all 9 positions of TicTacToe board is empty, which is initialized to space as key values in dictionary
tic_tac_toe_board = {'top-left':' ', 'top-mid':' ', 'top-right':' ',
                    'mid-left':' ', 'mid-mid':' ', 'mid-right':' ',
                    'bot-left':' ', 'bot-mid':' ', 'bot-right':' '}

#Method that displays the current TicTacToe board after each move
#This will show how board looks like after each move, what places are filled with X's and O's
def display_board() :
    print('     ' + tic_tac_toe_board['top-left'] + '|' + tic_tac_toe_board['top-mid'] + ' |' + tic_tac_toe_board['top-right'])
    print("--+--+--".center(15))
    print('     ' + tic_tac_toe_board['mid-left'] + '|' + tic_tac_toe_board['mid-mid'] + ' |' + tic_tac_toe_board['mid-right'])
    print("--+--+--".center(15))
    print('     ' + tic_tac_toe_board['bot-left'] + '|' + tic_tac_toe_board['bot-mid'] + ' |' + tic_tac_toe_board['bot-right'])
    print()

#This Method checks whether TicTacToe board gets full or not, Each place on board is filled with some X or O
#This method is used at end of game to check if game is end & on last move of the game when board gets full - whether any player wins on last move or game gets drawn
def isBoardFull() :
    return True if (' ' not in tic_tac_toe_board.values()) else False

#The method returns True if leftmost vertical column is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def vertialCheckLeft() :
    return True if ((tic_tac_toe_board['top-left']=='X' and tic_tac_toe_board['mid-left']=='X' and tic_tac_toe_board['bot-left']=='X') or
        (tic_tac_toe_board['top-left']=='O' and tic_tac_toe_board['mid-left']=='O' and tic_tac_toe_board['bot-left']=='O')) else False

#The method returns True if middle vertical column is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def vertialCheckMid() :
    return True if ((tic_tac_toe_board['top-mid']=='X' and tic_tac_toe_board['mid-mid']=='X' and tic_tac_toe_board['bot-mid']=='X') or
        (tic_tac_toe_board['top-mid']=='O' and tic_tac_toe_board['mid-mid']=='O' and tic_tac_toe_board['bot-mid']=='O')) else False

#The method returns True if rightmost vertical column is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def vertialCheckRight() :
    return True if ((tic_tac_toe_board['top-right']=='X' and tic_tac_toe_board['mid-right']=='X' and tic_tac_toe_board['bot-right']=='X') or
        (tic_tac_toe_board['top-right']=='O' and tic_tac_toe_board['mid-right']=='O' and tic_tac_toe_board['bot-right']=='O')) else False

#The method returns True if topmost horizontal row is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def horizontalCheckTop() :
    return True if ((tic_tac_toe_board['top-left']=='X' and tic_tac_toe_board['top-mid']=='X' and tic_tac_toe_board['top-right']=='X') or
        (tic_tac_toe_board['top-left']=='O' and tic_tac_toe_board['top-mid']=='O' and tic_tac_toe_board['top-right']=='O')) else False

#The method returns True if middle horizontal row is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def horizontalCheckMid() :
    return True if ((tic_tac_toe_board['mid-left']=='X' and tic_tac_toe_board['mid-mid']=='X' and tic_tac_toe_board['mid-right']=='X') or
        (tic_tac_toe_board['mid-left']=='O' and tic_tac_toe_board['mid-mid']=='O' and tic_tac_toe_board['mid-right']=='O')) else False

#The method returns True if bottommost horizontal row is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def horizontalCheckBot() :
    return True if ((tic_tac_toe_board['bot-left']=='X' and tic_tac_toe_board['bot-mid']=='X' and tic_tac_toe_board['bot-right']=='X') or
        (tic_tac_toe_board['bot-left']=='O' and tic_tac_toe_board['bot-mid']=='O' and tic_tac_toe_board['bot-right']=='O')) else False

#The method returns True if left diagonal i.e. \ is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def leftCrossCheck() :
    return True if ((tic_tac_toe_board['top-left']=='X' and tic_tac_toe_board['mid-mid']=='X' and tic_tac_toe_board['bot-right']=='X') or
        (tic_tac_toe_board['top-left']=='O' and tic_tac_toe_board['mid-mid']=='O' and tic_tac_toe_board['bot-right']=='O')) else False

#The method returns True if right diagonal i.e. / is filled with either all O's or all X's
#If it is, game will immidiately end with the declared winner
def rightCrossCheck() :
    return True if ((tic_tac_toe_board['top-right']=='X' and tic_tac_toe_board['mid-mid']=='X' and tic_tac_toe_board['bot-left']=='X') or
        (tic_tac_toe_board['top-right']=='O' and tic_tac_toe_board['mid-mid']=='O' and tic_tac_toe_board['bot-left']=='O')) else False

#ShortHand method to check for all columns, whether if anyone of 3 columns gets filled with either all O's or X's
def allVerticalChecks() :
    return True if(vertialCheckLeft()==True or vertialCheckMid()==True or vertialCheckRight()==True) else False

#ShortHand method to check for all rows, whether if anyone of 3 rows gets filled with either all O's or X's
def allHorizontalChecks() :
    return True if(horizontalCheckTop()==True or horizontalCheckMid()==True or horizontalCheckBot()==True) else False

#ShortHand method to check for both diagonals, whether if anyone of 2 diagonals gets filled with either all O's or X's
def bothDiagonalsCheck() :
    return True if(leftCrossCheck()==True or rightCrossCheck()==True) else False

#This message will be displayed at the start of the game only once
#Both players just need to enter the position each time with either top-mid, top-left, bot-mid, mid-mid etc
#By default, player 1 gets X and player 2 gets to fill O on TicTacToe board
#Pressing 'q' while making any move will quit from the current game. That will end current game as a draw and both players will get 1 points
#Winning = 3 points, Game Draw = 1 point & Loosing = 0 points
print('Enter X or O for input. Press "q" to quit game')
print('place you want for input. Ex- {top, mid, bot - left, right, mid}')
display_board()
playerName1 = str(input('Enter 1st Player name : '))
playerName2 = str(input('Enter 2nd Player name : '))

#This variable is used to track the player who quits , if player1 quits it will be marked as q1 , if player2 quits it will be marked as q2
#whoever quits, game will be drawn & he will get 0 marks for quitting, while the other player gets 1 mark , so if player1 quits : player1=0 & player2=1
quit_marks = ''

#This variable is used to control the chances given to player, each player will get chance one by one.
chancePlayer = 0
#These two variables will work as flag, if any player at any point of time wins the game, their flag will be marked as Winner(True)
isPlayerOneWins = False
isPlayerTwoWins = False

#This dictionary holds the game information like - player name & their Score
#Each time a player wins, his score will be increased with +3 points & on loosing player gets no point. 1 point for a Draw.
playersScoreInfo = {playerName1:0, playerName2:0}

#This method is used to clear everything when a new game starts. It will clear the TicTacToe Board first, mark both flags again as False
#If on previous game if player1 wins his flag will be True, so even after 2nd game with no result, player1 will still be shown as Winner
#Hence, we need to re-initialize both flags to False for new Game
def clearBoardAndEverything() :
    for keys in tic_tac_toe_board.keys() :
        tic_tac_toe_board[keys] = ' '
    global isPlayerOneWins
    isPlayerOneWins = False
    global isPlayerTwoWins
    isPlayerTwoWins = False

#Main Game Play Method, that keeps on asking for player input untill game is won by anyone of player or whole board gets Full & game gets drawn
#chancePlayer variable is incremented by +1 each time, so that each player gets chance one by one. Starting with 0, player1 gets chance when chancePlayer variable is even
#and player2 gets chance when chancePlayer variable is odd , chancePlayer variable gets incremented by +1 after each move
#After each move, it will first input either X or O to position entered by player1 or player2, then immidiately after entering, it will check whether player1 or player2 wins the game after that move or not
def finalGamePlay() :
    while (isBoardFull()==False) :
        #Global is used to make changes in actual global variables outside this finalGamePlay Method
        #If global not used, it will treat all these variables as local variables & actual changes will not reflect into original variables
        global chancePlayer, isPlayerOneWins, isPlayerTwoWins, playersScoreInfo, quit_marks
        #This condition for player1
        if (chancePlayer%2==0 and isBoardFull()==False) :
            print('\n' + playerName1 + "'s Chance")
            pos = str(input('Enter X at position : '))
            #If player1 enters 'q' , game will be drawn & current game gets over
            if pos == 'q' :
                quit_marks = 'q1'
                break
            else :
                tic_tac_toe_board[pos] = 'X'
                chancePlayer += 1
                display_board()
                if (allVerticalChecks()==True or allHorizontalChecks()==True or bothDiagonalsCheck()==True) :
                    isPlayerOneWins=True
                    playersScoreInfo[playerName1] += 3
                    break
        #This if condition is for player2
        if (chancePlayer%2==1 and isBoardFull()==False) :
            print('\n' + playerName2 + "'s Chance")
            pos = str(input('Enter O at position : '))
            #If player2 enters 'q' , game will get drawn
            if pos == 'q' :
                quit_marks = 'q2'
                break
            else :
                tic_tac_toe_board[pos] = 'O'
                chancePlayer += 1
                display_board()
                if (allVerticalChecks()==True or allHorizontalChecks()==True or bothDiagonalsCheck()==True) :
                    isPlayerTwoWins = True
                    playersScoreInfo[playerName2] += 3
                    break

#This method is used to display the final TicTacToe board & the winner of the current Game
def displayTheResult() :
    global isPlayerOneWins, isPlayerTwoWins, playerName1, playerName2, playersScoreInfo, quit_marks
    global chancePlayer
    print('chance : ' + str(chancePlayer))
    if isPlayerOneWins == True :
        print(playerName1 + ' wins')
    elif isPlayerTwoWins == True :
        print(playerName2 + ' wins')
    elif quit_marks == 'q1' :
        playersScoreInfo[playerName2] += 1
        print('game draw')
    elif quit_marks == 'q2' :
        playersScoreInfo[playerName1] += 1
        print('game draw')
    else :
        playersScoreInfo[playerName1] += 1
        playersScoreInfo[playerName2] += 1
        print('game draw')

#This variable tracks whether both players want to play more or not. If 'y' , new game starts, if 'n' game ends
wantMoreGames = 'y'

#This while loop will keep on asking whether both players want to play more or not
#If yes, For new game it will clear whole TicTacToe board, starts the game play & display the result
while True :
    if wantMoreGames == 'y' :
        finalGamePlay()
        displayTheResult()
        print('Score : [' + playerName1 + ' = ' + str(playersScoreInfo[playerName1]) + " , " + playerName2 + " = " + str(playersScoreInfo[playerName2]) + "]")
        clearBoardAndEverything()
        wantMoreGames = str(input('Want to play more ? {y/n}'))
    elif wantMoreGames == 'n' :
        break
