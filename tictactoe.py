"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    else:
        xc = 0
        oc = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    xc+=1
                if board[i][j] == O:
                    oc+=1
        if oc + xc == 9:
            return None
        if xc > oc:
            return O
        if xc == oc:
            return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a = set()
    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                a.add((i,j))
    return a

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    if type(action) == tuple:
        if board[action[0]][action[1]] != EMPTY:
            print(action)
            raise Exception('Invalid action')
        else:
            m = copy.deepcopy(board)
            m[action[0]][action[1]] = turn
            return m
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == None:
                continue
            else:
                return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == None:
                continue
            else:
                return board[1][i]
            
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if player(board) == None or winner(board) != None:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    alpha = -math.inf
    beta = math.inf
    if terminal(board):
        return utility(board),None
    turn = player(board)
    if board == initial_state():
        move = (0,1)
        return None,move
    if turn == O:
        if terminal(board):
            return utility(board),None
        v = math.inf
        for action in actions(board):
            x = minimax(result(board,action))[0]
            if x < v:
                v = x
                move = action
            if v == -1:
                return v,move
            beta = min(beta,v)
            if beta <= alpha:
                break
        return v, move
    if turn == X:
        if terminal(board):
            return utility(board),None
        v = -math.inf
        for action in actions(board):
            x = minimax(result(board,action))[0]
            if x > v:
                v = x
                move = action
            if v == 1:
                return v,move
            alpha = max(alpha,v)
            if beta <= alpha:
                break
        return v, move
        















                
    
