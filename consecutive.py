## https://coderbyte.com/results/gvargo:Consecutive:Python3 ##
from termcolor import colored


def Consecutive(arr):
	# code goes here
	# print(f'arr is of {type(arr)}')
	
	arrmax = sorted(arr)[-1]
	arrmin = sorted(arr)[0]
	
	# print(f'arrmax = {arrmax}')
	# print(f'arrmin = {arrmin}')
	
	m = [x for x in range(arrmin, arrmax + 1)]
	# print(m)
	
	return abs(arr.__len__() - m.__len__())


if __name__ == "__main__":
	# keep this function call here
	s = [int(x) for x in input().strip()[1:-1].split(sep=',')]
	print(colored(s, color='green'))
	print(Consecutive(s))
