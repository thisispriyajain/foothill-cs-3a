'''
* Program #4: A Triple String Class
* Programmer: Priya Jain
* Due: July 27, 2020
* CS 3A, Summer 2020
* Description: This assignment should test for valid strings. 
'''

class TripleString:
	MIN_LEN = 1
	MAX_LEN = 50
	DEFAULT_STRING = "(undefined)"

	#Constructor #1
	def TripleString(self):
		self.string1 = self.DEFAULT_STRING
		self.string2 = self.DEFAULT_STRING
		self.string3 = self.DEFAULT_STRING
 
	#Constructor #2
	def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING, string3 = DEFAULT_STRING):
		self.string1 = self.DEFAULT_STRING
		self.string2 = self.DEFAULT_STRING
		self.string3 = self.DEFAULT_STRING

		self.set_string1(string1)
		self.set_string2(string2)
		self.set_string3(string3)

	def set_string1(self, string1):
		if self.valid_string(string1):
			self.string1 = string1
			return True
		else:
			return False

	def set_string2(self, string2):
		if self.valid_string(string2):
			self.string2 = string2
			return True
		else:
			return False

	def set_string3(self, string3):
		if self.valid_string(string3):
			self.string3 = string3
			return True
		else:
			return False

	def get_string1(self):
		return 'String 1 is: ' + self.string1

	def get_string2(self):
		return 'String 2 is: ' + self.string2

	def get_string3(self):
		return 'String 3 is: ' + self.string3

	def valid_string(self, the_str):
		if(len(the_str) >= self.MIN_LEN and len(the_str) <= self.MAX_LEN):
			return True
		else:
			return False

	def to_string(self):
		return 'String 1: ' + self.string1 + ", " + 'String 2: ' + self.string2 + ", " + 'String 3: ' + self.string3

TripleString_One = TripleString()
TripleString_Two = TripleString("Python")
TripleString_Three = TripleString("Foothill", "College")
TripleString_Four = TripleString("Object", "Oriented", "Programming")

print(TripleString_One.to_string())
print(TripleString_Two.to_string())
print(TripleString_Three.to_string())
print(TripleString_Four.to_string())

TripleString_One.set_string1("C")
TripleString_One.set_string2("C#")
TripleString_One.set_string3("C++")

TripleString_Two.set_string1("Mountain View")
TripleString_Two.set_string2("High")
TripleString_Two.set_string3("School.")

TripleString_Three.set_string1("Santa")
TripleString_Three.set_string2("Clara")
TripleString_Three.set_string3("University")

TripleString_Four.set_string1("Los Altos")
TripleString_Four.set_string2("Los Altos Hills")
TripleString_Four.set_string3("Mountain View")

print(TripleString_One.to_string())
print(TripleString_Two.to_string())
print(TripleString_Three.to_string())
print(TripleString_Four.to_string())

resultOne = TripleString_One.set_string1("")

if(resultOne):
	print('The string was updated sucessfully.')
else:
	print('The string could not be updated.')

resultTwo = TripleString_Two.set_string1("Los Altos Hills")

if(resultTwo):
	print('The string was updated sucessfully.')
else:
	print('The string could not be updated.')

print(TripleString_One.get_string1())
print(TripleString_Two.get_string1())


#
# String 1: (undefined), String 2: (undefined), String 3: (undefined)
# String 1: Python, String 2: (undefined), String 3: (undefined)
# String 1: Foothill, String 2: College, String 3: (undefined)
# String 1: Object, String 2: Oriented, String 3: Programming
# String 1: C, String 2: C#, String 3: C++
# String 1: Mountain View, String 2: High, String 3: School.
# String 1: Santa, String 2: Clara, String 3: University
# String 1: Los Altos, String 2: Los Altos Hills, String 3: Mountain View
# The string could not be updated.
# The string was updated sucessfully.
# String 1 is: C
# String 1 is: Los Altos Hills
#







