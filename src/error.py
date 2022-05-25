USAGE = "Usage: python3 main.py [Number]"

def argCheck(args):
	if len(args) != 2:
		errExit(USAGE)
	if args[1].isnumeric() == False:
		errExit(USAGE)

def errExit(msg):
	print(msg)
	exit()