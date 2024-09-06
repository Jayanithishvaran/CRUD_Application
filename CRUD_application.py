import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

def add_contact(name, phone, email):
    cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    if contacts:
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
    else:
        print("No contacts found.")

def update_contact(contact_id, name=None, phone=None, email=None):
    if name:
        cursor.execute('UPDATE contacts SET name = ? WHERE id = ?', (name, contact_id))
    if phone:
        cursor.execute('UPDATE contacts SET phone = ? WHERE id = ?', (phone, contact_id))
    if email:
        cursor.execute('UPDATE contacts SET email = ? WHERE id = ?', (email, contact_id))
    conn.commit()
    print(f"Contact with ID {contact_id} updated successfully!")

def delete_contact(contact_id):
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    print(f"Contact with ID {contact_id} deleted successfully!")

def main():
    while True:
        print("\nContact Management Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            contact_id = int(input("Enter Contact ID to update: "))
            print("Leave fields blank if you don't want to update them.")
            name = input("Enter New Name (or press Enter to skip): ")
            phone = input("Enter New Phone (or press Enter to skip): ")
            email = input("Enter New Email (or press Enter to skip): ")
            update_contact(contact_id, name if name else None, phone if phone else None, email if email else None)
        elif choice == '4':
            contact_id = int(input("Enter Contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

conn.close()
