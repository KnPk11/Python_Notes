			### MODULES ###

# modules - import extra functionality
	import random # whole module
	print(random.randint(1, 10))
	
	from random import randint # specific functions
	print(randint(1, 10))
	
	from random import randint as dice # specific functions with a custom name
	print(dice(1, 6))
	
		# importing modules to Python
		pip install module_name
		
			### ELEMENTARY COMMANDS ###
			
# print - output text to console
	print('text')
	
# r'' - treat text as raw
	print(r'\text') # \text


# Arithmetic operators
	# +		addition
	# -		subtraction
	# *		multiplication
	# /		division)
	# **	raise to power
	# %		find modulo
	2 + 2

# '' & "" - text
	'text'
	"text"
	
# \ - escape character
	'text\'s'
	
# \n & """""" - new line
	print('line1\nline2')
	print("""line1
	line2
	""")

# input - input a variable
	var = input('input text: ')
	
# + - string concatination
	print('string' + ' ' + 'concatination')
	
# * - string multiplication
	print(2 * 'text')
	
# convert variable types
	print(int('5') + int('2'))
	
# variables
	x = 2
	print(x + 5)
	
# del - delete variables
	del x
	
# in-place operators
	x += 3 # x = x + 3
	x += 'text2' # x = x + 'text2'
	
# true & false - boolean logic
	print(2 == 3) # False
	print('text' == 'text') # True
	print(2 != 3) # True
	print(5 > 10) # False
	print(5 <= 7) # True
	
# if statement
	x = 2
	if x > 0:
		print('Positive number')
		if x > 1:
			print('Greater than one')
		
# else statement
	x = 2
	if x > 0:
		print('Positive number')
	else:
		print('Negative number')
		
# elif statement
	x = 0
	if x < 0:
		print('Negative number')
	elif x > 0:
		print('Positive number')
	else:
		print('Zero')
	
# and & or boolian statements
	print(1 == 1 and 2 == 2) # True
	print(1 == 1 or 2 == 3) # True
	
# not statement - inverse boolean logic
	print(not 1 == 1) # False
	print(not 1 != 1) # True
	
# Boolean operator priority. = has the highest.
	print(False == False or True) # True (True or True)
	print(False == (False or True)) # False (False = False/True)
	print((False == False) or True) # True (True or True)
	
