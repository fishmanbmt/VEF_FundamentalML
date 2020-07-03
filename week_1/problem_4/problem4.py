#! /usr/bin/python3


def count_vowel(s):
	vowels = ['u', 'e', 'o', 'a', 'i']
	ret = 0
	for i in s:
		if i in vowels:
			ret += 1

	return ret


msg = input('Enter a String: ')
print('The number of vowels : {}'.format(countVowel(msg)))
