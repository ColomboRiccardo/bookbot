def get_num_words(content):
	return len(content.split())

def get_letter_count(content):
	letter_dict = {}
	for letter in content:
		if letter == " ":
			pass
		if letter.lower() in letter_dict:
			letter_dict[letter.lower()] += 1
		else:
			letter_dict[letter.lower()] = 1
	return letter_dict