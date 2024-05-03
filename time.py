#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: modified by Yobel Dolores
#
# ## #############################################################
import sys
from time import perf_counter, sleep

def foo():
	sleep(1)

def fact(n):
	return 1 if n <= 1 else n * fact(n-1)

def main(argv):
	start = perf_counter()
	n = int(argv[1])
	fact(n)
	#foo()
	elapsed = perf_counter() - start
	print("Foo took {:.2f}ms".format(elapsed*1000))


if __name__ == '__main__':
	main(sys.argv)
