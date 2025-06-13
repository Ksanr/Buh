#Импортировать функции в модуль main.py
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

# При вызове функций модуля main.py выводить текущую дату.
print(f'Текущая дата: {datetime.now().date()}')

# и вызывать эти функции в конструкции.
if __name__ == '__main__':
    calculate_salary()
    get_employees()

