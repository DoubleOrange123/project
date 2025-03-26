from database_methods import database
from classes import product  
from menu import menu, secondaryMenu, ThirdMenu  

def convert(products):
    converted_data = []
    for prod in products:
        converted_data.append(product(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6]))
    return converted_data

def main():
    db = database()  
    db.open_connections()
    all_products = db.AllProd()
    all_products = convert(all_products)
    print(all_products)
    choice = -1
    while choice != 0:
        menu()  #
        choice = int(input())
        match choice: 
            case 1:
                db.add_customer()
            case 2:
                db.addProduct()
            case 3:
                secondaryMenu(all_products) 
            case 4:
                ThirdMenu(all_products, db) 
            case 5:
                db.register_customer()
            case 0:
                print('Закрыть')

if __name__ == '__main__':
    main()
