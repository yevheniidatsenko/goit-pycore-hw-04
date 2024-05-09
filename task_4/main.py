def parse_input(user_input):
    """
    Parse user input into command and arguments.
    
    Args:
        user_input (str): User input string.
    
    Returns:
        tuple: Command and arguments as a tuple.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    
    Args:
        args (list): List of arguments (name and phone number).
        contacts (dict): Contacts dictionary.
    
    Returns:
        str: Success message.
    """
    if len(args)!= 2:
        return "Invalid arguments. Please provide name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Update an existing contact in the contacts dictionary.
    
    Args:
        args (list): List of arguments (name and new phone number).
        contacts (dict): Contacts dictionary.
    
    Returns:
        str: Success message or error message if contact not found.
    """
    if len(args)!= 2:
        return "Invalid arguments. Please provide name and new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args, contacts):
    """
    Show the phone number of a contact.
    
    Args:
        args (list): List of arguments (name).
        contacts (dict): Contacts dictionary.
    
    Returns:
        str: Phone number or error message if contact not found.
    """
    if len(args)!= 1:
        return "Invalid arguments. Please provide name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all(contacts):
    """
    Show all contacts.
    
    Args:
        contacts (dict): Contacts dictionary.
    
    Returns:
        str: All contacts as a string.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    """
    Main function to handle user input and commands.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()