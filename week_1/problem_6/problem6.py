#! /usr/bin/python3


# Global variable
result = []
v = ['c', 'a', 't', 'd', 'o', 'g']
cap = len(v)
m = [0] * cap
cnt = 0


def generateSubset(n):
	global cnt
	if n == cap:
		cnt += 1
		print('No {}: '.format(cnt), result)
	else:
		for i in range(cap):
			if m[i] == 1:
				continue
			else:
				m[i] = 1
				result.append(v[i])
				generateSubset(n + 1)
				m[i] = 0
				result.pop()

print('Start')
generateSubset(0)
