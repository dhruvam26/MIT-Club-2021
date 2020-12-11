a = 10
b = 5

if(a < b):
  print("a is less than b")
elif(a == b):
  print("a is greater than or equal to b")
else:
  print("this code is a failure like me")

print()

a = 0

while(a < 10):
  a += 1
  print("This code has been iterated through", a, "times.")

print()

a = 0
b = True

while(b):
  a += 1
  print("This code has been iterated through", a, "times.")
  if(a >= 10):
    print("The break condition has been met")
    break
  print("print go brrr")


print()

a = 0
b = 35

while(a < 10 or b > 20):
  a += 1
  b -= 1
  print("a is equal to", a)
  print("b is equal to", b)
  print()



exampleString = "This is an example"
a = ""

for character in exampleString:
  print(character)
  if (character == "e"):
    break
  a += character
  print()

print(a)