# https://docs.python.org/3.5/tutorial/classes.html

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

== stopped here ==
9.6. Private Variables

