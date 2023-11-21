phonebook = {}

def add_contact(name, phone_number):
    phonebook[name] = {
        'phone_number': phone_number,
        # 'call_history': []
    }
    print(f"Added {name} to the phonebook with phone number {phone_number}")


def search_contact(name):
    if name in phonebook:
        contact = phonebook[name]
        print(f"Name: {name}, Phone Number: {contact['phone_number']}")
    else:
        print(f"{name} not found in the phonebook")


def display_contacts():
    print("Phonebook Contacts:")
    for name, contact_info in phonebook.items():
        print(f"Name: {name}, Phone Number: {contact_info['phone_number']}")


def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name} from the phonebook")
    else:
        print(f"{name} not found in the phonebook")


def add_call(name, call_details):
    if name in phonebook:
        phonebook[name]['call_history'].append(call_details)
        print(f"Added a call to the call history of {name}: {call_details}")
    else:
        print(f"{name} not found in the phonebook")


def display_call_history(name):
    if name in phonebook:
        call_history = phonebook[name]['call_history']
        print(f"Call history for {name}:")
        for i, call in enumerate(call_history, start=1):
            print(f"{i}. {call}")
    else:
        print(f"{name} not found in the phonebook")


def update_contact_phone(name, new_phone_number):
    if name in phonebook:
        phonebook[name]['phone_number'] = new_phone_number
        print(f"Updated the phone number of {name} to {new_phone_number}")
    else:
        print(f"{name} not found in the phonebook")


while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Delete Contact")
    print("5. Add Call to Contact")
    print("6. Display Call History")
    print("7. Update Contact Phone Number")
    print("8. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        add_contact(name, phone_number)
    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '5':
        name = input("Enter name to add a call to: ")
        call_details = input("Enter call details: ")
        add_call(name, call_details)
    elif choice == '6':
        name = input("Enter name to display call history: ")
        display_call_history(name)
    elif choice == '7':
        name = input("Enter name to update phone number: ")
        new_phone_number = input("Enter new phone number: ")
        update_contact_phone(name, new_phone_number)
    elif choice == '8':
        print("Exiting phonebook.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
