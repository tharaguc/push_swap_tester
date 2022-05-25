import sys
import randomArr
import error

args = sys.argv

def main():
	sum = 0
	error.check(args)
	num = int(args[1])
	for _ in range(100):
		res , ok_ko= randomArr.run(num)
		print(f"{res} >> {ok_ko}", end='')
		sum = sum + res
	print(f'Average: {sum / 100}')

if __name__ == "__main__":
	main()