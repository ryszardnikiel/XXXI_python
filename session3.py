##########################################################################################################
# Python lesson 3 - 2021.11.16
##########################################################################################################
# password = '1234'
#
# user_input = ''
#
# while user_input != password:
#     user_input = input("Enter the key to the outside, "
#                        "or you shall be locked forever!")
#
# print('We are finally out!')
# students = ['Fabrizio', 'John', 'Kasia']
# student = input('Write the student name: ')
# if student in students:
#     print("{} is in class! {} {} {} {}".format(student,
#                                                student,
#                                                'testing',
#                                                'testing3',
#                                                'another one'))
# else:
#     print(student + " is not in class!")

# Create a list called available_stock that will contain the following items:
# milk, water, bread, butter, apple, coffee
# Create a program that:
# Until customer says "done", request what product customer would like to
#               add to the "basket" with the message
#              "Please select one of the following products or type done: "
# Hint: use a while loop ("while input is not 'done', ask customer a new product")
# If the product is available, add to the basket and print message
# "Item added to the basket."
# If the product is not available, print message
# "Item not available, please select another item."
# When the customer is done shopping, print a message
# "End of shopping. Selected items: <list>"
# Print the selected items in the previous message (<list>)
# available_stock = ['milk', 'water', 'bread', 'butter', 'apple', 'coffee']
# item = ''
# basket = []
# while item != 'done':
#     print('Please select one of the following products or type "done":')
#     print(available_stock)
#     item = input()
#     if item in available_stock:
#         basket.append(item)
#         print('Item added to the basket.')
#     elif item != 'done':
#         print('Item not available, please select another item.')
#
# print("End of shopping. Selected items:")
# print(basket)

# list_example = [['Fabrizio', 18], ['Marek', 24]]
# for item in list_example:
#     print("{} is {} years old.".format(item[0], item[1]))

available_stock = [
    ['milk', 4], ['water', 0.5], ['bread', 1], ['butter', 5], ['apple', 2.1], ['coffee', 7.5]
]

item = ''
basket = []

while item != 'done':
    print('Please select one of the following products or type "done":')
    print(available_stock)
    item = input()
    for product in available_stock:
        if item in product:  # check if product = ['milk', 4]
            basket.append(product)
            print('Item added to the basket.')
            break

print("End of shopping. Selected items:")
total_value = 0.0
for basket_item in basket:
    print("{} - {} PLN".format(basket_item[0], basket_item[1]))
    total_value += basket_item[1]
print("----------------------------------------------")
print("Total value of the bill: ", total_value)
