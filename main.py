from stats import get_num_words, get_letter_count, sort_letter_dict
import sys

def get_book_text(filename):
	with open(filename) as f:
		file_contents = f.read()
		# print(f"Found {get_num_words(file_contents)} total words")
		# print(f"Found {get_letter_count(file_contents)} total letters")
		letters_dict = get_letter_count(file_contents)
		sorted_letters_dict = sort_letter_dict(letters_dict)

		result_to_print = ""

		for letter in sorted_letters_dict:
			result_to_print += f"{letter["char"]}: {letter["num"]}\n"

		print(f"""
		============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {get_num_words(file_contents)} total words
--------- Character Count -------
{result_to_print}
============= END ===============
		""")
		

def main():
	if len(sys.argv) >= 2:
		get_book_text(sys.argv[1])
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

main()
