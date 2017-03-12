def main():
	f=open("myFile.txt", "r")
	for line in f:
		print(line.strip("\n\r"))
	f.close()

if __name__ == "__main__":
	main()
