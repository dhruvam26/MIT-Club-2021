#MIT CLub Python Lesson 4
#Res Sharpe
#12/4/20

"""
So to start things off, once again, we're going to begin with a review.

So last week we discussed if() statements. The concept behind them is fairly simple.
You feed in parameters like in a method, and if you code meets those parameters, it
will run. Along with if() there are also elif() which will run if your code doesn't
meet your first parameter but meets another one specified within those parenthesis.
At the end of it all, you can also use an else statement which will run if literally
everything else fails. Within the parenthesis for if() statements, you can use things
like != (compares to see if two things are not equal), == (compares to see if two things
are equal), > and < (Checks to see if something is greater than or less than), and finally >= and <= (Greater than or equal to and less than or equal to.). The if statements will
then use these operators and convert them to boolean statements if the condition is met.
"""

a = 12
b = 16

if(a >= b):
  print("a is greater than or equal to b")
elif(a == b):
  print("a is equal to b")
elif(a <= b):
  print("a is less than or equal to b")
else:
  print("Can't make out what the hecc a and b are.")

print()


"""
You can also use "and" or "or" to have multiple parameters in an if statement. In
super simple terms, "and" requires that both parameters are met, wheras "or" only
requires one of the parameters to be met.
"""

a = 30
b = 65

if (a >= 20 and b <= 50):
  print("a is greater than or equal to 20 and b is less than or equal to 50")
else:
  print("One or more parameters are not met")

print()

if(a >= 20 or b <= 50):
  print("One or both parameters are met")
else:
  print("None of the parameters are met")

print()

# So that's last lesson in a nutshell, now it's time for new stuff

"""
So today, we're going to discuss loops. Loops are, in simple terms, code that will run
over and over until something happenes in it to stop it. There are two types of loops
that we are going to go over; while() loops and for loops. I'll begin with while()
loops. while() within the parenthesis of a while loop, you write a statement that the
compiler can read as a boolean. within the code inside of the while loop, you must
(emphasis on must) make your code so that the boolean value in parenthesis can switch
at a certain point and end the loop or (empasis on or) use an if() statement that uses
the break statement to end a loop. Something that will come in pretty handy for loops
is the += and -= operators, which can either add or subtract something and redefine the
variable as the answer that results from it. Here is an example of a while loop.
"""

a = 0

while(a < 10):
  a += 1
  print("This program has looped through", a, "times.")

print()

"""
Breaking this loop down, you see that as my parameter for it I have (a < 10). So what
this means is that as long as a < 10, my code within the loop will run. Looking inside
the loop, you can see that I started it with a += 1, this line basically redefines a by
adding a 1 to the current a value. After that, I have a print() statement that lists the
a value which is now equal to the amount of times that the code has run through the loop.
So if you look at the compiler it just repeats this code until the a value is 10. If you
don't feel like setting up you while loop like that, you can use a break statement within
an if statement which will end the loop.
"""

a = 0
b = True

while(b):
  a += 1
  print("This program has looped through", a, "times.")

  if(a >= 10):
    print("The break statement has been reached, the loop will end here.")
    break

print()

"""
One more thing that you can do that I will not include here because I don't want to,
is that you can use "and" or "or" when defining the parameters for a while() loop just
like an if() statement.
"""

"""
Finally there are for loops. for loops will basically increment through what you enter
into them, which can be a String, a range of numbers, or a list (we haven't been over
these yet, but we will in a few weeks). Essentially with most things, it goes through
literally every single character that the thing you enter has to offer (or index if
we're talking about lists, again we'll go over those in a few weeks). For now, we'll
stick with strings. For a for loop, you begin by saying for, after you put a variable
name for whatever the specific thing you are incrementing through is. This defines the
variable name, it is not what you are incrementing through. After that you put in and
last but not least the variable that you are incrementing through. Look at this example
loop using a string.
"""

a = "example string go brrr"
b = ""

for character in a:
  if (character == "a" or character == "e"):
    b += character.upper()
  else:
    b += character

print(b)
print()

"""
Currently, what this code does, is it increments one character at a time through the
String assigned to a, and adds the character to an empty String, but if the character
is equal to a or e it adds that character but capitalized. Once again, the break
statement can be used to exit here too.
"""

exampleString = "This is an example"
a = ""

for character in exampleString:
  print(character)
  if (character == "e"):
    break
  a += character
  print()

print(a)