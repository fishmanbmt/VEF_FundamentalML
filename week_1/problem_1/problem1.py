#! /usr/bin/python3


def inputElement():
	n = input('\tEnter number: ')
	if not n.isnumeric():
		print('\t-> Invalid input, input must be a number')
		n = input('\tEnter number: ')

	return int(n)


def findMinMax(a):
	min_val = max_val = a[0]
	for it in a:
		if min_val > it:
			min_val = it
		if max_val < it:
			max_val = it

	return min_val, max_val


print('Input length of list')
n = inputElement()

print('-' * 30)
print('Input each element')
a = []
for i in range(n):
	print('intput a[{}]'.format(i))
	a.append(inputElement())

print('-' * 30)
print('Find min and max value')
if len(a) == 0:
	print('\tList is empty')
	exit(1)

min_val, max_val = findMinMax(a)
print('\tmin value is {}'.format(min_val))
print('\tmax value is {}'.format(max_val))


