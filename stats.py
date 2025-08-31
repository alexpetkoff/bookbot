def get_words_count(book_text):
	return len(book_text.split())

def get_character_count(book_text):
	book_text_lowercase = book_text.lower()
	characters_dict = {}

	for char in book_text_lowercase:
		if char in characters_dict:
			characters_dict[char] += 1
		else:
			characters_dict[char] = 1

	return characters_dict

def sort_on(items):
	return items["num"]

def sort_dictionary(dict):
	dict_list = []

	for key in dict:
		dict_list.append({"char": key, "num": dict[key]})

	dict_list.sort(reverse=True, key=sort_on)
	return dict_list