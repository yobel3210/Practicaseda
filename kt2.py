#! /usr/bin/env python3

import sys

def knight_tour(n, x, y):
    init_board(n)
    board[x][y] = 1
    step = 1
    return recursive_knight_tour(n, [x, y], step+1)

def recursive_knight_tour(n, move, step):
    if step > n**2:
        return True
    for x, y in get_moves(n, move[0], move[1]):
        board[x][y] = step
        if recursive_knight_tour(n, [x, y], step+1):
            return True
        board[x][y] = -1
    return False

def init_board(n):
    global board
    board = [ [ -1 for i in range(n) ] for i in range(n) ]

def get_moves(n, x0, y0):
    kmoves = [(-2,  1), (-1,  2), ( 1,  2), ( 2,  1), ( 2, -1), ( 1, -2), (-1, -2), (-2, -1)]
    for kmove in kmoves:
        x1 = x0 + kmove[0]
        y1 = y0 + kmove[1]
        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
            continue
        if board[x1][y1] != -1:
            continue
        yield x1, y1

def print_board():
    for row in board:
        print( ' '.join([ str(cell).rjust(3) for cell in row]) )

def main():
    n = 5
    results = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if knight_tour(n, x, y):
                results[x][y] = 1
            else:
                results[x][y] = 0
    for row in results:
        print(row)

if __name__ == "__main__":
    main()
