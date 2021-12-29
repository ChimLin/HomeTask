import json
from re import *

def create_json_file(dct_users = {}):
    with open("users.json", "w") as file_json:
        json.dump(dct_users, file_json, indent=4)


def read_json_file():
    try:
        with open("users.json", "r") as file_json:
            return json.load(file_json)
    except FileNotFoundError:
        return []


def check_for_duplicate(lst, identificator):
    for item in lst:
        if item:
            if item["identificator"] == identificator:
                print(f"Идентификатор {identificator} существует")
                return True
    return False


def validate_criteria_password(password):
    score = 0
    rools = ["^.{8,}$", "[A-Z]{1,}|[А-ЯЁ]{1,}", "[a-z]{1,}|[а-яё]{1,}", "\d+", "[!£$%&]+"]
    for x in rools:
        if findall(x, password):
            score += 1
    return score


def change_password():
    try:
        json_file = read_json_file()
        if len(json_file) == 0:
            raise Exception("Нету пользователей для изменения пароля")
        while True:
            login = input("Введите идентификатор пользователя для смены пароля: ")
            if not check_for_duplicate(json_file, login):
                continue
            break
        password = write_password()
        for item in json_file:
            if item['identificator'] == login:
                item["password"] = password
        print(f"Пароль для идентификатора {login} был изменен успешно")
        create_json_file(dct_users=json_file)
    except Exception as message:
        print(message)


def is_weak_password(score):
    if 0 <= score <= 2:
        print("Пароль слабый. Введите боллее надежный пароль")
        return True
    elif 3 <= score <= 4:
        if input("Пароль можно улучшить! Желаете повторить процедуру? y/n ") == "y":
            return True
    else:
        print("Пароль надежный")
    return False


def write_password():
    while True:
        password = input("Введите пароль: ")
        if is_weak_password(validate_criteria_password(password)):
            continue
        break
    return password


def write_idenificator():
    json_file = read_json_file()
    while True:
        identificator = input("Введите идентификатор: ")
        if check_for_duplicate(json_file, identificator):
                continue
        break
    password = write_password()
    json_file.append({"identificator": identificator, "password":password})
    create_json_file(dct_users=json_file)


def print_logins():
    print("Список логинов:")
    for item in read_json_file():
        if item:
            print("\t", item["identificator"])
    print()


while True:
    try:
        choice = input("Введите цифру: \n\t 1 - Добавить пользователя \n\t 2 - изменить пароль \n\t 3 - Вывести список пользователей \n\t 4 - Выход \n")
        if not choice.isnumeric() or len(choice) != 1:
            raise Exception("Введеное значение не соответствует требованию")
        elif choice == "1":
            write_idenificator()
        elif choice == "2":
            change_password()
        elif choice == "3":
            print_logins()
        elif  choice == "4":
            break
    except Exception as message:
        print(message)
        print()
        continue