def getInteger(prompt):
	result = int(input(prompt))
	return result

def main():
	print("started")
	output = getInteger("please enter an integer: ")
	output2 = getInteger("please enter another integer: ")
	print(output)

if __name__ == "__main__":
	main()
