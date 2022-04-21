from os import system


system('clear')

'''
Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task. 
The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, 
we can do the function calls to reuse code contained in it over and over again. 

Functions can be both built-in or user-defined. It helps the program to be concise, non-repetitive, and organized.
'''

def my_func():
  print("Welcome to Python Class")
  print(3*'\t' ,'Thanks')

my_func()


input()
system('clear')

#Arguments in Python Function
def myFun(x, y=50):
    print("x is : ", x)
    print("y is : ", y)

myFun(20)

input()

myFun(50,40)

input()

#keyword Arguments
myFun(y='1000', x='Something New')

input()
system('clear')