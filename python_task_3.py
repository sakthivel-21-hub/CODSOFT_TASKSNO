def display_menu():
    print("\n=========================================")
    print("             CONTACT BOOK                ")
    print("=========================================")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=========================================")

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print(f"✅ Success! {name} has been added to your contacts.")

def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("Your contact book is empty.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter Name or Phone Number to search: ").strip().lower()
    
    found_contacts = []
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            found_contacts.append(contact)
            
    if found_contacts:
        print("\n🔍 Search Results:")
        for c in found_contacts:
            print(f"Name: {c['name']} | Phone: {c['phone']} | Email: {c['email']} | Address: {c['address']}")
    else:
        print("❌ No matching contacts found.")

def update_contact(contacts):
    print("\n--- Update Contact ---")
    query = input("Enter the Name of the contact you want to update: ").strip().lower()
    
    for contact in contacts:
        if contact['name'].lower() == query:
            print(f"Found contact: {contact['name']}")
            contact['name'] = input(f"Enter new Name (leave blank to keep '{contact['name']}'): ").strip() or contact['name']
            contact['phone'] = input(f"Enter new Phone (leave blank to keep '{contact['phone']}'): ").strip() or contact['phone']
            contact['email'] = input(f"Enter new Email (leave blank to keep '{contact['email']}'): ").strip() or contact['email']
            contact['address'] = input(f"Enter new Address (leave blank to keep '{contact['address']}'): ").strip() or contact['address']
            print("✅ Contact updated successfully!")
            return
            
    print("❌ Contact not found.")

def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    query = input("Enter the Name of the contact you want to delete: ").strip().lower()
    
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == query:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ").lower()
            if confirm == 'y':
                del contacts[i]
                print("✅ Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
            
    print("❌ Contact not found.")

def main():
    # A list to store all contact dictionaries
    contacts = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nExiting Contact Book. Have a great day! 👋")
            break
        else:
            print("❌ Invalid input! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()