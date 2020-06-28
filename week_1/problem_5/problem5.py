#! /usr/bin/python3
import math


def norm(v, p=2):
	n = 0.0
	for it in v:
		n += it**p

	return n**(1.0/p)


list_input = input('Enter a list of number: ')
v = [int(x) for x in list_input.split()]
p = int(input('Enter p: '))
print('norm({}, {}) is {:.2f}'.format(v, p, norm(v, p)))
print('norm({}) is {:.2f}'.format(v, norm(v)))
