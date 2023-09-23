import csv
import os

def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def load_from_csv(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1]
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
    print("3: Add or update a contact in CSV")
    operate = None
    while operate is None:
        try:
            operate = int(input("Enter your choice: "))
            if operate < 1 or operate > 3:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a choice between 1 and 3.")

    if operate == 1:
        q = input("Enter the name to search for: ")
        if q in contacts:
            print(f"Name: {q}, Number: {contacts[q]}")
        else:
            print("Contact not found.")

    elif operate == 2:
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")

    elif operate == 3:
        while True:
            m = input("Enter a name (or 'cancel' to cancel): ")
            if m.lower() == 'cancel':
                break

            if m in contacts:
                choice = input("Contact already exists. Do you want to override it? (y/n): ")
                if choice.lower() == 'n':
                    continue

            while True:
                user_input = input("Enter a phone number: ")
                try:
                    s = int(user_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the phone number.")

            contacts[m] = s
            print("Contact added or updated.")

            add_more = input("Do you want to add or update more contacts? (y/n): ")
            if add_more.lower() != 'y':
                break

    c = input("Continue? (y/n): ")
    if c.lower() == "n":
        break

save_to_csv(csv_filename, [[name, number] for name, number in contacts.items()])
print("Contacts saved to CSV.")
