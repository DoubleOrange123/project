import mysql.connector
import datetime

class database:
      def __init__(self):
            self.__db = None
            self.__cursor = None

      def open_connections(self):
            self.__db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='warhammer308308', 
            database='electronics_store',auth_plugin='mysql_native_password')
          
      def select_all_clients(self)-> list[str]:
            query = 'SELECT * FROM client'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            clients = self.__cursor.fetchall()
            self.__cursor.close()
            return clients

      def insert_data_client_by_id(self, values2: list[str]):
            query2 = f'INSERT INTO client (login, firstname, lastname, phone) \
            VALUES(\"{values2[0]}\", \"{values2[1]}\", \"{values2[2]}\", \"{values2[3]}\")'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query2)
            self.__db.commit()
            
      def select_all_products(self)-> list[str]:
            query = 'SELECT * FROM product'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            product = self.__cursor.fetchall()
            self.__cursor.close()
            return product    
      
      def select_all_products_category(self)-> list[str]:
            query = 'SELECT idCategory FROM product'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            product = self.__cursor.fetchall()
            self.__cursor.close()
            return product
      def select_all_products_price(self)-> list[str]:
            query = 'SELECT price FROM product'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            product = self.__cursor.fetchall()
            self.__cursor.close()
            return product
      
      def select_all_products_name(self)-> list[str]:
            query = 'SELECT name FROM product'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            product = self.__cursor.fetchall()
            self.__cursor.close()
            return product      
      
      def change_data_product_by_id(self, id: int, values: list[str]):
            query2 = f'UPDATE product \
            SET price = {values[0]}, name = \"{values[1]}\", count = {values[2]} \
            WHERE id = {id}'  
            print(values)
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query2)
            self.__db.commit()

      def change_data_product_by_id_v2(self, id: int, count: int):
            query2 = f'UPDATE product \
            SET count = {count} \
            WHERE id = {id}'  
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query2)
            self.__db.commit()

      def new_order(self, id: int, count: int, login: str):
            query2 = f'INSERT INTO orders (order_date, login, amount, prod_id) \
            VALUES(\"{datetime.date.today()}\", \"{login}\", {count}, {id})'
            print(query2)
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query2)
            self.__db.commit()

      def insert_data_product_by_id(self, values2: list[str]):
            query2 = f'INSERT INTO product (price, name, count) \
            VALUES({values2[0]}, \"{values2[1]}\", {values2[2]})'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query2)
            self.__db.commit()

      def insert_data_product_by_id(self, values2: list[str]):
            query2 = f'INSERT INTO product (price, name, count) \
            VALUES({values2[0]}, \"{values2[1]}\", {values2[2]})'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query2)
            self.__db.commit()      

      def check_if_user_in(self, login: str):
            query = f'SELECT login from client \
            WHERE login = \"{login}\"'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            login = self.__cursor.fetchone()
            self.__cursor.close()
            if login != None:
                  return True
            return False

      def select_all_products_price(self)-> list[str]:
            query = 'SELECT amount FROM orders'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            amount = self.__cursor.fetchall()
            self.__cursor.close()
            return amount
      
      def select_all_orders(self)-> list[str]:
            query = 'SELECT order_date, amount FROM orders'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            data = self.__cursor.fetchall()
            self.__cursor.close()
            return data
      
      def add_customer(self):
            print("Введите данные для регистрации:")
            login = input("Логин: ")
            firstname = input("Имя: ")
            lastname = input("Фамилия: ")
            phone = input("Телефон: ")
            self.insert_data_client_by_id([login, firstname, lastname, phone])

      def addProduct(self):
            price = int(input())
            name = input()
            count = int(input())
            self.insert_data_product_by_id([price, name, count])

      def AllProd(self):
            return self.select_all_products()
      
      def register_customer(self):
            print("Введите данные для регистрации:")
            login = input("Логин: ")
            firstname = input("Имя: ")
            lastname = input("Фамилия: ")
            phone = input("Телефон: ")
            customer_id = self.insert_data_client_by_id([login, firstname, lastname, phone])
            return customer_id
      
      def select_all_prodID(self)-> list[str]:
            query = 'SELECT prod_id, amount FROM orders'
            self.__cursor = self.__db.cursor()
            self.__cursor.execute(query)
            data = self.__cursor.fetchall()
            self.__cursor.close()
            return data
      
      def All_Orders(self):
            return self.select_all_orders()
