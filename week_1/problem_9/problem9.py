#! /usr/bin/python3
import numpy as np

def multiply(a, b):
	return np.dot(a, b)


print('Start....')
print('Generate a')
a = np.random.rand(3,2)
print(a)

print('Generate b')
b = np.random.rand(2,2)
print(b)

print('Result is:')
print(multiply(a, b))

