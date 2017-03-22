import math

def main():
	try:
		radius = float(input("please enter a radius: "))
		area = math.pi * radius**2
		print("area = ",area)

	except:
		print("you didn enter a number")

if __name__ == "__main__":
	main()
