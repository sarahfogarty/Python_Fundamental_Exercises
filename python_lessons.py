print "Hello World"

my_string = "this is a string stored in teh my_string variable"
# This is an integer stored in a variable
my_num = 5
#  a tuple stored in a variable
my_tuple = (1,2,3,4,5)
#  a dictionary stored in a variable
my_dictionary = {'name': 'Michael Choi', 'fave_lang': 'Python'. 'level': 'Sensei'}


# define a function tha tsays hello to the name provided
# this starts a new block

def say_hello(name):
    # these lines are indented therefore part of the function
    if name:
        print 'Hello, ' + name + 'from inside the function'
    else:
        print 'No name'
# now we are unindented and have ended the previous block
print 'outside of the function'


# to get user input, we will use the raw_input() or input() functions
# create variable called greeting that holds the value of a string
greetings = "Hello Ninja!"
print greetings
# you can use single or double quotes for strings
print 'What is your name?'
# we use raw_input() to get user input and set it to a variable.
name = raw_input()
print 'How old are you?'
# We can also used input() to get user input
age = input()
# adding of variables to a string to be printed is like this:
print "Your name is", name
print "You are", age, "years old"
# you can also add the variable in between strings just liek teh above
raw_input("\n\nPress the enter key to exit.")
# the line above woudl make the app not close or exit out automtatically


#  strings
print "this is a string"

name = "Zen"
print "My name is ", name

name = "Zen"
print "My name is " + name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}". Format(first_name, last_name)
# Above, the string "zen" is inserted where the first curly brace is and the string "last_name" where the secton curly brace is. There should be a corresponding number of curly braces and arguements passed to the .format() function.

# Built in string functions

# <string>.capitalize()
my_string = "hello world"
print my_string.capitalize()
# The output would be: Hello world

 # <string>.lower
 my_string = "Hello WORLD"
 print my_string.lower()
 # The outbut would be: hello world

 # <string>.swapcase
 my_string = "Hello WORLD"
 print my_string.swapcase()
 # the output woudl be> hELLO world

 # <string>.upper
 my_string = "hello world"
 print my_string.upper()
 # the output would be: HELLO WORLD

 # <string>.find(<substring>)
my_string = "hello world"
print my_string.find("el")
# The output woudl be 1

# <string>.replace(<old>, <new> ,[max])
# this method returns a copy of the string with all occurances of substring old replaced by new. If the optional argument max is given, only the first number of times indicated in max will you have the substring old replaced.
my_string = "hello world"
print my_string.replace("world", "kitty")
# The output would be hello kitty

my_string = "egg, egg, Spam. egg. and Spam"
print my_string.replace('egg', "Spam", 2)
# the output would be Spam, Spam, Spam, egg, Spam
# notice that only the first 2 "egg" matches were replaced in the string

# Lists
ninjas = ["Rozen", "KB", "Oliver"]
,y_list = [4,['list', 'in', 'a', 'list'], 987]
empty_list = []

# An example of a list with mixed data types
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables
salad = 3 * vegetables
print salad

# python lists values are accessed same as JS
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens

# Manipulating Lists
# .append appends new items to the end of a list
# <list>.append(<new_element>)
x = [1,2,3,4,5]
x.append(99)
print x
# the output would be [1,2,3,4,5,99]

# .insert inserts a new item into the list at the given index. You can pass any data type in to this function
# <list>.insert(<index>, <new_element>)
x = [1,2,3,4,5]
x.insert(2,99)
print x
# The outout would be [1,2,99,3,4,5]

#  .remove would remove teh first item from the list whos value is provided
# <list>.remove(<element>)
x = [1,2,3,4,5]
x.remove(3)
print x
# the output would be [1,2,4,5]

# .pop removes the item at a given position' if the position is not given, it will remove the last entry from the list
# <list>.pop(<optional_index>)
x = [1,2,3,4,5]
x.pop()
print x
# the output would be [1,2,3,4]
y = [12,11,12,13,14]
y.pop(1)
print y
# the output would be [10,12,13,14]

# .sort sorts the elements in a list
# <list>/sort()
x = [99,4,5,2,-3]
x.sort()
print x
# the output would be [-3, 2, 4, 5, 99]

# Slicing uses [] characters to return a copy of the list, constrained to the specified indices. The starting index and ending index should be separated by the ":" character
x = [99,4,2,5,-3]
print x[:]
# the output would be [99,4,2,5,-3]
print x[1:]
# the output would be [4,2,5,-3]
print x[:4]
# the output would be [99.4.2.5]
print x[2:4]
# the output would be [2,5]

# List built in functions
# len() returns the number of items in a list
my_list = [1,'zen','hi']
print len(my_list)
# the output would be 3

# max() returns the largest item in the sequence.
my_list = [1,7,3]
print max(my_list)
# the output would be 7

