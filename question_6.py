
def find_unique_words_in_file(filename):
	unique_words = []
	seen_words = []
	words = []

	with open(filename, 'r') as file:
		words = file.read().split()
	
	for word in words:
		if word in seen_words:
			if word in unique_words:
				unique_words.remove(word)
		else:
			unique_words.append(word)
			seen_words.append(word)

	return sorted(unique_words)


if __name__ == '__main__':
	filename = input("Enter filename: ")
	print("Unique words: %s" % ' '.join(find_unique_words_in_file(filename)))