# [] - lists used to store an indexed array
	words = ['word1', 'word2', 'word3', [1, 2, 3]]
	print(words[0]) # word1
	print(words[3][0]) # 1

	# strings can also be indexed as arrays
		str = 'text'
		print(str[2]) # x
		
	# changing an element inside a list
		words[1] = 'text'
		
	# concatinating and multiplying lists
		nums = [1, 2, 3]
		print(nums + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
		print(nums * 2) # [1, 2, 3, 1, 2, 3]
		
	# finding value in a list
		words = ['word1', 'word2', 'word3']
		print('word1' in words) # True
		print('word4' not in words) # True

	# append - append an object to the end of a list
		nums = [1, 2, 3]
		nums.append(4)
		print(nums) # [1, 2, 3, 4]
		
	# insert - insert an object to any position within a list
		words = ['word1', 'word2', 'word3']
		words.insert(1, 'text1')
		print(words) # ['word1', 'text1', 'word2', 'word3']
		
	# len - returns the length of a list
		nums = [1, 2, 3]
		print(len(nums)) # 3
	
	# max - returns maximum value of a list
		nums = [1, 2, 3]
		print(max(nums)) # 3
		
	# index - tells position of the first occurence.
		words = ['word1', 'word2', 'word3']
		print(words.index('word3')) # 2
	
	# range - returns all numbers within a specified range ({starting number}, {ending number}, {interval}.
		nums = list(range(3)) # [0, 1, 2]
		nums = list(range(1, 3)) # [1, 2]
		nums = list(range(1, 20, 5)) # [1, 6, 11, 16]
		
# {} - dictionaries. Structured way of storing data.
	dict = {'text1' : 1, 'text2' : 2, 'text3' : 3}
	print(dict['text3']) # 3
	
	# Can store lists inside
	dict = {
		'text1' : [1, 2, 3],
		'text2' : [4, 5, 6],
		'text3' : [7, 8, 9]
	}
	print(dict['text3']) # [7, 8, 9]
	
	# Can both set existing values as well as add new values
	dict = {
		'text1' : [1, 2, 3],
		'text2' : [0, 0, 0]
	}
	dict['text2'] = [4, 5, 6]
	dict['text3'] = [7, 8, 9]
	print(dict) # {'text1': [1, 2, 3], 'text2': [4, 5, 6], 'text3': [7, 8, 9]}
	
	# get - gets a value in a dictionary and returns None or a custom message when key is not found
	dict = {
		'text1' : [1, 2, 3],
	}
	print(dict.get('text1')) # [1, 2, 3]
	print(dict.get('text2')) # None
	print(dict.get('text2', 'Value not there')) # Value not there
	
# () - tuples. Unchangeable lists and hence have performance benefits.
	tuple = ('obj1', 'obj2', 'obj3')
	
# [x:y:z] - array cuts
	# where [{starting number inclusive}, {ending number not inclusive}, {step number}]
	nums = [1, 2, 3, 4, 5]
	print(nums[1:]) # [2, 3, 4, 5]
	print(nums[1:3]) # [2, 3]
	print(nums[0:5:2]) # [1, 3, 5]
	print(nums[0:-1]) # negative to count from right to left # [1, 2, 3, 4]
	print(nums[::-1]) # [5, 4, 3, 2, 1]
	
# list comprehension - create lists using a rule
	nums = [i**2 for i in range(5)]
	print(nums) # [0, 1, 4, 9, 16]
	
	# if-statement in a list
		evens = [i**2 for i in range(10) if i**2 % 2 == 0]
		print(evens) # [0, 4, 16, 36, 64]
		
# format - string formatting
	nums = 'Numbers: {x}, {y}' .format(x = 1, y = 2)
	print(nums) # Numbers: 1, 2

	nums = [4, 5, 6]
	msg = 'Numbers: {0}, {1}, {2}'. format(nums[0], nums[1], nums[2])
	print(msg) # Numbers: 4, 5, 6
	
# string functions
	print(['text1', 'text2', 'text3'])
	# join - joins objects into a single string using a separator
	print('.'.join(['text1', 'text2', 'text3'])) # text1.text2.text3
	# split - splits a string into objects using a separator
	print('text1, text2, text3'.split(','))
	# replace - used for replacing strings
	print('string'.replace('i', 'o')) # Strong
	# startswith & endswith - tells if a substring is in the beginning or an end of a strings
	print('a b c'.startswith('a')) # True
	print('a b c'.endswith('c')) # True
	# upper() & lower() - changes letter case
	print('Abc'.upper()) # ABC
	print('Abc'.lower()) # abc
	
# mathematic functions
	# min - returns minimum of a set
	# max - returns maximum of a set
	# abs - returns an absolute value of a number
	# sum - returns a sum of a set

			### LOOPS ###

#  while loop - executes as many times as needed while condition is true. Different to an if-statement executing only once.
	i = 1
	while i <= 5:
		print(i)
		i = i + 1
		
	while 1=1: # infinite loop
	
# for loop - loops over every item in a list. a more practical application of a while loop in the case of lists.
	words = ['word1', 'word2', 'word3']
	for word in words:
		print(word)
		
	for i in range(5):
		print(i)
	
# break - exits out of a loop when condition is met.
	i = 0
	while 1==1:
		print(i)
		i = i + 1
		if i >= 5
			break

# continue - continues to the next cycle of a loop when condition is met.
	i = 1
	while True:
		i = i + 1
		if i == 2:
			continue
		if i == 5:
			break
		print(i)
		
# all & any - returns true when all/any of the arguments satisfy a particular criteria
array = [55, 44, 33, 22, 11]

if all([i > 5 for i in array]):
    print("All larger than 5")

if any([i & 2 == 0 for i in array]):
    print("At least one number is even")
	
# enumerate - enumerates a list
for v in array:
	print(n) # (0, 55)
			 # (1, 44)
			 # (2, 33)
			 # (3, 22)
			 # (4, 11)
	
			### FUNCTIONS ###

# functions - objects of reusable code
	def func():
		print('function')
		
	func() # function
	
	def func(x, y):
		print(x + y)

	func(1, 2) # 3
	addition = func
	addition(1, 2) # 3
	
	# return - returns a value inside a function and exits out of the funtion (nothing will be executed afterwards)
	def func(x, y):
		if x >= y:
			return 'x greater than y'

	print(func(3, 2)) # x greater than y
	
	# functions within functions
		def add(x, y):
			return x + y

		def do_twice(func, x, y):
			return func(func(x, y), func(x, y)) # calls add(add(), add())

		a = 5
		b = 10

		print(do_twice(add, a, b)) # call add() with parameters a, b # 30

	# # & """ - comments and docstrings
	"""
	Guide
	"""
	print('text')
	
# decorators - used to modify existing functions without changing their structure
	def decorator(anotherfunction):
		def wrap():
			print("=======")
			anotherfunction()
			print("=======")
		return wrap()

	def function1():
		print("some function")

	decorated = decorator(function1) # =======
									 # some function
									 # =======
		
			### EXCEPTIONS ###
		
# try / except - tries executing what's in the try block, and executes the except block when an error occurs
	try:
		var = 10
		print(var + '5')
	except (ValueError, TypeError):
		print ('Format error')
	# except:
	# print('General error occured')
	
# finally - always execute that clause in case of try / catch
	try:
		var = 10
		print(var + '5')
	except (ValueError, TypeError):
		print ('Format error')
	finally:
		print('Nevermind')
		
# raise - raises exceptions
	try:
		num = 5 / 0
	except:
		raise # ZeroDivisionError: division by zero
		
# assert - test code correctness
	assert 1 + 1 == 3 # AssertionError
	assert (1 + 1 == 3), 'Just not right!' # AssertionError: Just not right!
	
			### WORKING WITH FILES ###
			
# open - opens a file
	file = open(r'C:\1.txt')
	file = open(r'C:\1.txt', 'r')
	file = open(r'C:\1.txt', 'w') # write mode
	file = open(r'C:\1.txt', 'wb') # binary write mode
	
# with - alternative way to open a file with an alias
	with open(r'C:\Users\K\Desktop\1.txt') as f:
		print(f.read())
	
# close - closes a file
	file.close()
	
# reading from a file
	file = open(r'C:\Users\K\Desktop\1.txt', 'r')
	print(file.read()) # read({number}) to read only the specified number of characters
	file.close()
	
# reading every row of a file
	contents = file.readlines()
	
	file = open(r'C:\Users\K\Desktop\1.txt', 'r')

	for line in file:
		print(line)

	file.close()

# write - write new contents to file
	file = open(r'C:\Users\K\Desktop\1.txt', 'w')
	file.write('new text')
	#written = file.write('new text')
	#print(written) # output number of characters written
	file.close()
	
# Example with a try
	try:
		file = open(r'C:\Users\K\Desktop\1.txt')
		print(file.read())
	finally:
		file.close()

			### OTHER OBJECTS ###
# None - an absence of value (similar to Null)
	var = None
	print(var) # None

	def func():
		return

	var = func()
	print(var) # None
	
# lambda functions - a short way of defining functions (less functional than ordinary))
print((lambda x: x * 2)(2)) #4

double = lambda x: x * 2
print(double(2)) #4

#map - Maps an array to a function as it’s imput. (The output needs to also be a list).
list1 = [1,2,3]

def function1(x):
    return x * x

print(list(map(function1, list1))) # [1,4,9]]

-# filter - returns only the values in an array that pass a certain criteria
list1 = [1,2,3,4,5]

def function1(x):
    return x > 2

print(list(filter(function1, list1))) # [3,4,5]

# yield - an iterative method for a function - used to display all values applicable to a loop
def function1(x):
    for i in range(x):
        if i > 5:
            yield i

print(list(function1(10))) #[6,7,8,9]

# decorated functions
def decor(function1):
    def wrap():
        print('.....')
        function1()
        print('.....')
    return wrap

def function1():
    print('text')

output = decor(function1)
output()


# @decorator - short way of decorating a function
...
@decor
def function1():
    print('text')

function1()

# recursion - calls the same or another function within itself. Important to include a break condition to avoid infinite loops
def function1(x):
    if x == 1:
        return x
    else:
        return x + function1(x - 1)

print(function1(5))


nums = {1, 2, 1, 3, 1, 4, 5, 6}
# add - add a number to the end
nums.add(-7)
# remove - remove a number
nums.remove(3)
# pop - ???

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) # {1,2,3,4,5,6,7,8,9}
print(first & second) # {4,5,6}
print(first - second) # {1,2,3}
print(second - first) # {7,8,9}
print(first ^ second) # {1,2,3,7,8,9}

