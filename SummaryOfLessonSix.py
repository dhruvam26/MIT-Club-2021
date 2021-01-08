#MIT Club Python Lesson 6
#Res Sharpe
#12/17/20

"""
No review today. We're just gonna just straight into it because I'm sure a lot of
people have a lot studying they need to do for exams, cause those are fun. Today we're
going to start using lists. A list is essentially a group of variables all combined
into one variable. Before break, I breifly mentioned indexes to everyone. The position
of variables within a list are called indexes, they start with 0, and move upwards
from there, REMEMBER, THEY DO NOT START WITH 1! You can enter any of the Python
primitives that you would like in any order. To start a list of, you first enter the
name of the list, followed by an equal sign and brackets. Within those brackets,
you can begin to enter any primitive you want, as long as they are seperated with commas.
"""

intList = [1, 2, 3, 4, 5]
doubleList = [1.1, 1.2, 1.3, 1.4, 1.5]
booleanList = [True, False, True, False, True]
StringList = ["Index 0", "Index 1", "Index 2", "Index 3", "Index 4",]
mixedList = [1, 2.5, True, 3, "Index 4", False]

"""
With lists, one nice thing to know is how to use the len() function. What len() does,
is it counts how many items are located inside of the list.
"""

print(len(intList))
print(len(doubleList))
print(len(booleanList))
print(len(StringList))
print(len(mixedList))

print()

"""
Moving on, there is a lot of things you can do with lists. So we're going to start with
accessing items within them. When you want to call an item within a list, you would do
listName(indexNumber). You can also access items within a certain amount of indexes using
listName(firstIndex:unincludedLastIndex). You can do the same thing if you want to read
everything starting from a certain index or reading everything before a certain index using
listName(startingIndex:) or listName(:endingIndex). Indexes can also be negative, and
with a negative index, rather than starting at the front, it starts at the end. Rather than
using 0, negative indexes use -1 to define the start index, which would be the final item
inside of the list. You can also add another : at the end and the number you put after it
will be what the indexes are counted through by. Now I will give examples of literally all
of that below.
"""

exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Here is the list everything is using: ", exampleList)
print()

#Prints 5
print(exampleList[4])

#Prints 5-9
print(exampleList[4:9])

#Prints 3 and Everything Afterwards.
print(exampleList[2:])

#Prints 4 and Everything Before.
print(exampleList[:4])

print()

#Prints 7
print(exampleList[-4])

#Print 2-6
print(exampleList[-9:-4])

#Prints 8 and Everything Afterwards.
print(exampleList[-3:])

#Prints 6 and Everything Before.
print(exampleList[:-4])

print()

#Prints every item 2 apart from index 0
print(exampleList[::2])

print()



"""
So, now that all that stuff is done, we're going to look at different built in methods
that exist within Python. To start off, we are going to look at methods that allow you
to change indexes in a list. First off is insert(). Insert allows you to enter anything you
want into an index of your choice. Using insert() will move whatever variable was in the
index to the right. To use insert(), you would do:
indexName.insert(index, whatYouAreInserting)
"""

exampleList = [1, 2, 4, 5]

print("Here's the new exampleList: ", exampleList)

exampleList.insert(2, 3)

print(exampleList)

print()

"""
There is also the append() method that will add whatever you want it to to the end of
the list.
"""

exampleList = [1, 2, 3, 4]

print("Here's our exampleList: ", exampleList)

exampleList.append(5)

print(exampleList)

print()

"""
Not a method, but you can also manually change what is located within an index by
calling the index and setting it like you would any primitive.
"""

exampleList = [1, 2, 3, 4]

print("Here's yet another exampleList: ", exampleList)

exampleList[3] = "This was originally a 4"

print(exampleList)

print()



"""
Now looking at the methods and other things that remove variables from a list,
there are 4 in mind; remove(), pop(), del, and clear. Starting with remove, you are
able to remove a specific item in a list, not an index
"""

exampleList = [1, 2, 3, 4, 5]

print("Here's our new exampleList: ", exampleList)

exampleList.remove(3)

print(exampleList)

print()

"""
Now looking at pop(), unlike remove, you select a specific index within the list
to delete. By default, pop() will remove the final index if you do not specify which
index you want it to delete
"""

exampleList = [1, 2, 3, 4, 5]

print("I've given up on trying to write different text here: ", exampleList)

exampleList.pop(0)

print(exampleList)

print()

# del allows you to delete an index that you choose to specify, or the whole list.

exampleList = [1, 2, 3, 4, 5]

print("Here's our new exampleList: ", exampleList)

del exampleList[3]

print(exampleList)

print()

exampleList = [1, 2, 3, 4, 5]

print("Here's our new exampleList: ", exampleList)

del exampleList
print()

#I can't run this now, because I have literally deleted exampleList from existance.
#print(exampleList)

"""
Finally, there is the clear method. Unlike del, clear removes all the variables within
the indexes, but it does not completely delete the list.
"""

exampleList = [1, 2, 3, 4, 5]

print("Here's our new exampleList: ", exampleList)

exampleList.clear()

print(exampleList)

print()

"""
The thing about lists is that there is a ton of things you can do with them, so it's
very hard for me to guage how long these lessons will take, but just to be on the safe
side, I'm going to wrap this lesson up here, there is still a lot more that needs to be done, but that'll happen next week.
"""