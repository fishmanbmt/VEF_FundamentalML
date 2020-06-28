#! /usr/bin/python3


def findMinMax(a):
	min_val = max_val = a[0]
	for it in a:
		if min_val > it:
			min_val = it
		if max_val < it:
			max_val = it

	return min_val, max_val


seq_numbers = input('Enter a list of number: ')
a = [int(x) for x in seq_numbers.split()]

print('-' * 30)
print('Find min and max value')
if len(a) == 0:
	print('\tList is empty')
	exit(1)

min_val, max_val = findMinMax(a)
print('\tmin value is {}'.format(min_val))
print('\tmax value is {}'.format(max_val))


