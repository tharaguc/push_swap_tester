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
		res, ok_ko, psarg, leak = runPushSwap(num)
		print(f"[ {psarg} ]")
		if ok_ko == 'OK\n':
			print(f"{Color.CYAN}{res}{Color.RESET} >> {Color.GREEN}OK{Color.RESET}", end=' ')
		else:
			print(f"{res} >> {Color.RED}KO{Color.RESET}")
		if leak == 0:
			print(f"leak >> {Color.GREEN}OK{Color.RESET}", end="\n\n")
		else:
			print(f"leak >> {Color.RED}KO{Color.RESET}", end="\n\n")
		sum = sum + res
	print(f'Average: {Color.CYAN}{sum / rep}{Color.RESET}', end="\n\n")

if __name__ == "__main__":
	main()