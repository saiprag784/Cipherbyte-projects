# contact master
# Initialize an empty list to store contacts

contacts =[]

# function to add a contact
def add_contact():
    name= input("Enter contact name:")
    number=int(input("Enter contact Phone Number:"))
    email= input("Enter conatact Email:")
    contact={
       "name":name,
       "phone":number,
       "email":email
    }
    contacts.append(contact)
    print("Contact added successfully!")


# function to view all contacts 
def view_contacts():
    print('\n Contact List:')
    if len(contacts)==0:
        print("No Contacts available.")
        return
    print("\n---Contact List---")
    for i in range(len(contacts)):
        contact=contacts[i]
        print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}") 

# function to search for a contact 
def search_contact():
    search_term = input("Enter name or phone number or email to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone'] or search_term in contact['email']]
    if not found_contacts:
        print("No matching contacts found.")
    else:
        for i in range(len(contacts)):
            contact=contacts[i]
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            
# function to delete a contact 
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name_to_delete.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
        else:
            print("Contact not found.")


def main():
    while True:
        print("\nContact Master")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



