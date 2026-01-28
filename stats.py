
def get_num_words(content):
	return len(content.split())

def get_letter_count(content):
	letter_dict = {}
	for letter in content:
		if not letter.isalpha():
			continue
		if letter.lower() in letter_dict:
			letter_dict[letter.lower()] += 1
		else:
			letter_dict[letter.lower()] = 1
	return letter_dict

def sort_letter_dict(letter_dict):
	result_list = []
	for char, num in letter_dict.items():
		result_list.append({"char": char, "num": num})
	result_list.sort(reverse=True, key=sort_on)
	return result_list

def sort_on(items):
	return items["num"]