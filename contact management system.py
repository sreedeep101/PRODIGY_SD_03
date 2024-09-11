class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added!")

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def edit_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            print(f"Contact {name} updated!")
        else:
            print("Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted!")
        else:
            print("Contact not found!")

def main():
    contact_manager = ContactManager()
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            name = input("Enter name: ")
            phone = input("Enter new phone number (leave blank if no change): ")
            email = input("Enter new email address (leave blank if no change): ")
            contact_manager.edit_contact(name, phone or None, email or None)
        elif choice == "4":
            name = input("Enter name: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
              
