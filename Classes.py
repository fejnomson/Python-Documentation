# https://docs.python.org/3.5/tutorial/classes.html
# https://docs.python.org/3.5/tutorial/index.html # this is also useful

def scope_test():

	def do_local():
		# local to do_local()
		spam = 'local spam'

	def do_nonlocal():
		# local to scope_test()
		nonlocal spam
		spam = 'nonlocal spam'

	def do_global():
		# global / module level, BUT NOT within scope_test
		global spam
		spam = 'global spam'

	spam = 'test spam'
	do_local()
	print('after local assignment:', spam)
	do_nonlocal()
	print("after nonlocal assignment:", spam)
	do_global()
	print('after global assignment:', spam)

scope_test()
print('in global scope:', spam)


class MyClass:
	"""example class"""
	i = 12345

	def f(self):
		return 'hello world'

x = MyClass() # instantiation. Think of this like a function, where the
# 	function creates a new instance of the class.
x.i # attribute reference; returns integer object
x.f() # also attribute reference; returns function object
y = x.f
y()

# __init__() is a function that'll execute whenever a class is initiated.
class MyClass:
	"""exmaple class"""
	def __init__(self):
		self.data = [] # so every time you instantiate a new myclass object, you're
		# running a function that adds an attribute, 'data', to the object, and
		# that attribute is an empty list.

	i = 12345

	def f(self):
		return 'hello world'

class myclass:
	def __init__(self):
		print('just instantiated a new myclass object')

	i = 12345

	def f(self):
		return 'hw'

class Complex:
	def __init__(self, realpart, imagpart):
		# So here you're assigning two inputs to the object (of class Complex)
		# 	upon instantiation
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)
x.r
x.i

# You can assign data attributes to an object, and delete them
x.counter = 1
while x.counter < 10:
	x.counter = x.counter * 2
print(x.counter)
del x.counter

# Calling using object.function(<self>) is the exact same as using
# 	classvar.function(object). In the latter, you have to explicitely
# 	specify WHICH INSTANCE OF THE OBJECT YOU'RE CALLING THE METHOD ON. On
# 	the former, it's always the object you're calling.
# It's basically just different notation. Almost like:
mylist = list(<some elements>)
mylist.print() # because you know that mylist is a list, you can call print
# without specifying method dispatch.
print.list(mylist) # but here, you don't know what mylist is, so you
# explicitely call method dispatch, so you know that mylist is a list.
t = MyClass()
t.f()
MyClass.f(t)
# It kinda forces you to throw everything together into useful abstractions
# 	and be explicity about the inputs and outputs. It's harder to just
# 	define general variables and functions, you have to say what they're
# 	used for and legal inputs and outputs.


# Class and instance variables
class Dog:

	kind = 'canine' # attribute FOR EVERY Dog OBJECT INSTANTIATED
	# This is a class variable, because it belongs to every object of that
	# 	class, regardless of the unique instantiation

	def __init__(self, name):
		# this is an instance variable, because it's unique to every instantiation
		self.name = name # attribute THAT'S DIFFERENT FOR EVERY DOG OBJECT INSTANTIATED

d = Dog('Fido')
e = Dog('Buddy')

class Dog:

	tricks = [] # class variable for every class object, regardlesss of individual instance

	def __init__(self, name):
		# instance attributte, unique to every instantiation
		self.name = name

	def add_trick(self, trick):
		# method attribute. function that comes with every Dog object.
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
e.tricks

class Dog:

	def __init__(self, name):
		self.name = name
		self.tricks = [] # if you want something unique to each instance, you
		# 	need to put it under __init__(), otherwise it'll belong to every
		# 	instantiation.

	def add_trick(self, trick):
		self.tricks.append(trick)

class Dog:

	def __init__(self, name):
		self.name = name
		self.tricks = [] # if you want something unique to each instance, you
		# 	need to put it under __init__(), otherwise it'll belong to every
		# 	instantiation.

	def add_trick(self, trick):
		self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
e.tricks

class Dog:

	def __init__(jeffrey, name):
		jeffrey.name = name
		jeffrey.tricks = [] # if you want something unique to each instance, you
		# 	need to put it under __init__(), otherwise it'll belong to every
		# 	instantiation.

	def add_trick(jeffrey, trick):
		jeffrey.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
