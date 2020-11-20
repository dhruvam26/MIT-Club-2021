#MIT Club Python Lesson 3
#Res Sharpe
#11/20/20 (Definately am not winging it again)

# Super Quick Review from Last Week!

"""
The input() function allows you to enter text into the compiler as your
program is being run. Like a primitive, it can be assigned to a variable.
You can also add a string within an input to do something like explain what
you need to enter into it.
"""

exampleInput = input("Please enter some randeom characters: ")
print("Here are your random characters: " + exampleInput)



"""
Functions are created using the def keyword. From there you list the function
name, and any parameters it may have within the parenthesis next to it. Afterwards
use a colon and push enter, and the software will automatically detect that you
are creating a function and indent for you. As long as you indent, any code you
write will be in the function. To see the results of your code, you can use
either return() or print(). print() will print out your results to the compiler
with no extra steps when you call the function, but if you use return, you must
call a print() when you are calling your function
"""

def exampleFunc1(a, b):
  c = a + b
  return(c)

"""
Because I used return in the function, I had to call it with a print() statement
to see the result.
"""

print(exampleFunc1(1,2))
print() #This just adds a blank line to the compiler



def exampleFunc2(a,b):
  c = a + b
  print(c)

"""
Notice that with print() in the function, I was able to perfrom the function
without calling a print() as the function was called below.
"""

exampleFunc2(3,2)
print()


# Time for new stuff!

"""
So this weeks lesson is fairly simple. This time we are going to go over
if, elif, and else statements. if, elif, and else statements are set to work
when certain conditions are met, so I'll go ahead and give an example
"""

a = True

if(a == True):
  print("a is True!")
elif(a == False):
  print("a is False!")
else:
  print("This isn't how boolean's work!")

"""
Think about if statments like when you call a function and are filling in it's
parameters. When you call an if, you are defining the parameters for it to run.
With the example above, my parameters were that a had to be True. Because a was
True, it then executed the code within it, almost like a function (Please do not
think I am calling if a function, cause I am not! They are very different things).
Now take a look at what happens if a is False.
"""

a = False

if(a == True):
  print("a is True!")
elif(a == False):
  print("a is False!")
else:
  print("This isn't how boolean's work!")

"""
What's happening here, is that the code is checking the parameter for if, and
it realizes that it is not True. So what it does then, is that it cycles past
it and all the code inside of it and moves on to elif, which stands for else if.
elif functions the same as if, but you are only supposed to use it after you have
called an if statement before. Last but not least, there are else statements. I'm
not going to show an example of these because they are fairly simple to understand.
Else statements are what you put at the end, and they take no parameters like
unlike both if and elif statements. else statements will run if none of your if or
elif statments run.
"""



"""
You may have noticed above that I used two equal signs rather than one. To put it
in quick terms, = is used when defining something, and == is used when comparing
two things to see if they are equal, REMEMBER THE DIFFERENCE! if statements are
not limited simply to booleans like I used above. Along with ==, you can also use
!=, >=, <=, >, <. Let me explain those super quick.
"""

# != equal means not equal to, just the opposite of ==

a = 32

if(a != 34):
  print("a is not equal to 34")

# > and < still mean greater than and less than

a = 43

if(a > 45):
  print("a is greater than 45")
elif(a < 45):
  print("a is less than 45")
else:
  print("a does not meet any of the prior conditions")

# Last but not least, >= and <= are greater than or equal to and less than or equal to

a = 25

if(a >= 20):
  print("a is greater than or equal to 45")
elif(a <= 19):
  print("a is less than or equal to 19")
else:
  print("a does not meet any of the prior conditions")



"""
I know this has gone on for a while now so if you've actually been reading all
of it, you're probably sick of all this by now, so I'll be quick. All these
operators I've been listing can be used for everything but Strings and Booleans
Both Strings and Booleans can only use == and !=. Finally, every if statement can
also contain the keywords "and" or "or". What these do, is they allow you to add
multiple parameters to your if statements. and allows an if statement to work if
both parameters are met. or allows an if statment to run if either of your parameters
are valid. Just think about the English language and it makes sense.
"""

a = 20
b = 50

#I am using and here, so both parameters have to match up for code to run.
if(a == 20 and b != 50):
  print("a equals 20 and b isn't equal to 50")
else:
  print("One or both parameters above do not match up")


#Now I changed and to or, and look at what happens.
if(a == 20 or b != 50):
  print("At least one of the parameters above match up")
else:
  print("None of the parameters above match up")