contacts = {}


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List")
    print("-" * 30)

    for name, details in contacts.items():
        print("Name :", name)
        print("Phone:", details["Phone"])
        print("-" * 30)


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("\nContact Found")
        print("Name   :", name)
        print("Phone  :", contacts[name]["Phone"])
        print("Email  :", contacts[name]["Email"])
        print("Address:", contacts[name]["Address"])
    else:
        print("Contact not found.")

    print()


def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        contacts[name]["Phone"] = input("New Phone: ")
        contacts[name]["Email"] = input("New Email: ")
        contacts[name]["Address"] = input("New Address: ")

        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")


while True:

    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.\n")