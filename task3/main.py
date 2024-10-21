import sys

def parse_log_line(line: str) -> dict:
  parts = line.split(" ", 3)
  
  # Перевірка, чи правильний формат рядка лог-файлу
  if len(parts) != 4:
    raise ValueError("Incorrect log line format.")

  date, time, level, message = parts

  return {
    "date": date,              # Дата логування
    "time": time,              # Час логування
    "level": level.upper(),    # Рівень логування (великі літери)
    "message": message.strip()  # Повідомлення (без пробілів на початку та в кінці)
  }

def load_logs(file_path: str) -> list:
  logs = []

  try:
    # Відкриваємо файл для читання
    with open(file_path, 'r') as file:
      for line in file:
        parsed_line = parse_log_line(line)  # Парсимо рядок лог-файлу
        logs.append(parsed_line)  # Додаємо розібраний рядок у список
            
  except FileNotFoundError:
    return "File not found."  # Обробка помилки, якщо файл не знайдено
  
  except Exception:
    return "Error loading log file."  # Обробка загальних помилок

  return logs  # Повертаємо список логів

def filter_logs_by_level(logs: list, level: str) -> list:
  # Фільтрація логів за рівнем
  return [log for log in logs if log['level'] == level.upper()]  

def count_logs_by_level(logs: list) -> dict:
  counts = {}  # Словник для зберігання кількостей логів за рівнем

  for log in logs:
    level = log['level']
    
    if level in counts:
      counts[level] += 1  # Збільшуємо лічильник для цього рівня
      
    else:
      counts[level] = 1  # Ініціалізуємо лічильник для нового рівня

  return counts  # Повертаємо словник з кількістю логів за рівнем

def display_log_counts(counts: dict):
  print("Log Level       | Count")
  print("-----------------|----------")
  for level, count in counts.items():
      print(f"{level:<16} | {count}")  # Виводимо рівень логування та його кількість

def main():
  if len(sys.argv) < 2:
    print("Please provide the path to the log file as a command line argument.")
    return
  
  try:
    file_path = sys.argv[1]
    logs = load_logs(file_path)  # Завантажуємо логи з файлу
    counts = count_logs_by_level(logs)  # Підраховуємо кількість логів за рівнем
    display_log_counts(counts)  # Виводимо підрахунки
    
  except Exception:
    print("File not found.")  # Повідомлення про помилку, якщо файл не знайдено
    return
  
  if len(sys.argv) > 2:
    level = sys.argv[2].upper()  # Отримуємо рівень для фільтрації
    filtered_logs = filter_logs_by_level(logs, level)  # Фільтруємо логи за рівнем

    if len(filtered_logs) == 0:
      print(f"\nNo log details found for level '{level}'")  # Якщо немає логів для цього рівня
      
    else:
      print(f"\nLog details for level '{level}':")
      
      for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")  # Виводимо деталі логів

if __name__ == "__main__":
  main()
