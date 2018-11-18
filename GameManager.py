from AbstractPlayer import *
from RandomPlayer import *

class GameManager:
    firstPlayer, secondPlayer = RandomPlayer(), RandomPlayer()
    firstPlayer.setTypeOfAssignedMark(O_MARK), secondPlayer.setTypeOfAssignedMark(X_MARK)
    empty_state = np.array([
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ']])
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
        currentState = new_state
        currentPlayer.setStateOfGameField(currentState)
    print (currentPlayer.gameField)
