import sys
sys.dont_write_bytecode = True

from src.runPush_swap import runPushSwap
from src.error import argCheck
from config.color import Color

args = sys.argv

def main():
	argCheck(args)
	num, rep = int(args[1]), int(args[2])
	sum = 0
	for _ in range(rep):
		res , ok_ko, psarg = runPushSwap(num)
		print(f"[ {psarg} ]")
		if ok_ko == 'OK\n':
			print(f"{Color.CYAN}{res}{Color.RESET} >> {Color.GREEN}{ok_ko}{Color.RESET}")
		else:
			print(f"{res} >> {Color.RED}{ok_ko}{Color.RESET}")
		sum = sum + res
	print(f'Average: {Color.CYAN}{sum / rep}{Color.RESET}', end="\n\n")

if __name__ == "__main__":
	main()