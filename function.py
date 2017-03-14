def getInteger(prompt):
	result = int(input (prompt))
	return result

def Main():
	print("LEARNING PYTHON - FUNCTION")
	output = getInteger("Please enter an integer: ")
	print(output)

if __name__ == "__main__":
	Main()