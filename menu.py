from database_methods import database
from classes import product


def secondaryMenuView():
    print('1. вывод всех продуктов')
    print('2. вывод по категории')
    print('3. вывод по цене')
    print('4. вывод по названию')
    print('0. Назад')

def ThirdMenuView():
    print("Выберите продукт") 

def viewAllProducts(all_products):
    for product in all_products:
        print(product)

def viewAllProductsByCategory(all_products):
    try:
        category_id = int(input("Введите ID категории для отображения продуктов: "))
        filtered_products = [product for product in all_products if product.idCategory == category_id]

        if filtered_products:
            print(f"Продукты в категории с ID {category_id}:")
            for product in filtered_products:
                print(product)
        else:
            print(f"В категории с ID {category_id} нет продуктов.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID категории.")

def secondaryMenu(all_products):
    choise = -1
    while choise != 0:
        secondaryMenuView()
        choise = int(input())
        match choise: 
            case 1:
                viewAllProducts(all_products)
            case 2:
                viewAllProductsByCategory(all_products)
            case 3:
                viewAllProducts_price(all_products)
            case 4:
                viewAllProducts_name(all_products)
            case 0:
                print('Возврат в главное меню.')

def menu():
    print('1. добавить покупателя')
    print('2. добавить продукт')
    print('3. далее')
    print('4. купить')
    print('5. регистрация (для покупки необходимо пройти регистрацию)')
    print('0. Закрыть')

def ThirdMenu(all_products: list[product], db: database):
        viewAllProducts(all_products)
        prodAvaible(all_products, db)

def prodAvaible(all_products:list[product], db: database):
    db.open_connections()
    login = input("Логин: ")
    if db.check_if_user_in(login):
        try:
            choice = int(input("Выберите номер продукта для покупки (или 0, чтобы выйти): "))
            if choice == 0:
                print("Выход из выбора продукта.")
                return
            elif 1 <= choice <= len(all_products):
                selected_product = all_products[choice - 1]
                print(f"Вы выбрали продукт: {selected_product}. Он доступен в количестве: {selected_product.count}")

                # Ввод количества для покупки
                quantity = int(input(f"Введите количество {selected_product.name} для покупки: "))
                if quantity > selected_product.count:
                    print(f"Недостаточно {selected_product.name} на складе. Доступное количество: {selected_product.count}.")
                else:
                    print(f"Вы успешно купили {quantity} {selected_product.name}.")
                    # Корректируем оставшийся продукт на складе
                    db.change_data_product_by_id_v2(selected_product.id, selected_product.count - quantity)
                    all_products[selected_product.id].count =  selected_product.count - quantity
                    # Создаем новый заказ
                    db.new_order(selected_product.id, quantity, login)
                    print(f"Количество {selected_product.name} обновлено")
                    print(f"Добавлен новый заказ")
            else:
                print("Неверный номер продукта")
        except ValueError:
            print("введите корректный номер или количество")
    else: print("YOU SHALL NOT PASS")

def viewAllProducts_price(all_products:list[product]):
    sorted_prod = sorted(all_products, key = lambda x: x.price, reverse = True)
    viewAllProducts(sorted_prod)


def viewAllProducts_name(all_products:list[product]):
    sorted_name = sorted(all_products, key = lambda x: x.name, reverse = False)
    viewAllProducts(sorted_name)



