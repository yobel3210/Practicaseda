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


def quicksort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quicksort(A, p, q-1)
		quicksort(A, q+1, r)
# end def


def partition(A, p, r):
	x = A[r]
	i = p-1
	for j in range(p, r):
		if A[j] <= x:
			i+= 1
			swap(A, i, j)
	swap(A, i+1, r)
	return i+1
# end def


def main(argv):
	seed(69)
	n = int(argv[1]) or 100
	A = [randint(-n, n+1) for i in range(n)]
	# print(A)
	start = perf_counter()
	quicksort(A, 0, len(A)-1)
	elapsed = perf_counter() - start
	# print(A)
	print("Quicksort time {:.2f}ms".format(elapsed*1000))


if __name__ == '__main__':
	main(sys.argv)
