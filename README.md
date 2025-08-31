# BookBot 📚🤖

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a simple Python program that analyzes a text file (such as a book) and reports statistics like:

Total word count

Character frequency (sorted)

## 🚀 Features

Reads in any .txt file

Counts the total number of words

Counts the frequency of each character (letters, numbers, symbols)

Sorts character counts for easier readability

Prints results in a clean, formatted way

## 📦 Installation

Clone this repository:

git clone https://github.com/alexpetkoff/bookbot
cd bookbot

Make sure you have Python 3 installed.

## ▶️ Usage

Run the script with a path to a text file:

python3 main.py books/frankenstein.txt

Example output:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78,566 total words
--------- Character Count -------
a: 4500
b: 1234
c: 2345
...
============= END ===============
```

## 🛠 Project Structure

```
.
├── main.py # Entry point
├── stats.py # Helper functions for stats
└── README.md # This file
```

## 📚 How it works

get_book_text(filepath) → Reads the entire book into memory

get_words_count(text) → Counts words in the text

get_character_count(text) → Counts characters and stores them in a dictionary

sort_dictionary(dict) → Sorts the dictionary for easy display

## ✅ Example Books to Try

Project Gutenberg
has thousands of free .txt books you can analyze.
