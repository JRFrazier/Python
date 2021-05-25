# Python

All of my notes and projects from my Python learning journey

# Notes:

## Commenting

Add a "#" in front of the line to write a commend or comment out your code

example:

```python
# This is a comment
```

---

## Printing

Use the "print()" command to print to the terminal.

example:

```python
print("Hello World!")
```

---

## Relational Operators

```python
== # value equality / equivalence
!= # value inequality / inequivalence
< # less-than
> # greater-than
<= # less-than or equal to
>= # greater-than or equal to
```
---

## Variables

Assign a variable by stating the name of the variable then an equals "=" symbol and the value.

example:

```python
foo = "bar"
```

### Destructuring

- Allows you to assign variable names to multiple values in one line

example:

```python
def multi_output():
    x = 1
    y = 2
    z = 3
    return x, y, z

a, b, c = multi_output() # a = 1, b = 2, c = 3
```

---

## Functions

- All Python functions start with the keyword "def"
- Function bodies are indented under the function declaration
- Function names are lowercase.
- If a function name has two or more words the words are separated with and underscore "\_"

example:

```python
def example_func():
    print("Hello World!")
# this is the end of the function
```

- the "return" keyword is used to return values in a function
- You can return multiple values in a function by separating both return values with a comma.

  example:

```python
def example():
    val1 = 1
    val2 = 2
    return val1, val2
```

---

## Errors

**SyntaxError** - Something is wrong with the way the code was written

**NameError** - When the Python interpreter sees a word it does not recognize.

---

## Multiline Quotes:

```python
quote = """ this is
a multiline
quote"""
```

---

## Boolean

True = True
False = False

Equals ==
Not Equals !=

and
or
not

---

## Conditional Operater

if, elif, and else

```python
animal = "cat"

def is_cat(animal):
    if animal == "cat":
        return True
    elif animal == "dog":
        return False
    else:
        return "please enter cat or dog"
```

try and except

```python
def raises_value_error():
  raise ValueError

try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")
```

---

## Lists

- Ordered set of objects (think "array" in JS)

example:

```python
numbers = [1, 2, 3, 4]
```

### Zip

- will combine items in 2 or more lists

example:

```python
name = ['ray', 'sam', 'lue']
age = [16, 17, 18]
height = [56, 67, 50]

name_age_height = list(zip(name, age, height)) # the list function converts the zip from a pointer to a list

print(name_age_height) # will output [('ray', 16, 56), ('sam', 17, 67), ('lue', 18, 50)]
```

### Append

- Use _.append()_ to add to a list

example:

```python
numbers = [1, 2, 3, 4]

numbers.append(5)

print(numbers) # [1, 2, 3, 4, 5]
```

### Combining Lists

- Use the _+_ to combine 2 lists together

example:

```python
numbers = [1, 2]
new_numbers = numbers + [3, 4]
```

### Range

- To access a range from a list you can use the _range()_ function combined with a for loop.

example:

```python
range1 = range(10)

print(list(range1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range2 = range(2, 10)

print(list(range2))) # [2, 3, 4, 5, 6, 7, 8, 9]

range3 = range(2, 9, 2)

print(list(range3))) # [2, 4, 6, 8]
```

### Length

- Use the "len()" function to get the length of an object

example:

```python
my_list = [1, 2, 3, 4]

print(len(my_list)) # 4
```

### Last Element

- To ge the last element of a list use -1 in the square brackets

example:

```python
my_list = [1, 2, 3, 4]

print(my_list[-1]) # 4
```

### Slicing lists

- To select a specific range from a list you can use the slice option (object[start:end])

example:

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letters[1:5]) # ['b', 'c', 'd', 'e']

# print from the beginning of the list to d
print(letters[:4])

# print from c to the end of the list
print(letters[2:])

# print last 2 elements of letters
print(letters[-2:])
```

### List Functions

```python
foo = [1, 2, 3]

foo.append(4) # adds 4 to the end of foo

foo.pop() # removes 4 from the end of foo

