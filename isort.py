#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################

import sys
from random import randint, seed
from time import perf_counter

def swap(A, i, j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp
# end def


def insertionsort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j-1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i-=1
		A[i+1] = key
# end def


def main(argv):
	seed(69)
	n = int(argv[1]) or 100
	A = [randint(-n, n+1) for i in range(n)]
	# print(A)
	start = perf_counter()
	insertionsort(A)
	elapsed = perf_counter() - start
	# print(A)
	print("Insertion sort time {:.2f}ms".format(elapsed*1000))


if __name__ == '__main__':
	main(sys.argv)
