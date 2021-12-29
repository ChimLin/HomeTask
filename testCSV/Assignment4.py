import csv

columns = ["Name", "Price", "Description"]
comands = ["LIST", "ADD", "DELETE", "SEARCH", "BREAK"]

def create_and_add_elements_in_csv(dictionary = {}):
    """"Создания файла с расширением csv и запись в него данных из dictionary"""
    try:
        with open("items.csv", "w") as file:
            writer = csv.DictWriter(file, columns)
            writer.writeheader()
            for key in dictionary.values():
                writer.writerow(key)
    except IOError as message:
        print(message)

# dictionary of goods
goods = { 1: {"Name": "Butter",
              "Price": 80,
              "Description": "yellow-to-white solid emulsion of fat globules"
              },
        2: {"Name": "Bread",
                      "Price": 40,
                      "Description": "White loaf baked with heat"
                      },
        3: {"Name": "Milk",
                      "Price": 72,
                      "Description": "Milky item for drinking"
                      },
        4: {"Name": "Cheese",
                      "Price": 280,
                      "Description": "Solid and yellow piece with holes"
                      },
        5: {"Name": "Salami",
                      "Price": 749,
                      "Description": "Made with meet and other chemical elements"
                      }}

def sub_list_all_goods(reader):
    """Выводит весь перечень товаров из csv файла в командную строку"""
    one_time = 0
    for row in reader:
        if one_time == 0:
            print(f"{'          '.join(row)}")
            print("____________________________________")
            one_time += 1
        print(f"{row['Name']}\t\t  {row['Price']}\t       {row['Description']} ")


def sub_return_list_items(reader):
    """"Возвращает список списков товаров для поиска дубликата"""
    lst_for_compare = []
    for row in reader:
        lst_for_compare.append([row['Name'], row['Price'], row['Description']] )
    return lst_for_compare


def list_all_goods(flow = 0):
    """Ссыллатся на функции sub_list_all_goods, sub_return_list_items"""
    try:
        with open("items.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            if flow == 0:
                sub_list_all_goods(csv_reader)
            else:
                return sub_return_list_items(csv_reader)
    except IOError as message:
        print(message)


def add_new_good():
    """"Добавление товара в фаил csv"""
    while True:
        name = input("Введите название товара: ")
        price = input("Введите цену товара: ")
        description = input("Опишите товар: ")
        lst = list_all_goods(1)
        with open("items.csv", "a") as file:
            writer = csv.writer(file)
            if [name, price, description] in lst:
                print("Данный товар существует. Повторите процедуру")
                continue
            writer.writerow([name, price, description])
            print("Товар добавлен")
            break


def delete_item():
    """Удаление строки из файла по названию товара"""
    del_item = input("Введите название товара для удаления из списка: ")
    dct = {}
    key = 1
    with open("items.csv", "r") as old:
        for row in csv.DictReader(old):
            if row["Name"] != del_item:
                dct[key] = dict(row)
                key += 1
    create_and_add_elements_in_csv(dct)


def search_description():
    search = input("Введите название товара для отображения его описания: ")
    lst = list_all_goods(1)
    for row in lst:
        if row[0] == search:
            print(f"Описание товара {search} : {row[2]}")
            break

create_and_add_elements_in_csv(goods)

while True:
    try:
        user_choice = input("Введите 1 из 4-x команд:\n\tLIST - отобразить список всех товаров\n\tADD - ввести информацию о товаре и добавить его\n\tDELETE - удалить существующий товар по имени\n\tSEARCH - получить описание товара по его имени \n\tBREAK - остановить программу\n")
        if user_choice not in comands:
            raise ValueError(f"Нету такой команды как {user_choice}")
        elif user_choice == 'LIST':
            list_all_goods()
            print(" --------------------------------")
        elif user_choice == 'ADD':
            add_new_good()
            print(" --------------------------------")
        elif user_choice == 'DELETE':
            delete_item()
            print(" --------------------------------")
        elif user_choice == "SEARCH":
            search_description()
            print(" --------------------------------")
        else:
            print("Завершение программы")
            break
    except ValueError as message:
        print(message, "\n --------------------------------")
        continue

