def main():
	words = ['cat','bat','hat','sat']

	with open("words.txt", 'w') as f:
		for word in words:
			f.write(word + "\n")

if __name__ == "__main__":
	main()
