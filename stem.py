from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in  example_words:
	print(ps.stem(w))

new_text = "It is very important to be pythonly while your are pythoning. All pythoners have pythoned poorly"

words = word_tokenize(new_text)

for w in  words:
	print(ps.stem(w))