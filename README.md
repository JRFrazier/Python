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

### Classes

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
