#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ################################################################
#
# Author: Mauricio Matamoros
#
# Checks whether the given strings are palindromes
#
# ## ################################################################
import sys

def palindrome(s):
	i = 0
	j = len(s)-1
	while i < j:
		if s[i] != s[j]:
			return False
		i+=1
		j-=1
	return True
# end def


def main(argv):
	for s in argv[1:]:
		print("'{}' {} palíndromo.".format(
			s,
			"es" if palindrome(s) else "no es"
		))
# end def

if __name__ == "__main__":
	main(sys.argv)