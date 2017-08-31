
def longest_substring_in_alphabetical_order(string):
	longest_substring = string[0]
	substring = string[0]

	for index in range(1, len(string)):
		if is_alphabetical(string[index - 1], string[index]):
			substring += string[index]
		else:
			if len(substring) > len(longest_substring):
				longest_substring = substring
			substring = string[index]

	return longest_substring
		

def is_alphabetical(character_one, character_two):
	if ord(character_one) <= ord(character_two):
		return True
	return False


if __name__ == '__main__':
	string = raw_input("Enter string: ")
	print longest_substring_in_alphabetical_order(string)
