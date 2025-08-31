import sys
from stats import get_words_count
from stats import get_character_count
from stats import sort_dictionary

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():

	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_text = get_book_text(sys.argv[1])
	words_count = get_words_count(book_text)
	character_dict = get_character_count(book_text)
	sorted_dict = sort_dictionary(character_dict)


	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {words_count} total words")
	print("--------- Character Count -------")

	for el in sorted_dict:
		print(f"{el["char"]}: {el["num"]}")

	print("============= END ===============")

if __name__ == "__main__":
    main()
