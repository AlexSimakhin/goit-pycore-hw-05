import sys
from typing import Callable

def input_error(func: Callable) -> Callable:
  # Декоратор для обробки помилок вводу
  def inner(*args, **kwargs):
    try:
      # Виконуємо основну функцію
      return func(*args, **kwargs)
    
    except ValueError:
      # Обробка помилки, якщо недостатньо аргументів
      return "Give me both name and phone, please."
  
    except IndexError:
      # Обробка помилки, якщо недостатньо аргументів 
      # (у нинішній версії, покищо до цієї помилки дія не доходить, треба подумати мені TODO: task)
      return "Not enough arguments were provided."
    
    except KeyError:
      # Обробка помилки, якщо контакт не існує
      return f"Contact {args[0]} doesn't exist."
  
    except KeyboardInterrupt:
      # Обробка переривання користувачем
      print("\nProcess interrupted by the user. Exiting...")
      sys.exit()
  
    except Exception as e:
      # Обробка будь-яких інших неочікуваних помилок
      return f"An unexpected error occurred: {type(e).__name__}, {e}"

  return inner
