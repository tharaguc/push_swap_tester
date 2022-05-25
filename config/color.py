class Color:
	RED = '\033[31m'
	GREEN = '\033[32m'
	CYAN = '\033[36m'
	RESET = '\033[0m'

def green(msg):
	return f"{Color.GREEN}{msg}{Color.RESET}"

def red(msg):
	return f"{Color.RED}{msg}{Color.RESET}"

def cyan(msg):
	return f"{Color.CYAN}{msg}{Color.RESET}"