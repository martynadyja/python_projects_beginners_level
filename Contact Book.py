#Contact Book

print("Contact Book")

contactbook = []

addcontact_responses = ["add a new contact", "add contact", "contact add", "new contact", "add new contact"]
readcontact_responses = ["read contacts", "read contact", "view contacts", "view contact", "see contacts", "see contact", "view my contacts"]
remove_and_change_contact_responses = ["remove contacts", "remove contact", "remove my contacts", "remove my contact", "change contacts",
                                       "change contact", "change my contacts", "change my contact"]
quitapp_responses = ["close app", "close", "quit app", "quit", "stop running", "stop"]

def changescene_small():
    for i in range(1, 2):
        print("\n")

def main():
    changescene_small()
    action = input("Do you want to see contacts, add a new contact, change contact or remove contact? If you want to leave, reply 'quit'. ")
    action = str(action)

    if action in addcontact_responses:
        changescene_small()
        print("If you don't want to enter a value, you can just press enter.")

        name = input("Enter a name: ")
        name = str(name)
        phone = input("Enter a phone:  ")
        phone = str(phone)

        entry = (name +" "+ phone)
        entry = str(entry)

        contactbook.append(entry)
        print("Contact added: " + entry)

    elif action in remove_and_change_contact_responses:
        changescene_small()

        name = input("Enter a name: ")
        name = str(name)
        phone = input("Enter a phone: ")
        phone = str(phone)

        entry = (name +" "+ phone)
        entry = str(entry)

        contactbook.remove(entry)
        print("Contact removed: " + entry)

        new_name = input("Enter a new name: ")
        new_name = str(new_name)

        new_phone = input("Enter a new phone: ")
        new_phone = str(new_phone)

        entry2 = (new_name +" "+ new_phone)
        entry2 = str(entry2)

        contactbook.append(entry2)
        print("Contact changed: " + entry2)

    elif action in readcontact_responses:
        contacts = contactbook
        contacts = str(contacts)
        print(contacts)

    elif action in quitapp_responses:
        print(action)

    else:
         print("Response not recognized. Please phrase your response differently.")

running = True
while running:
    main()
