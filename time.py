#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################

from time import perf_counter, sleep

def foo():
	sleep(1)

def main():
	start = perf_counter()
	foo()
	elapsed = perf_counter() - start
	print("Foo took {:.2f}ms".format(elapsed*1000))


if __name__ == '__main__':
	main()