# itertools
from itertools import count, cycle, repeat

for i in count(5):
    print(i)
    if i == 10:
        break # 1 2 3 4 5

for i in cycle('ABC'):
    print(i) # A B C A B C A B C...

for i in repeat(5, 3):
    print(i) # 5 5 5

from itertools import accumulate, takewhile, chain

def function1(x):
    return x < 5
    
# accumulate - accumulates all the variables in an array into a sum
print(list(accumulate(range(5)))) #[1,3,6,10]
# takewhile - return values of an array until they stop satisfying a condition
print(list(takewhile(function1, range(10))))
# chain - combine two objects into one array
print(list(chain('ABC', 'DEF')))

from itertools import product, permutations

# product - a cartesion product between two arrays
print(list(product('AB', 'CD')))
# permutations - 
print(list(permutations('ABC', 3)))

# class - a blueprint for an object
class processors:
    def __init__ (self, freq, wattage):
        processors.freq = freq
        processors.wattage = wattage

    # can define gereral properties
    def type(self):
        print('CPU')

AMD = processors(3700, 65)
print(AMD.freq) # 3700
AMD.type() # CPU

# class inheritance - superclass/subclass - using a class as a blueprint for another class
class CPU(processors):
    def type(self):
        print("CPU")

Intel = CPU(4500, 75)
print(Intel.freq) # 4500
Intel.type() # CPU

