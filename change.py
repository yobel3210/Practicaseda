#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################

import sys
coins = {
 	0.1 : 3,
 	0.2 : 3,
 	0.5 : 2,
 	  1 : 0,
 	  2 : 3,
 	  5 : 0,
 	 10 : 3,
 	 20 : 3,
 	 50 : 3,
 	100 : 3,
 }

def change(amount):
	coin_keys = sorted(coins.keys(), reverse=True)
	my_change = {coin: 0 for coin in coins}
	for coin in coin_keys:
		while amount >= coin and coins[coin]>0:
			amount -= coin
			my_change[coin] += 1
			coins[coin] -= 1
		if amount ==0:
			break
	return my_change
# end def


def main(argv):
	amount = float(argv[1])
	print("Cambio de", amount, "en:")
	for (coin, num) in sorted(change(amount).items(), reverse=True):
		if not num:
			continue
		print(num,
			"moneda" if num == 1 else "monedas",
			"de",
			coin if coin >= 1 else coin * 10,
			"pesos" if coin >= 1 else "centavos")

# end def


if __name__ == '__main__':
	main(sys.argv)