e.tricks
# 'self' has no special meaning in python, you can use any variable. It's
# 	just a convention.


# You can define functions outside of a class defintion, then use them in a
# 	class definition.
def f1(self, x, y):
	return min(x, x + y)

class C:
	f = f1

	def g(self):
		return 'hello world'

	h = g

# You can define methods in a class that refer to methods of that class.
# 	So here, addtwice() refers to add() method. this works.
class Bag:
	def __init__(self):
		self.data = []

	def add(self, x):
		self.data.append(x)

	def addtwice(self, x):
		self.add(x)
		self.add(x)

purse = Bag()
purse.data
purse.add('jeffrey')
purse.add('monson')
purse.addtwice('michael')
suitcase = Bag()
suitcase.data
suitcase.add('blue shirt')
suitcase.add('socks')
suitcase.addtwice('pants')

# object's classs is stored as object.__class__
purse.__class__
suitcase.__class__


# Inheritance
# Does an instantiation belong to a certain class?
isinstance(purse, Bag) # is purse instance of class Bag?
isinstance(purse, list) # is purse instance of class list?
isinstance([1, 2, 3], list)
isinstance(pd.Series([1, 2, 3]), pd.Series)
isinstance(pd.Series([1, 2, 3]), list)
# does a certain class inherit from another one?
issubclass(bool, int) # does boolean inherit from integer?
issubclass(1, 'jeff') # inputs must be class


# 9.6. Private Variables
# private variables are variables that belong to an object that CAN'T BE 
# 	ACCESSED FROM OUTSIDE OF THE OBJECT.
# These don't formally exist in python.
# BUT convention is: if name prefixed with underscore _spam, then it should
# 	be treated as non-public
class Mapping:
	def __init__(self, iterable): # so maybe the __ at the beginning of the
	# 	init variable name means that you're not supposed to call the
	# 	__init__ method from outside of the class (aka publicly); it should
	# 	only be accessed within the class (akak privately).
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

	__update = update # Private copy of original update() method
	# 	looks like here, you're assigning the update method,
	# defined locally within Mapping, to a new name __update. So you can call
	# __update within the Mapping class internally.
	# The use here is to iterate thru the list you provide upon instantiation,
	# 	using the update() method that you define later.
	# But why can't you just use update(), instead of __update()

x = Mapping([1, 2])

# Because __init__ isn't formally private, you can call it publicly to
# 	instantiate a new object.
x.__init__(['a', 'b'])
x.items_list
x.update(['1', '2'])
x.items_list

class Mapping2:
	def __init__(self, iterable): # so maybe the __ at the beginning of the
	# 	init variable name means that you're not supposed to call the
	# 	__init__ method from outside of the class (aka publicly); it should
	# 	only be accessed within the class (akak privately).
		self.items_list = []
		self.update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

x = Mapping2([1, 2])
x.update([3, 4])
# this works fine.

class MappingSubclass(Mapping):

	def update(self, keys, values):
		# provides new signature for update() but doesn't break __init__()
		for item in zip(keys, values):
			self.items_list.append(item)
			# this creates a subclass of Mapping, where the update method takes
			# 	keys AND values, zips them together into a list of tuples, then
			# 	appends the list of tuples to the existing items list.
			# When you call update() on a MappingSubClass object, it'll call the
			# 	one defined in MappingSubclass. Guessing that the original one
			# 	defined in Mapping is overwritten.
			# The new definition / overwriting of update() doesn't break the 
			# 	call to __init__, becuase you saved the original function as
			# 	__update(), which you didn't overwrite.

xs = MappingSubclass([1, 2])
xs.update(['first', 'second'], [1, 2])


class MappingSubclass2(Mapping2):

	def update(self, keys, values):
		# provides new signature for update() but doesn't break __init__()
		for item in zip(keys, values):
			self.items_list.append(item)
			# this creates a subclass of Mapping, where the update method takes
			# 	keys AND values, zips them together into a list of tuples, then
			# 	appends the list of tuples to the existing items list.
			# When you call update() on a MappingSubClass object, it'll call the
			# 	one defined in MappingSubclass. Guessing that the original one
			# 	defined in Mapping is overwritten.
			# The new definition / overwriting of update() doesn't break the 
			# 	call to __init__, becuase you saved the original function as
			# 	__update(), which you didn't overwrite.