# min() returns the smallest item in a list. When comparing boolean to numbers true == 1 and false == 0. Comparing items of different types is uncommon but if you ever do this, note that all numbers < all dictionaries < all list < all strings , all tuples.
my_list = [1,7,3]
print min(my_list)
# the output would be 1

# any() returns True if there exists any item in teh sequence which is True.
my_list = [0,'hi',' ']
print any(my_list)
# the output would be false
my_list = [0, ' ']
print any(my_list)
# the output would be False since 0 (zero)

# all() returns True if all items in teh sequence are true.
my_list = [0, 'Zen', ' ']
print all(my_list)
# woudl return false
my_list [4, 'hi']
print my_list
# would return true


# Conditional Expressions and Logical Operators

age = 15
of age >= 18:
    print 'legal age'
else:
    print 'you are so young!'

# in python, use elif when you have multiple elses
if age >= 18:
    print 'legal age'
elif age == 17:
    print "one more year until you will be legal age"
else:
    print 'you are so young!'

# elif is the same as else if from other languages


# FOR and WHILE loops

for count in range (0,5):
    print "looping - ", count

#  for <counter> in <sequence or range>:
# do something

# Looping through a listcreate a new listcreateremember lists can hold many data-types, even lists!
my_list= [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world']
for element in my_list:
    print element
# the output woudl be:
# 4
# dog
# 99
# ['list', 'inside', 'another']
# hello world!

# remember this for loop?
for count in range (0,5):
    print "looping - ", count

# we can wrewrite it as a WHILE loop
count = 0
while count < 5:
    print 'looping -', count
    count += 1

# basic syntax for while loops looks like:
# while <expression>:

# break
for val in 'string':
    if val == 'i':
        break
    print val
# the outbut would be:
# s
# t
# r

# continue
for val in 'string':
    if val == 'i':
        continue
    print (val)
# output would be:
# s
# t
# r
# n
# g

# pass

class EmptyClass:
    pass
for val in my_string:
    pass


# Else

x = 3
y = x
while y > 0:
    print y
    y = y - 1
else:
    print 'final else statement'
# the output woudl be:
# 3
# 2
# 1
# final else statement

x = 3
y = x
while y > 0:
    print y
    y = y - 1
    if y == 0:
        break
else:
    print "final else statement"
# the output wou be
# 3
# 2
# 1

#Functions
def add(a,b):
    x = a + b
    return x
# the result value gets assigned to the "result" variable
result = add(3,5)
print result
# this woudl print 8

# the def keyword signifies the declaration of a functionDeclararion meand naming the function and creating the instruction
# we have named teh function 'add' and we give it two pramaters (inputs into the function)
def add(a,b):
    x = a + b
    return x
# return means we return something

# we have declared a function with the def keyword and named add, and it takes two inputs (parameters).
# An important thing to know is that th eabove code does not actually invoke the function; it just declares it/ Once you've defined your function, we can executed it by invoking or calling it using ()
print add(3,5)
# Once invoked, a function can give us an output. Soem fnctions take and inpot and some functions don't give use an output. Even if not output is produced the code inside the function can alter the program - this is called side effect.

# Function parameters
# finctions do not have to take parameters but they can optionally have one or more parameters.
# we define the da_hi function with one parameters
def say_hi(name)
    print 'Hi. ' + name

# now we can invode this function by calling its name and padding in the correct number of arguements:
# invoking the function passing in one argument
say_hi('Michael')
say_hi('Andrew')
say_hi('Jay')
# output is
# Hi, Michael
# Hi, Andrew
# Hi, Jay

def say_hi():
    return 'Hi'
greeting = say_hi()
print greeting
# this will output Hi

# two parameters
def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
# output returns 10, 5, and 15 respectively


# tuples
tuple_data = ('physics', 'chemestry', 1997, 2000)
tuple_num = (1,2,3,4,5)
tuple_letters = 'a', 'b', 'c', 'd'

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print julia[2]
# output is 1967

for data in julia:
    print data

# if we try to use item assignment to modify one of the elements of the tuple we get an error
julia[0] = "x"
# typeerror: 'tuple' object does not support item assignment.

julia = julia + ("Eat Pray Love", 2010)
#result is...
#("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia", "Eat Pray Love", 2010)

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
#result is...
#("Julia", "Roberts", 1967, "Eat Pray Love", 2010, "Actress", "Atlanta, Georgia")


# Tuple assignment
value = ("Michael", "Instructor", "Coding Dojo") #tuple packing

value = ("Michael", "Instructor", "Coding Dojo")
(name, position, company) = value #tuple unpacking
print name
print position
print company
# the output is
# Michael
# Instructor
# Coding Dojo

# There are times we experience the nedd of swapping calues and we normaly use this line:
temp = a
a = b
b = temp

# in python we can just do this:
(a ,b) = (b, a)

# The left side is a tuple variable; the right side is a tuple of values. Each value is assigned to its respectivevariable. All the expressions on the right side are evaluated before any of the assignments. Thsi feature makes tuple assignment quite versitile.
# Bu ttake note that the count of variables to the left should also have the same count of variables to the right.
(a ,b ,c, d) = (1, 2, 3)
# Value error: need more than three values to unpack

# Built in Tuple functions -

# len() - returns the number of items in a sequence
tuple_data = ('physics', 'chemistry', 1997, 2000)
print len(tuple_data)
# result is 4

# max() returns the max item in the sequence
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print max(tuple_data)
print max(tuple_num)
#result is..
#x-ray
#89

# min() returns the min item in the sequence
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print min(tuple_data)
print min(tuple_num)
#result is...
#chemistry
#15

# sum() returns the sum of the individual items
tuple_num = (67, 89, 31, 15)
print sum(tuple_num)
#result: 202

# any() returns true if there exists ant item in teh tuple which is true
# If a tuple contained (0, fales, ", 0.0, []), all of which have boolean valuse of false, then any(tuple) would be false. If a tuple contained [-1 , -2, 10, -4, 20]. all of which evaluate to ture, then any(tuple) would be true.
tuple_num = (67, 89, 31, False, 0, None)
print any(tuple_num)
#result: True

# all() returns true if all items are true.
tuple_num = (67, 89, 31, False, 0, None)
print all(tuple_num)
#result: False

# enumerate() iterates through the tuple returning 2-tuples of (index,item). This function "enumerates" all the items in a sequence: it provides a number and each element of the original sequence in a 2-tuple.
num = (1, 5, 7, 3, 8)
for index, item in enumerate(num):
    print(str(index)+" = "+str(item))
#result is...
#0 = 1
#1 = 5
#2 = 7
#3 = 3
#4 = 8

# sorted() iterates through the tuple in sorted order. Note the reutrned collection is a sorted list - not tuple.
num = (1, 5, 7, 3, 8)
print sorted(num)
#result: [1,3,5,7,8]

# reversed() iterates through the tuple in reverse order. Noite the the return value from reversed() is generic <reversed object> and must be fed into the tuple() or list() construction to create one of those objects.
num = (9, 1, 8, 2, 7, 3)
print tuple(reversed(num))
#result: (3, 7, 2, 8, 1, 9)

# Tuples as return values - Functions can alwaus only return one value but by making that value a tuple, we can effectively group together as many values as wel like and return them together. This is very useful - we often want to know some highest and lowest score, or we want to find the mean and the standard deviation, or we wnt to know the year, month, and day.
# For example, we coudl write a function that returns both the circumference and the area of a circle of radius r:
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)


