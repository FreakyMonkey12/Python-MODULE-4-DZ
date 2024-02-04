def parse_input(input_string):
    parts = input_string.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(contacts, username, phone):
    contacts[username] = phone
    return f"Contact {username} with phone number {phone} added successfully."

def change_contact(contacts, username, phone):
    if username in contacts:
        contacts[username] = phone
        return f"Phone number for contact {username} changed to {phone}."
    else:
        return f"Contact {username} not found."

def show_phone(contacts, username):
    if username in contacts:
        return f"The phone number for {username} is {contacts[username]}."
    else:
        return f"Contact {username} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        all_contacts = "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
        return all_contacts

def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command == "exit" or command == "close":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                username, phone = args
                print(add_contact(contacts, username, phone))
            else:
                print("Invalid command format. Usage: add username phone")
        elif command == "change":
            if len(args) == 2:
                username, phone = args
                print(change_contact(contacts, username, phone))
            else:
                print("Invalid command format. Usage: change username phone")
        elif command == "phone":
            if len(args) == 1:
                username = args[0]
                print(show_phone(contacts, username))
            else:
                print("Invalid command format. Usage: phone username")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
