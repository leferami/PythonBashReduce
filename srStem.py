#!/usr/bin/env python
# Pass an object through a queue to another process
import time
import sys
import re
from datetime import datetime
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
for line in sys.stdin:
	if(len(line)!=1):
		words = word_tokenize(line)
		for w in words:
			print(ps.stem(w))
			