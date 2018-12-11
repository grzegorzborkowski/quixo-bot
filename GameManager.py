from AbstractPlayer import *
from RandomPlayer import *
from MiniMaxPlayer import *
import tqdm


class GameManager:
    player_won = 0
    for i in tqdm.tqdm(range(5)):
        firstPlayer, secondPlayer = MiniMaxPlayer(), RandomPlayer()
        firstPlayer.setTypeOfAssignedMark(O_MARK), secondPlayer.setTypeOfAssignedMark(X_MARK)
        empty_state = np.array([
                   [' ', ' ', ' ', ' ', ' '], 
                   [' ', ' ', ' ', ' ', ' '], 
                   [' ', ' ', ' ', ' ', ' '], 
                   [' ', ' ', ' ', ' ', ' '], 
                   [' ', ' ', ' ', ' ', ' ']])
        
        # empty_state = np.array([
        #     [' ', ' '],
        #     [' ', ' ']])
        # empty_state = np.array([
        #     [' ', ' ', ' '],
        #     [' ', ' ', ' '],
        #     [' ', ' ', ' ']])
        firstPlayer.setStateOfGameField(empty_state)
        currentPlayer = firstPlayer
        currentState = empty_state
        while currentPlayer.check_if_player_won(currentState, X_MARK) == False and currentPlayer.check_if_player_won(currentState, O_MARK) == False:
            move = currentPlayer.makeMove()
            new_state = currentPlayer.simulate_state_after_move(currentState, move)
            if currentPlayer == firstPlayer:
                currentPlayer = secondPlayer
            else:
                currentPlayer = firstPlayer
            #print (currentState)
            currentState = new_state
            currentPlayer.setStateOfGameField(currentState)
            #print (move)
            #print (currentState)
        #print (currentPlayer.gameField)
        if currentPlayer.check_if_player_won(currentState, O_MARK):
            player_won += 1
        print (currentState)
    print ("player_won", str(player_won))
        
