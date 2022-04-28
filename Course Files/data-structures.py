from os import system
system('clear')

#Lists in Python 
'''
Lists are just like the dynamically sized arrays declared in other languages. But the most powerful thing is that list need not be always homogeneous. A single list can contain strings, integers, as well as objects. Lists can also be used for implementing stacks and queues. Lists are mutable, i.e., they can be altered once declared.
'''

# Creating a List of strings and accessing using index
List = ["Python", "For", "All"]
print("\nList Items: ")
print(List[0])
print(List[2])

input()
system('clear')

# Creating a Multi-Dimensional List
List = [['Python', 'For'], ['All']]
print("\nMulti-Dimensional List: ")
print(List[0])

input()

#size of List
print(len(List))

input()
system('clear')

## dynamic List Operations ============================

List = []
 
# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print("List after Addition : ", end='')
print(List)

input()

# Adding elements to the List using Iterator
for i in range(8, 12):
    List.append(i)
print("List after iterative Addition: ",end='')
print(List)

input()

#Adding other data-structures in List 
List.append((5, 6))
print("List after Addition of a Tuple: ", end='')
print(List)

input()
system('clear')

# Addition of Element at specific Position (using Insert Method)
List.insert(3, 1500)
List.insert(5, 'YEEEAHH')
print("List after performing Insert Operation: ", end='')
print(List)
input()


'''
Other than append() and insert() methods, there’s one more method for the Addition of elements, extend(), 
this method is used to add multiple elements at the same time at the end of the list.
'''

List.extend([6, 'Another', 'Way'])
print("List after performing Extend Operation: ", end='')
print(List)

input()

'''
Elements can be removed from the List by using the built-in remove() function but an Error arises if the element doesn’t exist in the list. 
Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. 
'''
List.remove('Way')
List.remove(4)
print("List after performing Remove Operation: ", end='')
print(List)

input()


'''
Pop() function can also be used to remove and return an element from the list, 
but by default it removes only the last element of the list, 
to remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.

Clear() method removes all items from the list
'''

## Slicing of a List
print(List[2:6])
print(List[4:])

input()
# Negative Slicing
print(List[:-6])

input()
system('clear')

#### Other List Methods
'''
Index()	- Returns the index of the first matched item
Count()	- Returns the count of the number of items passed as an argument
Sort()	- Sort items in a list in ascending order
Reverse() - Reverse the order of items in the list
copy() - Returns a copy of the list

There are some usefull functions too
sum() - Sums up the numbers in the list
cmp() - This function returns 1 if the first list is “greater” than the second list
max() - return maximum element of a given list
min() -return minimum element of a given list
'''


## Tuples in Python
'''
Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. 

Values of a tuple are syntactically separated by ','. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. This helps in understanding the Python tuples more easily.
'''

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('I', 'Love', 'Spiderman')
 
Tuple3 = Tuple1 + Tuple2
 
print("First Tuple: ", end='')
print(Tuple1)
 
print("\nSecond Tuple: ", end='')
print(Tuple2)
 
# Printing Concatendated
print("\nTuples after Concatenation: ", end='')
print(Tuple3)

'''
Built-in-Methods
index( ) - Find in the tuple and returns the index of the given value where it’s available
count( ) - Returns the frequency of occurrence of a specified value

Built-in Function
all() - Returns true if all element are true or if tuple is empty
any() - return true if any element of the tuple is true. if tuple is empty, return false
len() - Returns length of the tuple or size of the tuple
max() - return maximum element of given tuple
min() -	return minimum element of given tuple
sum() -	Sums up the numbers in the tuple
sorted() - input elements in the tuple and return a new sorted list
tuple() - Convert an iterable to a tuple.
'''

input()
system('clear')



## Sets in Python
'''
In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.

The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
'''


## Dictionaries in Python

'''
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized. 

'''