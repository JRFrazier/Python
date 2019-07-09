# Python

All of my notes and projects from my Python learning journey

# Notes

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
````

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

tye and except

```python
def raises_value_error():
  raise ValueError

try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")
```
