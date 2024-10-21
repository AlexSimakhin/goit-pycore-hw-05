from contacts_operations import add_contact, change_contact, get_contact, get_all_contacts, remove_contact

COMMAND_CLOSE = {"close", "exit", "leave"}
COMMAND_HELLO = {"hello"}
COMMAND_ALL = {"all"}
COMMAND_ADD = {"add"}
COMMAND_CHANGE = {"change"}
COMMAND_PHONE = {"phone"}
COMMAND_REMOVE = {"remove", "delete"}


def parse_input(user_input: str) -> tuple:
  try:
    # Розділення вводу користувача на команду та аргументи
    cmd, *args = user_input.strip().lower().split(maxsplit=1)
    return cmd, args[0].split() if args else []
  except ValueError:
    return "", []


def handle_command(command: str, args: list, contacts: dict) -> None:
  # Обробка команд на основі введеної команди
  match command:
    case cmd if cmd in COMMAND_CLOSE:
      print("Goodbye!")
    case cmd if cmd in COMMAND_HELLO:
      print("How can I help you?")
    case cmd if cmd in COMMAND_ALL:
      print(get_all_contacts(contacts))
    case cmd if cmd in COMMAND_ADD:
      print(add_contact(args, contacts))
    case cmd if cmd in COMMAND_CHANGE:
      print(change_contact(args, contacts))
    case cmd if cmd in COMMAND_PHONE:
      print(get_contact(args, contacts))
    case cmd if cmd in COMMAND_REMOVE:
      print(remove_contact(args, contacts))
    case _:
      print("Invalid command.")

def main():
  contacts = {} # Словник для зберігання контактів
  print("Welcome to the assistant bot!")
  
  while True:
    user_input = input("Enter a command: ")
    command, args = parse_input(user_input)
    handle_command(command, args, contacts)
    
    if command in COMMAND_CLOSE:
      break


if __name__ == "__main__":
  main()