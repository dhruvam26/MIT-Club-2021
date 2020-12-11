#MIT Club Lesson 5
#Res Sharpe
#12/11/20

"""
Today is kinda going to be a garbage dump of things that are nice to know but I
haven't covered yet either cause I haven't been able to fit it in, or cause I fogot about
it. This is mainly because I can't always cover everything I want during our club meetings
so I try and cram in the important stuff. All that we are going to go over are some
miscellaneous statements/functions for loops, the Modulo operator, and Python
escape characters. There are a few major statements that can be used in while and for
loops that I'm going to start off with. First, there is the continue statement. All the
continue statement does is stop a programs current iteration and move on to the next.
"""

exampleString = "Haha, example string go brrr"
finalString = ""

for character in exampleString:
  if (character == "a" or character == "e" or character == "i"):
    continue
  else:
    finalString += character

print(finalString)

print()

a = 0
b = 1
c = 0

while(a < 10):
  if(b >= 5):
    a += 2
    c += 1
    print(a)
    print("The number of iterations is equal to: ", c)
    continue
  a += 1
  b += 1
  c += 1
  print(a)
  print("The number of iterations is equal to: ", c)

"""
There is also a statement called pass. All pass does is it prevents the code from
breaking if you don't enter anything into it. ngl, I don't really know all
the specifics behind it because I have never used it before, but now you know.
"""

exampleText = "I typed this text"

for character in exampleText:
  pass

print()

"""
One more big thing with for loops that my last two brain cells did not remember
last Friday is the range() funtion. Using range() you are able to iterate through
numbers. This gets us into the topic of Python indexes. When you enter a number into
the range() function, it starts at 0 by default. So by entering range(6), that would
actually go from 0-5. Observe:
"""

for x in range(6):
  print(x)

print()

"""
When you use range, you can also set up the specific number you want it to go through
using range(x,y) where x and y are the first and last numbers you want to iterate
through.
"""

for x in range(1,10):
  print(x)

print()

"""
If you look at the output in the compiler, you'll notice that it doesn't print 10 out.
That's not an issue with the code, that's just how Python works, so if you want to
iterate through a range like that, you must put one number above the one you want to
end on. One last thing with range() is that you can set the amount you want to increment
by with range(x,y,z) x and y respectively being the first and last values you want to
iterate through and z being the value you want to iterate by. One more thing to quickly
note is that it will skip any numbers that do not perfectly line up with that iteration
value, which is why it doesn't print 20 out in the compiler when you run this code.
"""

for x in range(1,21,2):
  print(x)

print()



"""
So moving on to the Modulo operator (more commonly known as mod) %, this works the same
as the division sign but instead of returning an answer, it will return the exact
remainder of what you divide by
"""

a = 37 % 5
print(a)

print()

b = 67438 % 3
print(b)

print()



"""
Now to wrap this up, we're going to look at some of the Python escape characters. You
won't always necessarily use these, but it's nice to know if you want to format your
code so it looks nice in the compiler. The purpose of escape characters is to allow you
to insert characters that are illegal into a String.

Here is everything that I think we're gonna need:

\': insert a single quote
\": insert a double quote
\\: insert a backslash
\n: insert a new line
\t: insert a tab (Just a few spaces)

"""

exampleString = '\'This is the same thing, but single quotes!\''
print(exampleString)
print()

exampleString = "\"These are double quotes in a String!\""
print(exampleString)
print()


exampleString = "This is just a backslash in the String, nothing special --> \\"
print(exampleString)
print()


exampleString = "This is the top line,\nand this is now the bottom line."
print(exampleString)
print()


exampleString = "\tI inserted a tab into this String!"
print(exampleString)
print()
