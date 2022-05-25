import random
import subprocess

def run(n):
	l = list(range(n))
	random.shuffle(l)
	str_l = " ".join([str(n) for n in l])
	command1 = f"./push_swap {str_l} | wc -l | tr -d ' '"
	command2 = f"./push_swap {str_l} | ./checker_Mac {str_l}"
	count = subprocess.run(command1, shell=True, capture_output=True, text=True)
	ok_ko = subprocess.run(command2, shell=True, capture_output=True, text=True)
	return int(count.stdout), ok_ko.stdout