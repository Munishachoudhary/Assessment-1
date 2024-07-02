phone_book = {}  
def add_contact(name, number):
    if name in phone_book:
        print(f"Contact '{name}' already exists")
    else:
        phone_book[name] = number
        print(f"Contact '{name}' with number '{number}' added successfully.")

def search_contact(name):
    if name in phone_book:
        print(f"Name: {name}, Number: {phone_book[name]}")
    else:
        print(f"Contact '{name}' not found in the phone book.")

def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found in the phone book.")

while True:
    print("1. Add ")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")

    select  = input("Enter your choice (1-4): ")

    if select == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif select == "2":
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif select == "3":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif select == "4":
        print("Exit")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 4.")