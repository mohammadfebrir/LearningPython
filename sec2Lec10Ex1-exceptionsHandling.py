def main():
	try:
		f=open("blah.txt", "r")
		for line in f:
			print(line.strip("\n\r"))
		f.close()
	except:
		print("file not found")

if __name__ == "__main__":
	main()
