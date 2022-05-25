USAGE = "Usage: python3 main.py [ Number of arguments for push_swap] [ Number of repetitions ]"

def argCheck(args):
	if len(args) != 3:
		errExit(USAGE)
	if args[1].isnumeric() == False:
		errExit(USAGE)
	if args[2].isnumeric() == False:
		errExit(USAGE)

def errExit(msg):
	print(msg)
	exit()