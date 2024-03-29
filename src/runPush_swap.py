import random
import subprocess

def runPushSwap(n):
	l = list(range(n))
	random.shuffle(l)
	str_l = " ".join([str(n) for n in l])
	command1 = f"./bin/push_swap {str_l} | wc -l | tr -d ' '"
	command2 = f"./bin/push_swap {str_l} | ./bin/checker_Mac {str_l}"
	command3 = f"leaks -noContent -q --atExit -- ./bin/push_swap {str_l}"
	count = subprocess.run(command1, shell=True, capture_output=True, text=True)
	ok_ko = subprocess.run(command2, shell=True, capture_output=True, text=True)
	leak = subprocess.run(command3, shell=True, stdout=subprocess.DEVNULL)
	return int(count.stdout), ok_ko.stdout, str_l, leak.returncode