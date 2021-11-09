##########################################################################################################
# Python lesson 2 - 2021.11.09
##########################################################################################################
my_name = 'Some Name'  # creating string variable
my_age = 18  # creating integer variable
print(my_name, my_age)

# if statement example
if my_age > 40:
    print('you are very old')
elif my_age > 18:
    print('you are adult')
else:
    print('you are teenager')

calories = 0
# What am I going to eat? - if challenge
# <=1500 calories - eat salad and eggs
# calories > 1500 and calories <=2000 - eat dumplings
# calories > 2000 - eat dumplings and dessert

##########################################################################################################
# Python List (create, append, indexing, index method, remove, pop, insert, index, list, length)
fruits = ['orange', 'banana', 'strawberry']  # create python list
print(fruits[0])  # accessing first element of fruits list
print(fruits[1])  # accessing second element of fruits list
print(fruits[-1])  # accessing last element of fruits list
fruits[0] = 'apple'  # changing value of first element of fruits list
print(fruits)

print('banana index:', fruits.index('banana'))  # get index of 'banana' element
fruits.remove('banana')  # remove banana element
print(fruits)

fruits = ['orange', 'banana', 'strawberry']  # create python list
fruits.pop(1)  # remove second item of fruits list
print(fruits)
fruits.append('banana')  # add element to the list (at the end)
fruits.insert(0, 'grape')  # add element to the list (at the beginning)
print(fruits)
print(len(fruits))  # show list length

# Python List exercises:
# 1. Create list 'countries' with three elements (Poland, Russia, Germany)
countries = ['Poland', 'Russia', 'Germany', 'Brazil', 'USA', 'Canada']
# 2. Add new element at the end of the list - Austria
countries.append('Austria')
# 3. Print the second item in the countries list.
print(countries[1])
# 4. Change the value from "Germany" to "England", in the countries list.
countries[2] = 'England'
# 5. Use the insert method to add "France" as the second item in the countries list.
countries.insert(1, 'France')
# 6. Use the remove method to remove "Russia" from the countries list.
countries.remove('Russia')
# 7. print the list
print(countries)
# ['Poland', 'France', 'England', 'Brazil', 'USA', 'Canada', 'Austria']

##########################################################################################################
# loop while (infinitive loop, break statement, continue statement)
# loop for (break statement, continue statement, range() Function)

# while loop example
some_value = 0
while some_value < 5:
    some_value += 1
    print(some_value)
# it prints:
# 1
# 2
# 3
# 4
# 5

# while loop with break statement
some_value = 0
while some_value < 5:
    some_value += 1
    print(some_value)
    if some_value == 3:
        break
# it prints:
# 1
# 2
# 3

# while loop with continue statement
some_value = 0
while some_value < 5:
    some_value += 1
    if some_value == 3:
        continue
    print(some_value)
# it prints:
# 1
# 2
# 4
# 5

# for loop example
countries = ['Poland', 'France', 'England', 'Austria']
for country in countries:
    print(country)
# it prints:
# Poland
# France
# England
# Austria

# for loop example with break statement
for country in countries:
    if country == 'England':
        break
    print(country)
# it prints:
# Poland
# France

# for loop example with continue statement
for country in countries:
    if country == 'England':
        continue
    print(country)
# it prints:
# Poland
# France
# Austria
