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

def hanoi(disks, src=1, dest=2, aux=3):
	if disks > 0:
		# Mueve n-1 discos del origen (src) al auxiliar
		# usando destino como poste intermedio
		hanoi(disks-1, src, aux, dest)

		# Mueve un disco del origen al destino
		print("Mueve disco D{} de P{} a P{}".format(disks, src, dest))

		# Mueve n-1 discos del auxiliar al destino
		# usando origen (src) como poste intermedio
		hanoi(disks-1, aux, dest, src)

def main(argv):
	n = int(argv[1]) if len(argv) > 1 else 3
	hanoi(n)

if __name__ == "__main__":
	main(sys.argv)
