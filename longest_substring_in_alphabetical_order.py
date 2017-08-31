
def longest_substring_in_alphabetical_order(string):
	longest_substring = string[0]
	substring = string[0]

	for index in range(1, len(string)):
		if ord(string[index - 1]) <= ord(string[index]):
			substring += string[index]
		else:
			if len(substring) > len(longest_substring):
				longest_substring = substring
			substring = string[index]

	return longest_substring


if __name__ == '__main__':
	string = raw_input("Enter string: ")
	print longest_substring_in_alphabetical_order(string)
