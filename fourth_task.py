from functools import wraps

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "contact does not exist."
        except IndexError:
            return "Give me name please."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return (cmd, *args)

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "That name already exists."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]} "
    # if name in contacts:
    #     return f"{name}: {contacts[name]} "
    # else:
    #     return("contact does not exist")
    
@input_error
def show_all(contacts):
    all = []
    for contact in contacts:
        all.append(contact + ":\t" + contacts[contact])
    return (all)
    

def main():
    contacts = {"Jass": "+383729384", "Kate": "+3489792835792"}
    #contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print("Enter a command: \n hello \n add name phone \n change name phone \n phone name \n all \n exit, close")
        elif command == "all":
            if not contacts:
                print ("contact list is empty.")
            for contact in show_all(contacts):
                print(contact)
        #elif len(args) == 1 and command == "phone":
        elif command == "phone":
            print(show_phone(args, contacts)) 
        #elif len(args) == 2:      
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts)) 
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
