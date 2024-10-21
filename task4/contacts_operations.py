from wrapper import input_error

@input_error
def add_contact(contact_data: list, contacts: dict) -> str:
  name, phone = contact_data
  
  # Додавання нового контакту у словник
  contacts[name] = phone
  return "Contact added."


@input_error
def change_contact(contact_data: list, contacts: dict) -> str:
  name, phone = contact_data

  # Оновлення контактної інформації
  contacts[name] = phone
  return "Contact updated."


@input_error
def get_contact(contact_data: list, contacts: dict) -> str:
  name = contact_data[0]
  
  # Повернення телефонного номера
  return contacts[name]


@input_error
def get_all_contacts(contacts: dict) -> str:
  # Перевірка, чи є контакти в словнику
  if not contacts:
    return "Contacts are empty."
  
  # Формування списку контактів для виведення
  output = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
  return output
  

@input_error
def remove_contact(contact_data: list, contacts: dict) -> str:
  name = contact_data[0]
  
  # Видалення контакту
  del contacts[name]
  return "Contact removed."