xs2 = MappingSubclass2([1, 2]) # this call fails becuase it calls the 
# 	update() function that you defined in MappingSubclass2, as opposed to
# 	the one in Mapping2
# So the punch line here is that you can use the __<name> convention to 
# 	keep certain function defintions private to a class, to avoid
# 	overwriting it / having it conflict with futher defintions / subclasses.


# can have a data type used to just bundle together a few named items
class Employee:
	pass # empty class dfeintion

john = Employee()
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 100

# Instance method objects also have attributes:
x.update
x.update.__self__ 
x.update.__func__
# not sure what these mean...



# ------------------------------------------------------------------------------
# Exceptions and errors
# You can throw different error objects based on the type of error
# 	encountered.
# So if you get a ValueError, you can set some course of action; if you get
# 	a KeyError, you can set another course of action.
# In the real world, you'd never try an expression where raise a specific
# 	type of error yourself; this is just for the sake of example.
# Looks like Exception handles all types of errors, so it's bad for using in
# 	my example below, unless you use it last. This gives a chance to match
# 	the specific error thrown with a specific type of exception first,
# 	before you apply the general catch-all of Exception.
try:
	raise ValueError()
except ValueError:
	print('999')
except KeyError:
	print('000')
except Exception:
	print('555')

try:
	raise KeyError()
except ValueError:
	print('999')
except KeyError:
	print('000')
except Exception:
	print('555')

try:
	raise Exception()
except ValueError:
	print('999')
except KeyError:
	print('000')
except Exception:
	print('555')
# ------------------------------------------------------------------------------


# Exceptions are classes too
# two ways of using raise statment, for throwing errors:
raise Class
raise Instance

class B(Exception): # think this just makes a new class that inherits from Exception; new class is 'B'
	pass
class C(B): # new class that inherits from B, which inherits from Exception
	pass
class D(C): # new class that inherits from C, which inherits from B, which inherits from Exception
	pass

# So I think this is: it raises an error, because B, C, and D all throw
# 	errors, similar to stop() in R. BUT, because B, C, and D are different
# 	object types, they're considered 'different' types of errors. Like
# 	ValueError or KeyError in python.
for cls in [B, C, D]:
	# B inherits from Exception
	# C inherits from B
	# D inherits form C
	try:
		# So here, you're raising an error of class B, C, or D.
		raise cls()
	except D:
		# If the error you raised is of class D, print 'D'
		print('D')
	except C:
		# If the error you raised is of class C, print 'C'
		print('C')
	except B:
		# If the error you raised is of class B, print 'B'
		print('B')
# So here, you're raising error of class B. The exception that matches that
# 	type of error makes it print 'B'.
# Then, you're raising error of class C. Exception that matches that type of
# 	error says to print 'C'.
# Then you're raising error of class 'D'. Exception that matches says to
# 	print 'D'.

for cls in [B, C, D]:
	try:
		raise cls()
	except B:
		print('B')
	except C:
		print('C')
	except D:
		print('D')
# This prints out 'B', 'B', 'B' becuase THE FIRST MATCHING EXCEPT CLAUSE IS
# 	THE ONE THAT'S TRIGGERED.
# So that means that B is of class B AND class Exception, because B inherits
# 	from Exception; C is of class Exception, class B, AND class C; D is of
# 	class Exception, class B, class C, AND class D.
# And this uses the FIRST MATCHING CLASS.
# So in theory, it should always match class Exception before anything else:
for cls in [B, C, D]:
	try:
		raise cls()
	except Exception:
		print('090909090909')
	except B:
		print('B')
	except C:
		print('C')
	except D:
		print('D')
# This is kinda like having class be c('grouped_df', 'tbl_df', 'data.frame')
#		in R.
# I'm proud of myself for not glossing over this.


# ITERATORS
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("dldldld.txt"):
    print(line, end='')
# for() statements in python call iter() on python container objects;
# 	iter() returns an iterator object with method __next__(); this method
# 	accesses elements of the container one at a time; when there are no
# 	more elements, __next__() raises StopIteration exception which tells the
# 	for loop to terminate

