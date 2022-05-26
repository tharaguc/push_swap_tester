import sys
sys.dont_write_bytecode = True

from src.runPush_swap import runPushSwap
from src.error import argCheck
from config.color import green, red, cyan

args = sys.argv

def main():
	argCheck(args)
	num, rep = int(args[1]), int(args[2])
	sum, max = 0, 0
	for i in range(rep):
		res, ok_ko, psarg, leak = runPushSwap(num)
		if i == 0:
			min = res
		if res > max:
			max = res
		if res < min:
			min = res
		print(f"[ {psarg} ]", end="\n-------------\n")
		if ok_ko == 'OK\n':
			print(f">> Actions: {cyan(res)}, Checker: {green('OK')},", end=' ')
		else:
			print(f">> Actions: {cyan(res)}, Checker: {red('KO')},", end=' ')
		if leak == 0:
			print(f"Leak: {green('OK')}", end="\n=============\n\n")
		else:
			print(f"Leak: {red('KO')}", end="\n=============\n\n")
		sum = sum + res
	print(f'Max    : {cyan(max)}')
	print(f'Average: {cyan(sum / rep)}')
	print(f'Min    : {cyan(min)}', end='\n\n')

if __name__ == "__main__":
	main()