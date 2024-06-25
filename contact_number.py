# Hi everyone! 
# Here we are with a new mini but important code together, 
# that at least once or towice in a day we use it in our cell phons.
# _____----- that is: contact member -----______


# FIRST we define a class by the name of (Contact) to define new types of objects that contain (name and phone_number).
# The __init__() method initializes each instance of Contact with specific values for name and phone_number.
# The __str__() method provides a formatted "string" representation of a Contact objects, displaying its name and phone_number.

class Contact:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

    def __str__(self):
        return  f'Name:{self.name}\n   Phone:{self.phone_number}'


# Defines a class named Manage_contact, which is designed to manage a list of contacts.
# Define a list to save the entered value by the name of "contacts"
# Define your operation like adding, removing, displaying the contact list or exit.
class Manage_contact:
    def __init__(self):
        self.contacts=[]


    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self,name):
        for contact in self.contacts:
            self.contacts.remove(contact)
            print(f'{name} has successfully removed from your contacts.')
            return
        print(f'{name} is not found in your contacts.')

    def display_contacts(self):
        if not self.contacts:
            print('No contacts to display.')
        else:
            for num_contact, contact in enumerate(self.contacts, start=1):
                print(f"{num_contact}. {contact} \n ")
# In def main(), we define that which functions to be executed, It presents a menu to the user, accepts input, and calls methods from the Manage_contact class based on user choices.
def main():
    contact_manager=Manage_contact()

    while True:
        print("\n ____Contact Manager Menu _____")
        print("1. Add a new contact")
        print("2. Remove a contact")
        print("3. Display all contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            new_contact = Contact(name, phone)
            contact_manager.add_contact(new_contact)
            print(f'{name} added to contacts.')

        elif choice == '2':
            name = input("Enter name to remove: ")
            contact_manager.remove_contact(name)

        elif choice == '3':
            print("\nThe list is in below: \n")
            contact_manager.display_contacts()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()