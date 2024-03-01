import re
from langid import classify

def split_text(sentence) -> [str]:
  return re.split(r'\W+', sentence)

def is_word_amharic(word):
  return classify(word)[0] == 'am'

def is_sentence_amharic(sentence) -> [bool, float]:
    words = split_text(sentence)
    _is = 0

    for word in words:
        if is_word_amharic(word):
            _is += 1

    _is = _is / len(words)

    return _is > 0.5, _is

def extract_amharic_words(text) -> [str]:
  words = []

  for word in split_text(text):
    if is_word_amharic(word):
      words.append(word)
    
  return words
