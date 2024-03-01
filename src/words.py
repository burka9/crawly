import re
from lib import extract_amharic_words
from db import search_word


def init_words(filename):
  # load file
	with open(filename, "r", encoding="utf8") as f:
		for line in f:
			for word in re.split(r'\s+', line):
				try:
					search_word.save(word, False)
					print(f'{word} saved')
				except Exception as ex:
					print(ex)
					pass
   
	print("init done!")


def list_words():
	words = search_word.find_all()
 
	print(search_word.collection.find())

	if not words:
		print("No words found")
		return None
 
	for word in words:
		print(word['word'])