#Finds all the boxes in the Sudoku with a value of zero
def empty_box(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return (y, x)  # row, col

    return None

#Checks if there are any repeaded numbers in the rows, colomns and boxes
def correct(board, number, position):

    #Checks colomns
    for y in range(len(board)):
        if board[y][position[1]] == number and position[0] != y:
            return False

    #Checks rows
    for x in range(len(board[0])):
        if board[position[0]][x] == number and position[1] != x:
            return False

    #Checks boxs
    boxy = position[0] // 3
    boxx = position[1] // 3

    for y in range(boxy*3, boxy*3 + 3):
        for x in range(boxx * 3, boxx*3 + 3):
            if board[y][x] == number and (y,x) != position:
                return False

    return True

#Solves the Sudoku puzzle useing backtracking
def solution(board):
    empty = empty_box(board)
    if not empty:
        return True
    else:
        (y1, x1) = empty

    for i in range(1, 10):
        if correct(board, i, empty):
            board[y1][x1] = i

            if solution(board):
                return True

            board[y1][x1] = 0

    return False
