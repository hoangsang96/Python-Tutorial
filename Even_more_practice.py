#Even more practice
def break_words(stuff):
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""sort the words"""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after popping it off """
	word = words.pop(0)
	print(word)

def print_last_word(words):
	""" Print the last word """
	word = words.pop(-1)
	print(word)

def sort_sentences(sentences):
	""" Take in a full sentences and return the sorted words"""
	words = break_words(sentences)
	return sort_words(words)

def print_first_and_last_sentences(sentences):
	words = break_words(sentences)
	print_first_word(words)
	print_last_word(words)

s = "hello i am there"
words = break_words(s)

print(words)
print(sort_words(words))

print("The first word is : ")
print_first_word(words)

print("The last word is : ")
print_last_word(words)

print("Sort the full sentencess : ", sort_sentences(s))
print_first_and_last_sentences(s)