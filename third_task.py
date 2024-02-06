import sys
from pathlib import Path
from collections import namedtuple
import collections
from tabulate import tabulate


def load_logs(file_path: str) -> list:
    file_path = Path(file_path)
    if file_path.exists() and file_path.suffix == ".log": #якщо файл не існує або не лог, программа завершиться
        with open(file_path, "r", encoding="utf-8") as log_file:
            return [parse_log_line(log_line.strip()) for log_line in log_file.readlines()] #повертає список зі словників. до кожної строки застосовується функція parse_log_line
    else:
        print("The file does not exist or is not a file log")
        sys.exit()
        
                


def parse_log_line(line: str) -> dict:
    log_templates = namedtuple("log_dic", "date time level message") # шаблон для іменованого кортежу
    try:
        log = line.split(" ")[0:3]
        log.append(" ".join(line.split(" ")[3:])) #Розділяє строку на складові
        log_dic =dict(log_templates._make(log)._asdict()) #робить іменований кортеж зі списку та перетворює на словник
        return log_dic
    except Exception:
        print("Damage file")
        sys.exit()


def filter_logs_by_level(logs: list, level: str) -> list:
    return(filter(lambda log:level == log["level"], logs))

    

def count_logs_by_level(logs: list) -> dict:
    return (dict(collections.Counter([log["level"] for log in logs]))) 


def display_log_counts(counts: dict): #створює таблицю за допомогою tabulate
    headers = ["Рівень логування", "Кількість"]
    table_data = [[level, count] for level, count in counts.items()]
    tab = tabulate(table_data, headers, tablefmt="pipe")
    print(tab)

    

def main():
    arguments = sys.argv
    if len(arguments) < 2 or len(arguments) > 3:
        print("Usage: python third_task.py <directory path> level(optional argument)")
    else:
        path_to_the_log = arguments[1]
        logs = load_logs(path_to_the_log)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if len(arguments) == 3: # якщо level введений і коректно, виводить додаткову інформацію
            level = arguments[2].upper()
            if level not in ["DEBUG", "ERROR", "INFO", "WARNING"]:
                print(f"{level} - incorrect name of the log level")
            else:
                print(f"Деталі логів для рівня '{level}':")
                for log_by_level in filter_logs_by_level(logs, level):
                    print(log_by_level["date"] + " " + log_by_level["time"] + " - " + log_by_level["message"])



if __name__ == "__main__":
    main()
