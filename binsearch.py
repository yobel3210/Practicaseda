#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ################################################################
#
# Author: Mauricio Matamoros
#
# Implements binary search of a given key in a random array
#
# ## ################################################################
import sys
from random import sample, seed

h = 0
def binsearch(key, A, l, r):
	global h
	h+=1

	################################################
	#
	# Student's code here!
	#
	################################################
# end def

def main(argv):
	# Generate random array A
	seed(69)
	limit = int(argv[2]) if len(argv) > 2 else 10000
	A = sorted(sample(range(0, limit*10), limit))

	# Fetch key
	key = int(argv[1]) if len(argv) > 1 else 69

	print("Searching for {} in A (n={})".format(key, len(A)-1))
	result = binsearch(key, A, 0, len(A))
	if result != -1:
		print("{} found at position {} ({})".format(key, result, A[result-2:result+3]))
	else:
		print("{} not found".format(key))
	print("h =", h)

if __name__ == "__main__":
	main(sys.argv)
