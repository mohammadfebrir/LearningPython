import math

def main():
	try:
		number = float(input("please enter a number: "))
		number = math.fabs(number)
		print(number)

	except:
		print("you didn enter a number")

if __name__ == "__main__":
	main()
