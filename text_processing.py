#text_processing.py

def getKeyCharacter():
	keyChar = input('Please enter a single character to act as a key: ')
	while len(keyChar) != 1:
		print("Error. You have exceeded the character limit.")
		keyChar = input('Please enter a SINGLE character to act as a key: ')
	return keyChar

def getString():
	userString = input('Please enter a phrase/sentence >= 4 and <= 500 characters: ')
	while len(userString) < 4 or len(userString) > 500:
		print("Error. You have exceeded the character limit.")
		userString = input('Please enter a phrase/sentence >= 4 and <= 500 characters: ')
	return userString

def maskCharacter(theString, keyCharacter):
	newString = ""
	for char in theString:
		if char == keyCharacter:
			char = '*'
		newString = newString + char
	return newString

def removeCharacter(theString, keyCharacter):
	newString = ""
	for char in theString:
		if char != keyCharacter:
			newString = newString + char
	return newString

def countKey(theString, keyCharacter):
	count = 0
	for char in theString:
		if char == keyCharacter:
			count = count + 1
	return count	

keyCharacter = getKeyCharacter()
targetString = getString()
maskString = maskCharacter(targetString, keyCharacter)
removeString = removeCharacter(targetString, keyCharacter)
occurChar = countKey(targetString, keyCharacter)


print('String with key character masked: ', maskString)
print('String with key character removed: ', removeString)
print('# of occurrences of key character: ', occurChar)


#
# Run 1:
# Please enter a single character to act as a key: e
# Please enter a phrase/sentence >= 4 and <= 500 characters: The headphones fell from the sky and dropped to the ground.
# String with key character masked:  Th* h*adphon*s f*ll from th* sky and dropp*d to th* ground.
# String with key character removed:  Th hadphons fll from th sky and droppd to th ground.
# # of occurrences of key character:  7

# Run 2:
# Please enter a single character to act as a key: s
# Please enter a phrase/sentence >= 4 and <= 500 characters: This too shall pass.
# String with key character masked:  Thi* too *hall pa**.
# String with key character removed:  Thi too hall pa.
# # of occurrences of key character:  4

# Run 3:
# Please enter a single character to act as a key: e
# Please enter a phrase/sentence >= 4 and <= 500 characters: The best is yet to come.
# String with key character masked:  Th* b*st is y*t to com*.
# String with key character removed:  Th bst is yt to com.
# # of occurrences of key character:  4

#
# Please enter a single character to act as a key: ee
# Error. You have exceeded the character limit.
# Please enter a SINGLE character to act as a key: ee
# Error. You have exceeded the character limit.
# Please enter a SINGLE character to act as a key: aa
# Error. You have exceeded the character limit.
# Please enter a SINGLE character to act as a key: i
# Please enter a phrase/sentence >= 4 and <= 500 characters: hi
# Error. You have exceeded the character limit.
# Please enter a phrase/sentence >= 4 and <= 500 characters: hi
# Error. You have exceeded the character limit.
# Please enter a phrase/sentence >= 4 and <= 500 characters: rad
# Error. You have exceeded the character limit.
# Please enter a phrase/sentence >= 4 and <= 500 characters: Imagination
# String with key character masked:  Imag*nat*on
# String with key character removed:  Imagnaton
# # of occurrences of key character:  2
#