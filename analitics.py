from database_methods import database
from classes import order
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates



def convert(orders):
    converted_data = []
    for ord in orders:
        converted_data.append(order(order_date = ord[0], amount = ord[1]))
    for obj in converted_data:
        print(f"Order Date: {obj.order_date}, Amount: {obj.amount}")
    print(converted_data)
    return converted_data

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from collections import defaultdict

def graph(orders):
    # Проверяем, что данные не пустые
    if not orders:
        print("Нет данных для построения графика.")
        return

    # Словарь для агрегации сумм по датам
    date_amount = defaultdict(float)

    for ord in orders:
        # Убедимся, что в кортеже достаточно элементов
        if len(ord) < 2:
            print(f"Недостаточно данных в записи: {ord}")
            continue
            
        date = ord[0]  # Получаем дату
        amount = ord[1]  # Получаем сумму
        date_amount[date] += amount  # Аггрегируем суммы по датам

    # Подготовка данных для графика
    date_list = sorted(date_amount.keys())  # Сортируем даты
    amount_list = [date_amount[date] for date in date_list]  # Получаем суммы для отсортированных дат

    # Строим график
    plt.figure(figsize=(10, 5))
    plt.plot(date_list, amount_list, marker='o')
    plt.title("График сумм заказов за каждую дату")
    plt.xlabel("Дата заказа")
    plt.ylabel("Сумма заказа")
    plt.xticks(rotation=45)  # Поворачиваем метки по оси X для удобства чтения
    plt.grid(True)  # Добавляем сетку для лучшей читаемости графика
    plt.tight_layout()  # Настраиваем компоновку для лучшего отображения графика
    plt.show()  # Показываем график
    
def convert_prodID(orders):
    converted_data = []
    for ord in orders:
        converted_data.append(order(prod_id = ord[0], amount = ord[1]))
    for obj in converted_data:
        print(f"Prod ID: {obj.prod_id}, Amount: {obj.amount}")
    return converted_data





def best_selling_prod(obj_list: list[order]):
    total_amount_per_id = {}
    for obj in obj_list:
        prod_id = obj.prod_id
        amount = obj.amount
        if prod_id in total_amount_per_id:
            total_amount_per_id[prod_id] += amount  
        else:
            total_amount_per_id[prod_id] = amount  
    
    max_amount = max(total_amount_per_id.values())
    
    best_selling_id = max(total_amount_per_id, key=total_amount_per_id.get)
    
    print(best_selling_id, max_amount)


def pandas_order(obj_list: list[order]):
    total_amount_per_date = {}  # Словарь для подсчета общего количества товаров по дате
    for obj in obj_list:
        order_date = obj.order_date
        amount = obj.amount
        if order_date in total_amount_per_date:
            total_amount_per_date[order_date] += amount  
        else:
            total_amount_per_date[order_date] = amount  

    # Находим максимальное количество купленных товаров
    max_amount = max(total_amount_per_date.values())
    
    # Находим все даты, у которых количество купленных товаров соответствует максимальному
    busiest_dates = [date for date, total in total_amount_per_date.items() if total == max_amount]

    for date in busiest_dates:
        print(f"{correct_date_format(date)}, {max_amount}") 


def correct_date_format(date:datetime):
    a = ""
    if date.day < 10:
        a += f'0{date.day}'
    else:
        a += str(date.day)
    a += "."
    if date.month < 10:
        a += f'0{date.month}'
    else:
        a += str(date.month)
    return (a)


def main():
    db = database()
    db.open_connections()
    data = db.select_all_orders()
    data2 = db.select_all_prodID()
    objects = convert(data)
    prods = convert_prodID(data2)
    graph(data)
    pandas_order(objects)
    best_selling_prod(prods)
main()

#изменения