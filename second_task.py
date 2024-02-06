from typing import Callable
import re


def generator_numbers(text: str):
    if type(text) != str:
        return(f"Incorrect data type: {type(text)}. Give the function a string")
    
    pattern = r"(?<=\s)-?\d+\.\d+(?=\s)|(?<=\s)-?\d+(?=\s)" #шаблон знаходить всі дійсні числа
    numbers = re.findall(pattern, text) # Знаходження всіх дійсних чисел
    start = len(numbers)

    while start > 0:  #генератор
        yield float(numbers[start-1])
        start -= 1


def sum_profit(text: str, func: Callable[[str], float]):
    if type(text) != str:
        return(f"Incorrect data type: {type(text)}. Give the function a string")
    
    sum_numb = 0

    for number in func(text):  #Сумування всіх дійсних чисел
        sum_numb += number

    return sum_numb

        
if __name__=="__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")