s = 'abc'
it = iter(s)
it
next(it)
next(it)
next(it)
next(it)

# You can add iterator behavior to your classes, by defining an __iter__()
# 	method that returns an object with a __next__() method.
# I think this'd be to call the for statement on...
class Reverse:
	"""Iterator for looping over a sequence backwards"""
	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self): # no idea what this means...
		return self

	def __next__(self):
		if self.index == 0: # if you reach the first element in the container,
		# throw the stopiteration error
			raise StopIteration
		self.index = self.index - 1 # otherwise chop the index by 1
		return self.data[self.index] # and lop off the data you've already processed
	# My guess is that for() will look in the Reverse object to see if it has
	# 	an __iter__ method, and it'll use the __next__() method as the work
	# 	horse.
	# So I think the idea here is that, if you add on a couple pieces to your
	# 	object, you can easily call the pre-existing for() function on it
	# 	without any additional work / overhead.
	# Maybe you have an object where you only ever want to loop through
	# 	backwards, or by evens, or by odds -- all that'd be encapsulated in
	# 	the class definition. for() would recognize that, so you aren't
	# 	limited to having to specify everything for every loop call.
	# It's like adding on an extra attribute to communicate with the for loop
	# 	function.

rev = Reverse('spam')
iter(rev)
for char in rev:
	print(char)


class Evens:
	"""iterator for looping thru Evens only"""

	def __init__(self, data):
		self.data = data
		self.index = -1
		self.last = len(data) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.index + 2 > self.last:
			raise StopIteration
		self.index = self.index + 2
		return self.data[self.index]

evs = Evens('spam')
iter(evs)
for char in evs:
	print(char)

# index = -1
if -1 + 2 >= 3:
	raise StopIteration
self.index = -1 + 2
return self.data[1]

# index = 1
if 1 + 2 >= 3: # stops one short - you can do 'spam'[3]
	raise StopIteration
self.index = -1 + 2
return self.data[1]


class EveryOther:
	"""iterator for looping thru odds only"""

	def __init__(self, data):
		self.data = data
		self.index = -2
		self.last = len(data) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.index + 2 > self.last:
			raise StopIteration
		self.index = self.index + 2
		return self.data[self.index]

evs = EveryOther('spam')
iter(evs)
for char in evs:
	print(char)


class Every:
	"""iterator for looping thru all"""

	def __init__(self, data):
		self.data = data
		self.index = -1
		self.last = len(data) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == self.last:
			raise StopIteration
		self.index = self.index + 1
		return self.data[self.index]

evs = Every('spam')
iter(evs)
for char in evs:
	print(char)


# Generators: a tool for creating iterators
def reverse(data):
	for index in range(len(data) - 1, -1, -1):
		# index goes from data[len(data) - 1]:0 by 1
		yield data[index]
		# I think yield just means return data[i], and if it's the last i, then
		# 	terminate the function

for char in reverse('golf'):
	print(char)

# generators are kind of a type of class-based iterator; geneators have the
# 	__iter__() and __next__() methods created automatically
# Don't need to use self.index and self.data; these are saved automatically
for ix in range(0, 11):
	print(ix)
# I think this is awkward coming from R, becuase in R everything is always
# 	abstractd away; it's always iterable so you can either just go thru
# 	numbers, names, or elements. You never need to explicitly define
# 	movement from from one to the next, or information to the call to for()
# 	about whether you can move thru the container or not.


# Generator expressions:
# Kinda like anonymous functions, but for quickly making a generator
# Kinda like list comprehensions, but with () instead
sum(i*i for i in range(10))
sum(i + 1 for i in  range(10)) # sum of 1 thru 10
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x, y in zip(xvec, yvec))
from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
test = {i: i * 2 for i in range(1, 11)} # YOU CAN GENERATE THE KEYS IN A
# 	DICTIONARY as part of a generator expression
test = [i * 2 for i in range(1, 11)] # lists don't have keys, so you don't
# 	need to store any keys.
data = 'golf'
list(data[i] for i in range(len(data) - 1, -1, -1))
{i: data[i] for i in range(len(data) - 1, -1, -1)}



