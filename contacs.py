import csv
import os

def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def load_from_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def clear_csv(filename):
    with open(filename, 'w', newline='') as file:
        pass

csv_filename = "contacts.csv"

if not os.path.isfile(csv_filename):
    with open(csv_filename, 'w', newline='') as file:
        pass

contacts = load_from_csv(csv_filename)

while True:
    print("What operation would you like to perform?")
    print("1: Search for a contact")
    print("2: Display all contacts")
    print("3: Add a new contact to CSV")
    print("4: Remove a contact from CSV")
    operate = None
    while operate is None:
        try:
            operate = int(input("Enter your choice: "))
            if operate < 1 or operate > 4:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a choice between 1 and 4.")

    if operate == 1:
        q = input("Enter the name to search for: ")
        found = False
        for contact in contacts:
            if q in contact[0]:
                print(f"Name: {contact[0]}, Number: {contact[1]}")
                found = True
        if not found:
            print("Contact not found.")

    elif operate == 2:
        for contact in contacts:
            print(f"Name: {contact[0]}, Number: {contact[1]}")

    elif operate == 3:
        while True:
            m = input("Enter a name (or 'cancel' to cancel): ")
            if m.lower() == 'cancel':
                break
            while True:
                user_input = input("Enter a phone number: ")
                try:
                    s = int(user_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the phone number.")
            contacts.append([m, s])
            print("New contact added.")

            add_more = input("Do you want to add more contacts? (y/n): ")
            if add_more.lower() != 'y':
                break

    elif operate == 4:
        if len(contacts) == 0:
            print("No contacts to remove.")
        else:
            name = input("Enter the name of the contact you want to remove: ")
            removed = False
            for contact in contacts:
                if name in contact[0]:
                    contacts.remove(contact)
                    print("Contact removed.")
                    removed = True
                    break
            if not removed:
                print("Contact not found.")

    c = input("Continue? (y/n): ")
    if c.lower() == "n":
        break

save_to_csv(csv_filename, contacts)
print("Contacts saved to CSV.")
