#! /usr/bin/python3
import numpy as np


def mean_var_stddev(sequence):
	mean = np.mean(sequence)
	var = np.var(sequence)
	stddev = np.std(sequence)
	return mean, var, stddev


print('Start.....')
seq = input('Enter a list: ')
seq = [int(x) for x in seq.split()]
mean, var, std_dev = mean_var_stddev(seq)
print('Result is:')
print('\tmean\t{:.3f}'.format(mean))
print('\tvar\t{:.3f}'.format(var))
print('\tstd_dev\t{:.3f}'.format(std_dev))
