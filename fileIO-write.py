def main():
	f=open("myFile.txt", "w")
	for i in range(4):
		f.write(input("enter a word: ") + '\n')
	f.close()

if __name__ == "__main__":
	main()
