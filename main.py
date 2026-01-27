from stats import get_num_words, get_letter_count

def get_book_text(filename):
	with open(filename) as f:
		file_contents = f.read()
		print(f"Found {get_num_words(file_contents)} total words")
		print(f"Found {get_letter_count(file_contents)} total letters")
		

def main():
	get_book_text("./books/frankenstein.txt")

main()
