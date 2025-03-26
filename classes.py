import datetime

class product:
    def __init__(self, id:int, price:int, name:str, isNew:bool, count:int, idCategory:int, idCustomer:int):
        self.id = id
        self.price = int(price)
        self.name = name
        self.isNew = isNew
        self.count = count
        self.idCategory = idCategory
        self.idCustomer = idCustomer

    def __str__(self):
        return f'ID: {self.id}, Price: {self.price}, Name: {self.name}, New: {self.isNew}, Count: {self.count}, Category ID: {self.idCategory}, Customer ID: {self.idCustomer}'
    
class order:
    def __init__(self, id_orders:int = 1, login:str = "a", order_date:datetime = datetime.date(2014, 2, 25), amount:int = 1, prod_id:int = 1):
        self.id_orders = id_orders
        self.login = login
        self.order_date = order_date
        self.amount = amount
        self.prod_id = prod_id


    def __str__(self):
        return f'id_orders: {self.id_orders}, login: {self.login}, order_date: {self.order_date}, amount: {self.amount}, prod_id: {self.prod_id}'