#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# Solves the Knight Tour problem using Backtracking
#
# ## #############################################################
import sys
from time import perf_counter, sleep

def knight_tour(n, x, y):
	'''
		Anchor for the Knight tour algorithm
	'''
	init_board(n)            # Initialize the N×N board
	board[x][y] = 1          # Start in x0, y0
	step = 1                 # This is the first step

	# Solve recursively with BackTracking
	return recursive_knight_tour(n, [x, y], step+1)
# end def



def recursive_knight_tour(n, move, step):
	'''
		Knight tour solving algorithm using Backtracking
	'''
	if step > n**2:
		return True          # Solution found!

	# Iterate over all valid moves
	for x, y in get_moves(n, move[0], move[1]):
		board[x][y] = step   # Assume this is a solution
		# print(f'Trying {step} on ({x}, {y})')
		if recursive_knight_tour(n, [x, y], step+1):
			return True      # Assumption was correct, solution found
		board[x][y] = -1     # Assumption was NOT correct, BACKTRACK!
	return False             # No solution was found in this branch.
# end def



def init_board(n):
	'''
		Initializes an N×N board
		Unvisited cells weight -1
	'''
	global board
	board = [ [ -1 for i in range(n) ] for i in range(n) ]
# end def



def get_moves(n, x0, y0):
	'''
		Gets all the valid moves from the (x0,y0) position in an N×N board
	'''
	kmoves = [ # All 8 knight moves
		(-2,  1), (-1,  2), ( 1,  2), ( 2,  1),
		( 2, -1), ( 1, -2), (-1, -2), (-2, -1)
	]
	for kmove in kmoves:
		x1 = x0 + kmove[0]
		y1 = y0 + kmove[1]
		# Discard moves out of the board
		if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
			continue
		# Skip visited cells
		if board[x1][y1] != -1:
			continue
		# Return this (and only this) move
		yield x1, y1
# end def



def print_board():
	'''
		Neatly prints the board
	'''
	for row in board:
		print( ' '.join([ str(cell).rjust(3) for cell in row]) )
# end def



def main(argv):
	n = 8
	x = 0
	y = 0
	try:
		n = int(argv[1])
		x = int(argv[2])
		y = int(argv[3])
	except:
		pass
	if x < 0 or x >= n:
		x = 0
	if y < 0 or y >= n:
		y = 0

	if knight_tour(n, x, y):
		print_board()
	else:
		print(f'Can\'t find a solution for a {n}×{n} board.')
	start = perf_counter()
	knight_tour(n, x, y)
	elapsed = perf_counter() - start
	print("Foo took {:.2f}ms".format(elapsed*1000))
# end def



if __name__ == "__main__":
	main(sys.argv)
