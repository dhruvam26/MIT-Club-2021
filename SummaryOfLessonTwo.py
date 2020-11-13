#MIT Club Python Lesson 2
#Res Sharpe
#11/13/20 (Definately not winging it)

"""
A lot of this lessons concepts are going to build off of what we learned last week,
so before I start teaching I'm going to do a quick review. Last weeks concepts are
CRUCIAL!! So please make sure to take the time to understand them.
"""


# These for operators make up the Python primitives, remember them!

# Hashtags are used for single line comments

"""
And triple quotes is used
for multi-line comments.
Both will be ignored by
the compiler.
"""

# ints are numbers that have no decimal point, can be both positive and negative
reviewInt = 1234

# floats are numbers that have a decimal point, can be both positive and negative
reviewFloat = 3.1415

# strings are lists of characters within single or double quotes
reviewString = "This is the reviewString"

# booleans are True and False statements
isThisAReviewBoolean = True

# print() statements allow you to print things to the compiler
print(reviewInt)
print()


"""
Now to the new Stuff!
"""

"""
To start things off, we're going to look at the input() function. input()
allows you to enter text of your choice into the compiler as code is being
run.
"""

print("Here's your first input!")
input()
print()

# Like a primitive, input can be assigned a variable.

print("Please type an example input")
exampleInput = input()
print(exampleInput)
print()

"""
Anything enteredninto an input statement will be read as a string, so if you
want it to become another primitive, you must enter the primitive you want it
to become when you define it. However if you enter something that is not the
primitive you listed, you will come back with an error.
"""

print("Here is the type of primitive exampleInput is. Notice that it is always a String.")
print(type(exampleInput))
print()

print("This next input must be an int")
intInput = int(input())
print(type(intInput))
print()

"""
At this point, you may have noticed that is seems a little inefficient to try
have to put a print statement before each input. What you can do, rather than
spreading out your input over multiple lines, is add a String at the start of
a print statement so that it can be condensed into one line.
"""

inputWithText = input("Enter whatever the hecc you feel like: ")
print(inputWithText)
print()


"""
Hopefully at this point, the concept behind inputs should be fairly simple,
because now we are going to move on to fuctions. Functions essentially have
set instructions inside of them set up to do certain tasks. To define a
function, you start with def, followed by your function name. Ex. def exampleFunction
After that you place parenthesis and a colon, so now it's def exampleFunction():
Now that the function is defined, inside it, you can do whatever you want, but
for simplicity sake, we'll just do addition. To finish the function off, you can
use the return keyword.
"""

def simpleAddition():
  intInFunction = 1 + 2
  return(intInFunction)

simpleAddition()

"""
After running this, you have most likely, but Definately realized that it
doesn't print anything to the compiler. That's because return doesn't function
the same a print statement, and it will not physically output the data to the
compiler, it will simply take note of that return value. If you want to get
the results from a function that uses a return statement, do this instead:
"""

print("The result of the simpleAddition function")
print(simpleAddition())
print()


"""
The final note with functions in this lesson is the parenthesis used when
defining them. These parenthesis aren't actually useless. When
defining a function, you can add parameters inside of the parenthesis so that
when the function is called, the user has to enter things for those parameters.
So now lets step that simpleAddition function up.
"""

def fancyAddition(a, b):
  c = a + b
  print(c)

fancyAddition(float(input("Please enter a Number: ")), float(input("Please enter another Number: ")))

"""
What you see above this text now is a version of the simpleAddition function on crack.
If you look at where the method is defined now, you see that both a and b are
defined withing the parenthesis. Like I said before, these are now method parameters,
because they are defined in the method parenthesis. Looking in the function, I have
set it up so that both a and b are added to get a new value c, which is printed. For
the record, the return statement is NOT REQUIRED. You can simply print in the function
instead of printing when you call it, this is what I prefer to do, but I figured I'd
show both ways in the lesson. Moving on, if you look below the function, you can see
the monster that is the code that calls the function. To break it down I call the
function at the start, which makes up the outer parenthesis. going into it, I have
two input statements which are seperated by a comma and changed into floats. The
statements are changed to floats because inputs come in as strings which would not
work inside the function. One of the most important things in this is the comma. 
Function calls work by assigning what you enter in the call to a parameter. With that
in mind, if you did not enter the comma, the complier would return an error because it
would read that it was only given one parameter. So really, all this does is assigns
a a float value from an input, and b a float value from another input. I hope this makes
sense, but if it doesn't, feel free to dm me on Discord so I can help you to understand it.
"""