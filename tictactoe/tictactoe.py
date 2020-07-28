"""
Tic Tac Toe Player
"""

import math

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
    if terminal(board) is True:
        return X
    else:
        xcount = 0
        ocount = 0
        for a in range(3):
            for b in range(3):
                if board[a][b] is not EMPTY:
                    if board[a][b] is X:
                        xcount = xcount + 1
                    else:
                        ocount = ocount + 1
        if xcount - ocount <= 0:
            return X
        else:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moveSet = []
    if terminal(board) is True:
        return X
    else:
        for a in range(3):
            for b in range(3):
                if board[a][b] is EMPTY:
                    moveSet.append((a, b))
    return moveSet


def result(board, action):

    import copy

    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy = copy.deepcopy(board)
    if action is not None:
        if copy[action[0]][action[1]] is not EMPTY:
            raise "Illegal Move!"
        else:
            if player(board) is X:
                copy[action[0]][action[1]] = X
            else:
                copy[action[0]][action[1]] = O
    return copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[0][1] == board[0][2] == X:
        return X
    elif board[0][0] == board[1][0] == board[2][0] == X:
        return X
    elif board[1][0] == board[1][1] == board[1][2] == X:
        return X
    elif board[2][0] == board[2][1] == board[2][2] == X:
        return X
    elif board[0][1] == board[1][1] == board[2][1] == X:
        return X
    elif board[0][2] == board[1][2] == board[2][2] == X:
        return X
    elif board[2][0] == board[1][1] == board[0][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    elif board[0][0] == board[0][1] == board[0][2] == O:
        return O
    elif board[0][0] == board[1][0] == board[2][0] == O:
        return O
    elif board[1][0] == board[1][1] == board[1][2] == O:
        return O
    elif board[2][0] == board[2][1] == board[2][2] == O:
        return O
    elif board[0][1] == board[1][1] == board[2][1] == O:
        return O
    elif board[0][2] == board[1][2] == board[2][2] == O:
        return O
    elif board[2][0] == board[1][1] == board[0][2] == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    count = 0
    for a in range(3):
        for b in range(3):
            if board[a][b] is not EMPTY:
                count = count + 1
    if count == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None
    elif player(board) is X:
        evals = []
        for move in actions(board):
            evals.append(min_value(result(board, move)))
        return actions(board)[evals.index(max(evals))]
    else:
        evals = []
        for move in actions(board):
            evals.append(max_value(result(board, move)))
        return actions(board)[evals.index(min(evals))]


def max_value(board):
    if terminal(board) is True:
        return utility(board)
    v = -math.inf
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v


def min_value(board):
    if terminal(board) is True:
        return utility(board)
    v = math.inf
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v