# dictionaries

weekend = { "Sun": "Sunday", "Mon": "Monday" } #literal notation
vals = dict(one=1, two=2) # dict() function
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
d = { i: object() for i in range(4) } #dictionary comprehension


# Accessing values
print weekend["Sun"]
print capitals["svk"]

# or use a for loop to access all keys and values
#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.items():
     print key, " = ", data

# Nested dictionaries
# dictionaries may also include list and tuples
context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

 # to iterate through them we can use a newst for loop

for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"

# the result is like this:
# Question # 1 :  Why is there a light in the fridge and not in the freezer?
# ----
# Question # 2 :  Why don't sheep shrink when it rains?
# ----
# Question # 3 :  Why are they called apartments when they are all stuck together?
# ----
# Question # 4 :  Why do cars drive on the parkway and park on the driveway?
# ----

 # It is possible to create lists friom dictionaries by using methods items(), keys() and vlaues(). As the name implys the method keys() creates a list, which consists soley of the keys of the dictionary. While valuse() produce a list consisting if the values, items() can be used to creat a list consisting of 2-tuples of (key, value)-pairs.
 data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
#['house', 'red', 'cat']
print data.values()
#['Haus', 'rot', 'Katze']

# Dictionaries form lists - for example we have two lists, one containing the dishes and the other containing coumtries.
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

# Now we will create a dictionary which assigns a dish to a country (of course according to the common prejudices) For this purpose  we need the function zip(). teh name zio was well chosen because the two lists get combined like a zipper.
country_specialities = zip(countries, dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]

# Variable country_specialties now contains the "dictionary" in teh 2-tuple list form. Thsi form can be easily transformed into a real dictionary wiht eht functions dict()
country_specialities_dict = dict(country_specialities)
print country_specialities_dict
#Result is...
#{'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}

# there is still one questions concerning the function zip(). What happens if on of the two arguement lists containd more elements that tne other one? It's easy: Superfulrious elements will not be used, whether the extras are keys or values.
countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
