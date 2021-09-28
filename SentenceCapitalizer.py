#SentenceCapitalizer.py

def capitalSentence(string):
	string = string.split(".")
	for i in string:
		print(i.strip().capitalize(), ".", end = '')
	return string

user_string = input('Enter a sentence you would like capitalized: ')
print(capitalSentence(user_string))