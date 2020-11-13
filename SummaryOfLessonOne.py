#MIT Club Python Lesson 1
#Res Sharpe
#11/2/20

# To comment code use a hashtag (#). Comments in code will be ignored when it is
# run. You can use this to easily remove code that you are unsure about implementing,
# and to also explain what your code does. Commenting is considered to be a good
# practice as it allows for people to easily understand what code does when used
# correctly, so try to get into the habit of it now.

"""
You can also use triple quotes (single or double) to create multiple line comments.
Its kind of like when you quote things. Anything within the triple quotes is a part
of the comment, and will not be compiled.
"""



"""
Python has 4 primitive variable types; Ints, Floats, Strings, and Booleans. In
a nutshell, a primitive is the simplest element in a language.
"""

int
float
str
bool

"""
To start off, an int is a whole number variable. They do not contain decimals,
and can be both positive and negative.
"""

exampleInt = 1234

"""
A float, like an int can be either a positive or negative whole number, but
unlike ints, they do allow for decimals.
"""

exampleFloat = 3.14159

"""
Strings are essentially words and characters. They must be surronded by either
Single Quotes '' or Double Quotes "", and within them you can enter just about
whatever you want.
"""

exampleString = "This is an example of a string"

"""
A boolean is a True and False statement. These primitives allow for instructions
to be passed when certain conditions are met, and things of that sort. When we
eventually begin actually engineering, these will be pretty useful.
"""

isThisABoolean = True



"""
Above, I also showed examples of variables. Variables can be assigned to any of
the four primitive and some other things we'll cover later. They are basically the
name of the primitive, as shown below
"""

isThisAVariable = True
areYouSureThisIsAVariable = "Yes"

"""
Moving on, now we have print() statements. A print statement allows for the User
to print out whatever they want to the compiler, for now, just enter a primitive
or a variable                                                     Compiler ---->
"""

print(exampleInt)
print(exampleFloat)
print(exampleString)
print(isThisABoolean)
print(1)
print(43.12)
print("This string has been printed")
print(False)


# Printing a blank statement just adds an empty line to the compiler
print()

"""
To close this lesson off, I'll finish with +, -, *, and /
These operators can be used on both floats and ints, and you can also use them on
variables that contain floats or ints.
"""

# Obviously, + and - add and subtract, so I don't think I need to explain it all that much

addedInt = 53 + 2
subtractedInt = 23 - 12

addedFloat = 23.1 + 34.2
subtractedFloat = 54.8 - 34.5

print(addedInt)
print(subtractedInt)
print(addedFloat)
print(subtractedFloat)
print(addedInt + addedFloat)
print(subtractedInt-subtractedFloat)

print()

"""
Finally, theres * and /
These operators are used to multiply and divide respectively. There's not really much to
explain about them other than that
"""

multipliedInt = 2 * 3
dividedInt = int(150 / 5)

multipliedFloat = 2.5 * 25.5
dividedFloat = 60.5 / 5.5

print(multipliedInt)
print(dividedInt)
print(multipliedFloat)
print(dividedFloat)
print(multipliedInt * multipliedFloat)
print(dividedInt / dividedFloat)