# super() - a supermethod returns the parent method
class A:
    def method(self):
        print('method1')

class B(A):
    def method(self):
        print('method2')
        super().method()

B().method() # method2, method2

# magic methods - adds special functionality to functions
class Day(object):
    def __init__(self, visits):
        self.visits = visits

    def __add__(self, other):
        TotalVisits = self.visits + other.visits
        return TotalVisits

day1 = Day(2)
day2 = Day(3)
total = day1 + day2
print(total) #5

# __new__ - explicitly creating a new method
# __del__ - decreasing the count/deleting an object

# private methods - not directly accessible to the rest of the program
_metgod1 # private. Importing a class won’t include those.
__method1 # strictly private and name will change. Can be called as _class1__method1

import random

class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

# @classmethod - an independent method inside a class with parameters that depend on class's
    @classmethod
    def date_to_string (cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        date = cls(day, month, year)
        return date

# @staticmethod - an independent method inside a class with parameters that don't depend on class's
    @staticmethod
    def is_date_valid (date_string):
        day, month, year = map(int, date_string.split('-'))
        return day <=31 and month <= 12 and year <= 9999

print(Date(12, 7, 2018).day) #12
print(Date.date_to_string('12-07-2018').month) #7
date2 = Date.date_to_string('12-07-2018')
print(date2.year) #2018

print(Date.is_date_valid('12-07-2018')) # True

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    # @property - making a read-only method insite a class.
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    # .setter - set class method values
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "123":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)



# Regular Expressions
import re

# match - matches at the beginning
print(re.match('text', 'text some')) # span=(0, 4)

if re.match('text', 'text some'):
    print('found') # found

# () groups
print(re.match(r'a(bc)(d(e)f)', 'abcdefg').group()) # abcdef
print(re.match(r'a(bc)(d(e)f)', 'abcdefg').group(0)) # abcdef
print(re.match(r'a(bc)(d(e)f)', 'abcdefg').group(1)) # bc
print(re.match(r'a(bc)(d(e)f)', 'abcdefg').group(2)) # def
print(re.match(r'a(bc)(d(e)f)', 'abcdefg').group(3)) # e
print(re.match(r'a(bc)(d(e)f)', 'abcdefg').groups()) # ('bc', 'def', 'e')


# (?P<name>...) named groups
print(re.match('?P<group1>abc', 'abcdefg')).group('group1')

# search - searches the whole string for a match
print(re.search('text', 'some text some')) # span=(5, 9)

# group() - return matching line
print(re.search('text', 'text some text').group()) # text

# start() - returns position of the first occurence
print(re.search('text', 'text some text').start()) # 0

# end() - returns position of the last occurence starting from the end
print(re.search('text', 'text some text').end()) # 4

# span() - returns position of the first & last occurence as an array
print(re.search('text', 'text some text').span()) # (0, 4)

# findall - outputs all matches into an array
print(re.findall('text', 'text some text')) # ['text', 'text']

# sub - substitute a pattern
print(re.sub('text', 'replaced text', 'text some text', count=0, flags=0)) # replaced text some replaced text

# <group> - named groups - can be taken using numbers and names
print(re.match(r'(?P<group1>abc)', 'abcdefg').group('group1')) # abc

# (?:expression) - hidden groups - can't be taken using the group() method so they don't return or break any group numbering
print(re.match(r'(?:abc)', 'abcdefg').group(1)) # no such group

# *args - the ability to pass multiple arguments to a function
def function(named_arg, *args):
    return args

print(function(1, 2, 3, 4, 5)) # (2, 3, 4, 5)

# **kwargs - returns previously unnamed variables and their values in a dictionary
def my_func(x, y=7, *args, **kwargs):
    return kwargs

print(my_func(2, 3, 4, 5, 6, a=7, b=8)) # {'a': 7, 'b': 8}

# extracting lists to variables
a, b, c = [1, 2, 3]
print(a,b) # 1 2

# *obj - assigns to the object the remainder of variables after all other variables have been assigned
a, *b, c = [1, 2, 3, 4, 5]
print(b) # 2, 3, 4

# ternary operator - a if condition else b
i = 2
a = 5 if i > 1 else 0
print(a) # 5

# else without 'if' - can be used after 'for', while
for i in range(10):
    if i == 11:
        break
else:
    print('unreached') # unreached

# else in try & catch
try:
    print(6/2)
except ZeroDivisionError:
    print('division error')
else:
    print('success') # success

print(1 + '1' == 2)



# __main__ - don’t execute the code in a script file when it has been imported as a module. Inside the imported script file it is the main file, but outside (such as when imported), it is not main
if __name__ == “__main__”:


			### REFERENCES ###
SoloLearn

Author: Konstantin Pokhilchuk