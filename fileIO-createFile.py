def main():
	words = ['cat','bat','hat','sat','1','2','3']

	with open("words.txt", 'w') as f:
		for word in words:
			f.write(word + "\n")

if __name__ == "__main__":
	main()
