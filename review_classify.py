import sys
import string
from itertools import izip

file_dir = './imdb/'

spaces = " "*len(string.punctuation)

dictionary = {}

train_data = []

with open(file_dir + 'imdb_test_text.txt', 'r') as a:
	dict_limit = 0
	for line in a:
		line = line.translate(string.maketrans(string.punctuation, spaces))
		l = []
		for word in line.split(' '):
			if len(word) > 1:
				l.append(word)
				dictionary[word] = dict_limit
				dict_limit += 1
		train_data.append(l)

print 'length of dictionary ' + str(len(dictionary))

train_list = []

with open(file_dir + 'imdb_test_labels.txt', 'r') as a:
	ind = 0
	for line in a:
		label = int(line)
		l = []
		for word in train_data[ind]:
			l.append(dictionary[word])
		train_list.append(l, label)

print len(train_list)