```

### Counting elements

- To count how many times a specified element appears in a list you can use the ".count()" function.

example:

```python
letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']

# Count how many times the letter 'i' shows up in the list 'letters'
print(letters.count('i')) # 4
```

### Sorting Lists

- To sort a list use the '.sort()' function.

_Note: this function will permanently sort the list. If you want to make a separate sorted list without affecting
the original list see 'sorted'._

example:

```python
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

print(names.sort()) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

# Sort in reverse

print(names.sort(reverse=True))) # ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']
```

- to create a separate sorted list use the 'sorted(list)' function

example:

```python
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

sorted_games = sorted(games)

print(sorted_games) # ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']

print(games) # ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
```

### Checking if Item Exists

- To determine if a specified item is present in a list use the "in" keyword:

example:

```python
the_list = ["apple", "banana", "cherry"]

if "apple" in the_list:
  print("Yes, 'apple' is in the list")
```

---

## Tuples

- Allows you to store multiple pieces of data inside of it
- Tuples are immutable

example:

```python
my_info = ('Justin', 38, 'Programmer') # This is a tuple

print(my_info) # ('Justin', 38, 'Programmer')
```

### Accessing elements of a Tuple

- Same as a list

  example:

```python
my_info = ('Justin', 38, 'Programmer')

print(my_info[0]) # Justin
print(my_info[1]) # 38
```

### Tuples are Immutable

example:

```python
my_info = ('Justin', 38, 'Programmer')

my_info[0] = "JR" # This would invoke an error
```

### Assigning elements of Tuple to variables (AKA: Unpacking a Tuple)

example:

```python
my_info = ('Justin', 38, 'Programmer')

name, age, occupation = my_info

