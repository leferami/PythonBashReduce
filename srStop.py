#!/usr/bin/env python
# Pass an object through a queue to another process
import numpy 
import time
import sys
import re
from datetime import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
worktime = 0
startTime = time.time()
i = 0
for line in sys.stdin:
	if(len(line)!=1):
		words = word_tokenize(line)
		filtered_sentence = []
		for w in words:
			if w not in stop_words:
				filtered_sentence.append(w)
		endTime = time.time()
		worktime = endTime - startTime
		print worktime
