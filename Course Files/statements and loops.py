from os import system
import sys

system('clear')

## Conditional Statements
'''We often only want certain code to execute when a particular condition has been met.
For example, if  my pet is hungry (condition), then I will feed the pet (action).
'''

num = 0

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

input()
system('clear')

## Nested IF Statement

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

input()
system('clear')



## Match Case is included in Python 3.10
'''
type='Fruits'

match type:
    case 'Fruits':
        print("Apple")
        exit()
    case 'Vegetables':
        print("Potato") 
'''



## Loops
'''
If you need to repeat a piece of code several times to get a final result, then you might need to use a loop. Loops are a common way of iterating multiple times and performing some actions in each iteration. Python provides two types of loops:
  a)  for loops for definite iteration, or performing a set number or repetitions
  b)  while loops for indefinite iteration, or repeating until a given condition is met
'''

## For Loops
'''
for loop_var in iterable:
    # Repeat this code block until iterable is exhausted
    # Do something with loop_var...
    if break_condition:
        break  # Leave the loop
    if continue_condition:
        continue  # Resume the loop without running the remaining code
    # Remaining code...
else:
    # Run this code block if no break statement is run

# Next statement
'''
##Printing Even Values
my_list = [1,2,3,4,5,6,7,8,9,10]
i = 0
for n in my_list:
    if n%2 == 0:
        print(n)
        i+=1
else:
    print(f'{i} even number found')

input()

for letter in 'This is a string.':
    print(letter, end=' ')

input()
system('clear')



#While Loops
'''
while expression:
    # Repeat this code block until expression is false
    # Do something...
    if break_condition:
        break  # Leave the loop
    if continue_condition:
        continue  # Resume the loop without running the remaining code
    # Remaining code...
else:
    # Run this code block if no break statement is run

# Next statement

break: Breaks out of the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: Does nothing at all.

'''



x = 2

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue

input()
system('clear')
# Infinite Loop
# DO NOT RUN THIS CODE!!!! 
# while True:
#     print("I'm stuck in an infinite loop!")


