# Wish List to Santa
#
#
# It's a very busy time of year for Santa.
# He needs to automate all the wish requests in a python program to make sure he can track all the wishes and do not deliver it more than once.
# Also, Santa needs to be able to export the information to the next day.
#
# Create a program with the following features:
# 1. Add item to the wish list to a person
# - Use a dictionary that the key will be the name of the person
# - Use a list that contains items that are made of:
# - Name of item (e.g. Playstation 5)
# - Delivery status (True or False)
# 2. Deliver presents for a person
# - Search for the person, and deliver all pending items, and print them on the screen
# 3. Print all pending gifts
# 4. Export the database to a json file

# Add item -> function
# Deliver -> function
# Print pending -> function
# Export -> function

# Generate one function for each feature.
# Create a program that will run under a while loop.
# If santa says "end", program should ask if Santa wants to export the database before shutdown.


import json
from pathlib import Path

DB_FILE_NAME = 'database.json'


def save_database(db):
    with open(DB_FILE_NAME, 'w') as fp:
        json.dump(db, fp)
    print("Database saved successfully!")


def load_database():
    my_file = Path(DB_FILE_NAME)
    if my_file.is_file():
        with open(DB_FILE_NAME) as f:
            db = json.load(f)
    else:
        db = {}
    return db


if __name__ == '__main__':
    db = load_database()

    while True:
        option = input(
            "Enter one of the following or type 'end' to exit:\n1- Add item to wish list\n2- Deliver presents\n3- Print all pending gifts\n4- Save database\n")
        if option == '1':
            person_name = input('Type the name of the person: ')
            gift = input("What is the requested gift? ")
            add_gift_to_wishlist(db, person_name, gift)
        elif option == '2':
            person_name = input('Type the name of the person: ')
            deliver_gifts(db, person_name)
            pass
        elif option == '3':
            print_pending_gifts(db)
            pass
        elif option == '4':
            save_database(db)
        elif option == 'end':
            export = ''
            while export.lower() not in ('y', 'n'):
                export = input("Would you like to save the database before leaving (y/n)?")
                if export == 'y':
                    save_database(db)
                elif export == 'n':
                    break
            break
        else:
            print("Please enter a valid option")
