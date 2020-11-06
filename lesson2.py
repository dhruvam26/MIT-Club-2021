#A function is a method that does what you instruct to
def funcX():
  print('Yay I made my first function!')

#Functions can take in input from you the user using input()
def funcY(userInput):
  print(f'Hi {userInput}!')
userInput = input('What is your name: ')
funcY(userInput)

#You can do math using functions and inputs
def funcZ(numberInput):
  print(f'{numberInput} + 1 = {numberInput + 1}')
numberInput = int(input('Give me a number: '))
funcZ(numberInput)

