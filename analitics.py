from database_methods import database
from classes import order
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def convert(orders):
    converted_data = []
    for ord in orders:
        converted_data.append(order(order_date = ord[0], amount = ord[1]))
    for obj in converted_data:
        print(f"Order Date: {obj.order_date}, Amount: {obj.amount}")
    print(converted_data)
    return converted_data

def graph(orders):
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

def graph2(orders):
    date_amount = defaultdict(float)
    for ord in orders:        
        date = ord[0]  
        amount = ord[1]  
        date_amount[date] += amount
    ser = pd.Series(date_amount)
    plt.figure(figsize=(8, 6))
    plt.pie(ser.values, labels=ser.index)
    plt.title('Распределение сумм по датам')
    plt.show()

def graph3(orders):
    product_data = defaultdict(float)
    for ord in orders:        
        prod_id = ord[0]  
        amount = ord[1]
        product_data[prod_id] += amount  
    
    ser = pd.Series(product_data)
    
    plt.figure(figsize=(12, 6))
    
    plt.bar(x=ser.index.astype(str),height=ser.values)
    plt.title('Суммы по продуктам')
    plt.xlabel('ID продукта')
    plt.ylabel('Сумма')
    plt.show()

'''def graph4(orders):
    date_product_amount = defaultdict(float)
    id_product_amount = defaultdict(float)
    for ord in orders: 
        date = ord[0]       
        prod_id = ord[2]  
        amount = ord[1]
        date_product_amount[date] += amount
        id_product_amount[prod_id] += amount
    
    ser = pd.Series(date_product_amount)
    ser2 = pd.Series(id_product_amount)

    plt.title("Прибыль магазинов")
    plt.bar(x=ser.index, height=ser.values, label=ser2.index)

    # размер текста на графике
    plt.legend(title='Магазины')

    plt.show()'''

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
    data3 = db.select_all_orders_and_id()
    objects = convert(data)
    prods = convert_prodID(data2)
    graph(data)
    graph2(data)
    graph3(data2)
    graph4(data3)
    pandas_order(objects)
    best_selling_prod(prods)
main()

#изменения