print(name) # Justin
print(age) # 38
print(occupation) # Programmer
```

### Creating a one element Tuple

example:

```python
one_el_tuple = (4,) # The trailing comma is required to store this as a tuple
```

---

## Loops

- Loops are a way of repeating a set of code many times.
- There are 3 types of loops (for, while, and list comprehension)

### For Loops

- iterates over a list

example:

```python
dog_breeds = ['french bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

# time for the loop
for breed in dog_breeds:
  print(breed)

# output will be a list of each breed in the list dog_breeds
```

- you can also run a loop for a number of times using "range()"

example:

```python
# Print Hello 3 times

for i in range(3):
  print("Hello")
```

#### Breaking the loop

- you can stop a loop from within using _break_

example:

```python
list_of_names = ['Justin', 'Shere', 'Harper', 'Delonte', 'Kaleb', 'Lorena']

for name in list_of_names:
  if name == "Harper"
    print("That is my daughter")
    break # this will stop the loop when it gets to the name "Harper"

print("End of search!")
```

#### Skipping items in a loop

- you can skip items by using _continue_

example:

```python
big_number_list = [1, 2, 30, 4, 5, 60, 7, 80, 9, 10]

for i in big_number_list:
  if i < 10:
    continue
  print(i) # will print only 30 60 80 and 10
```

### While loops

- Perform a set of code until some condition is reached.
- Can be used to iterate through lists

example:

```python
foo = ['a', 'b', 'c', 'd', 'e', 'f']

index = 0

while index < len(foo):
  print(foo[index])
  index += 1
```

- You can also run an infinite loop using a _while True_ loop

```python

while True:
  print("To Infinity and Beyond!")

```

### _List Comprehension_

- Short hand for running a conditional in a for loop against a list

example:

```python
foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

bar = [num for num in foo if (num % 2) != 0]

print(bar) # [1, 3, 5, 7, 9]

add_one_to_foo = [num + 1 for num in foo] # increases each number in foo by one

print(add_one_to_foo) # [2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## Strings

- Strings are similar to lists in that each character in a string has an index starting with zero 0.

- Strings in Python are _immutable_

example:

```python
my_name = "Justin"

first_initial = my_name[0]

print(first_initial) # J
```

### Slicing a String

- You can slice a string using the following syntax:

```python
my_name = "Justin"

print(my_name[0:2]) # Ju

print(my_name[1:4]) # ust

```

### Concatenating Strings

```python
first_name = "Justin"
last_name = "Frazier"

full_name = first_name + " " + last_name

print(full_name) # Justin Frazier
```

### Find The Length of a String

```python
my_name = "Justin"

print(len(my_name)) # 6
```

### Check For Words or Letters in String

```python
test_string = "This is a test string"

"test" in test_string # True

"Test" in test_string # False - as you can see this is type sensitive
```

### String Methods

- String methods will create new strings and never mutate the original string.

String Formatting:

```python
some_string = "Hello World"

some_string.lower() # returns the string in all lowercase
some_string.upper() # returns the string in all uppercase
some_string.title() # returns the string with the first letter of each word in uppercase
```

### Splitting Strings

- To split a string use the \n (new line) or \t (vertical tab) to split strings.

example:

```python
smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print (chorus_lines) # ['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"]
```

### Joining a String

- use ".join()" to join a string

example:

```python
usage: 'delimiter'.join(list_you_want_to_join)

ingredients = ['steak', 'butter', 'salt', 'pepper', 'garlic', 'sage', 'oliv oil']

print(', '.join(ingredients)) # 'steak, butter, salt, pepper, garlic, sage, olive oil'
```

### .strip() Method

- This method will, by default, strip white spaces from the beginning and end of a string unless an argument is provided. If an argument is provided this method will ONLY strip the character provided in the argument from both ends of the string.

example:

```python

my_name = "    Justin Frazier    "

print(my_name.strip()) # "Justin Frazier"
```

### .replace() Method

- This method allows you to replace any space or character in a string with something else.

example:

```python

with_spaces = "You got the kind of loving that can be so smooth"

print(with_spaces.replace(' ', '_')) # 'You_got_the_kind_of_loving_that_can_be_so_smooth'
```

### Replace with case insensitive

example:

```python
import re

str_replace = re.compile("this", re.IGNORECASE)

print(str_replace.sub("that", "You can get with that, or you can get with that")) # You can get with this, or you can get with that
```

### .find() Method

- use to find index of specified string in a string.

example:

```python

greatest = "You are the greatest!"

print(greatest.find('greatest')) # 12
```

### .format() Method

- enables you to include variables within a string.

example:

```python
def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

print(favorite_song_statement("Satellite", "Dave Matthews"))
```

### Convert String to Float

- Use the float() method to convert a string into a float

example:

```python
foo = "100"
print(float(foo)) # 100.0
```

---

## Modules

- To import a module use the following syntax:

```python
from module import object # use this syntax if you are exporting a specific object from a module

import module # use this syntax if you would like to import the entire module
```

- To see all _objects_ that are available in an module use the following syntax:

```python
from datetime import datetime

print(dir(datetime)) # ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
```

### Aliasing A Module Name

```python
import module as new_name
```

---

## Virtual Environments w/ pipenv

Read about it here:
https://docs.pipenv.org/en/latest/#

---

## Dictionary

- is an unordered set of key: value pares. (Like an object in JS)

example:

```python
foo = {"name": "Justin", "job": "Developer"}
```

### Adding A "Key: Value" Pair

example:

```python
foo = {}

foo["name"] = "Justin"
```

### Adding Multiple Keys

- Use .update() to add multiple "Key: Value" pairs to a Dictionary.

example:

```python
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}

print(sensors) # {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}
```

### List Comprehensions to Dictionaries

- You can create a dictionary from 2 lists using list comprehensions to dictionaries

example:

```python
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}

print(drinks_to_caffeine) # {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}
```

### Try/Except to Get Key

- Check to see if a key is available in a dictionary and if not return a custom value.

example:

```python
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

def check_caffeine_level(source):
  try:
    print(caffeine_level[source])
  except KeyError:
    print('Unknown Caffeine Level')

check_caffeine_level('matcha') #  'Unknown Caffeine Level'

```

### Get a Key from Value

- Use the .get() method to search for a value instead of the my_dict[key] notation we have been using.

example:

```python
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")
```

- you can also specify a value to return if the key doesn't exist.

example:

```python
 building_heights.get('Kilimanjaro', 'No Value') # will return "No Value"
```

### Remove a Key

- Use .pop() to remove a key from a dictionary

example:

```python
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

raffle.pop(320291, 'No Prize') # will remove key 320291 from the "raffle" dictionary or it will return "No Prize" is the key doesn't exist

```

### Get All Keys

example:

```python
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores)) # This will print ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
```

- There is another method of doing this using .keys(), however this will return _dict_keys_ which is an imutable object of the key values.

example

```python
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(test_scores.keys()) # will print dict_keys(['Grace', 'Jeffrey', 'Sylvia', 'Pedro', 'Martin', 'Dina'])
```

### Get All Values

- Use the .values() method to return all values in a dictionary

```python

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

print(num_exercises.values()) # Will print dict_values([10, 13, 15, 22, 19, 18, 18])

```

### Get All Items In A Dictionary

- Use the .items() method.
- Each item returned by .items() will be a tuple _(key, value)_

```python
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

print(pct_women_in_occupation.items()) # This will return dict_items([('CEO', 28), ('Engineering Manager', 9), ('Pharmacist', 58), ('Physician', 40), ('Lawyer', 37), ('Aerospace Engineer', 9)])
```

---

## Classes

- A _Class_ is a template for a data type, that describes the kinds of information that class will hold and how a programmer will interact with that data.

- Define a _Class_ in Python using the Keyword "class" followed by the name of the class

- Class names should be Capitalized in accordance to the [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/#class-names)

example class:

```python
class Foo:
  pass
```

> Note: The _pass_ keyword acts as a place holder for code that's not yet present where something is required to prevent an _IndentationError_

- To use as class you first have to _Instantiate_ it.

- You can instantiate a class by assigning it to a variable:

example class instantiation:

```python
class Foo:
  pass

bar = Foo()
```

### Class Variables

- A _class variable_ is a variable that's that same for every instance of the class.
- When we want the same data to be available to every instance of a class we use a class variable.

```python
class Musician:
  title = "Rockstar" # This is a class variable

drummer = Musician() # Instantiating the class

print(drummer.title) # Prints our "Rockstar"
```

### Methods

- _Methods_ are functions that are defined as part of a class.
- The first argument in a "Method" is always the object that is calling the method.
- Convention recommends that we name this first argument (self).

```python
class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation() # Prints "Dogs experience 6 years for every 1 human year."
```

- Methods can take on additional arguments aside from self.

### Dunder Methods (AKA: Magic Methods)

- These methods are called dunder methods because they are surrounded by double underscores `__init__`
- These methods have special behavior and behave differently form regular methods.

`__init__` (Constructor Method)

- used to initialize a newly created object.
- called every time the class is instantiated.
- Methods that are used to prepare an object being instantiated are called constructors.

example:

```python
class Hello:
  def __init__(self):
    print("Hello")

say_hello = Hello() # This will print "Hello" every time the class is instantiated

```

`__repr__`

- Tells Python what we want the _string representation_ of the class to be.
- It can only have on parameter of _self_

example for strings:

```python
class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

tyler =  Employee("Tyler Durden")

print(tyler) # prints out "Tyler Durden"
```

example for numbers:

```python

class Number:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return repr(self.number)

one = Number(1)

print(one) # 1
```

'**add**'

- allows you to use the "+" symbol to add two instances of a class together.

### Instance Variable

- Instance variables are variables that are specific to the object (instance of a class) they are attached to.

example:

```python
class Foo:
  pass

hey_foo = Foo()
hi_foo = Foo()

hey_foo.greet = "Hey"
hi_foo.greet = "Hi"

print(hey_foo.greet) # will print "Hey"
print(hi_foo.greet) # will print "Hi"
```

### Verifying if object has attribute

- We can use either _getattr()_ function or the _hasattr()_ function.
- The _getattr()_ function will return the attribute if it exists.
- The _hasattr()_ function will return the _True_ or _False_ if the attribute does/doesn't exist.

```python

class NoAttr:
  pass

attributeless = NoAttr()

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value
```

### List Object's Attributes

- Use the _dir()_ function to list the attributes of and object.

example:

```python
dir("this")
## ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### Inheritance

- Allows you to reuse parts of another classes definition inside of another class.
- Everything from the class you are inheriting (Parent Class) will be brought into the new class. Unless you change a value that was passed from the parent class in the new class everything will be the same.

The example below shows a class called "Admin" that is using the _constructor_ from the class "User".

```python
class User:
    is_admin = False

    def __init__(self, user_name):
        self.username = user_name


class Admin(User):
    is_admin = True
```

### Exceptions

- An _Exception_ is a class that inherits from Python's **Exception** class
- These can be validated by using the _isssubclass()_ function.
  - _isssubclass()_ is a Pythhon built-in function that takes two parameters and returns **True** if the first argument is a subclass of the second argument, esle it will return **False**.

```python

def get_food_from_fridge():
  if refrigerator.cooling == False:
    raise RefrigeratorException
  else:
    return food

def heat_food(food):
  if microwave.working == False:
    raise MicrowaveException
  else:
    microwave.cook(food)
    return food

try:
  food = get_food_from_fridge()
  food = heat_food(food)
except KitchenException:
  food = order_takeout()

```

### Super()

- Allows you to add extra logic to the existing method.
- **super()** gives us a _proxy method_.

```python
class Batman:
    def __init__(self):
        self.wealth = "Rich"
        self.armor = "Batsuite"
        self.lives = "Gotham"


class IronMan(Batman):
    def __init__(self):
        super().__init__()
        self.armor = "IronMan Suit"
        self.lives = "Malibu"
```

### Interface

- An interface in PYthon usualy refers to the names of the methods and the arguments they take.

### Polymorphism

- _Polymorphism_ is when the same code performs different actions dependingon the data type.

example:

```python
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list)) # 4
print(len(a_dict)) # 1
print(len(a_string)) # 21
```

---

## Nodes

- Nodes form the vasis of linked lists, stachs, queues , trees etc...
- An individual node contains data and links to other nodes
- Data within a node can be a veriety of types
- The links or link within the node are referred to as _pointers_
- If the link or pointer is null this indicates that you have reached the end of THAT node of link path
- nodes may only be linked to or from a single other node.
  - if you remove a single linkto a node, that nodes data and any linked nodes could be lost
  - when this happens to a node, it is considered an _orphaned node_

### Nodes In Python

Below is a class and 3 instances of that class where each instance has it's own value and a link to another instance of that class.
This example demonstrates how links can be created from one class (Node) to another.

```python
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  def set_link_node(self, link_node):
    self.link_node = link_node

  def get_link_node(self):
    return self.link_node

  def get_value(self):
    return self.value

# Add your code below:
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data) # "enjoys spending time in movie lots"
print(wackos_data) # "has a penchant for hoarding snacks"
```

---

## Linked Lists

- Are comprised of nodes
- The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
- Can be unidirectional or bidirectional
- Are a basic data structure, and form the basis for many other data structures
- Have a single head node, shich serves as the first node in the list
- Require some maintenance in order to add or remove nodes
- Are not required to be stored in sequential order in memory

example:

```python
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
```

---

## Stacks

- A stack is a data structure which contains and ordered set of data
- There are 3 methods for interacting with data in a stack (Push, Pop, and Peek):

  - Push - adds data to the "top" of the stack
  - Pop - returns and removes data from the "top" of the stack
  - Peek - returns data from the "top" of the stack but does not remove it

- Stacks mimic a physical "stack" of objects.
- The method in which items are placed and removed from a stack is called "Last In First Out" or LIFO.
- Stack have a defined size.
- A _Stack Overflow_ occurs when data is pushed onto an already full stack.

example:

```python
ifrom node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit

  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0

```
