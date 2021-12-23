import random

# Задание 1 ---------------------------------

def check_for_duplicates(number):
    """"Проверка на дубликаты"""
    new_number = get_digits(number)
    if len(new_number) == len(set(new_number)):
        return True
    else:
        return False


def generat_numbers():
    """"Создание рандомного числа от 1000 до 9999"""
    while True:
        num = random.randint(1000, 9999)
        if check_for_duplicates(num):
            return num


def get_digits(number):
    return [int(i) for i in str(number)]

def cows_or_bulls(number, guess):
    """"Сравнивает сгенерированные числа с введенными"""
    bull_cow = [0, 0]
    num_list = get_digits(number)
    guess_list = get_digits(guess)

    for i, j in zip(num_list, guess_list):
        if j in num_list:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

number = generat_numbers()

while True:
    guess = input("Введите 4-х значное число от 1000 до 9999 для игры. Для остановки игры введите -1 или STOP: ")

    if guess == '-1' or guess == 'STOP':
        print("Игра завершина")
        break

    guess = int(guess)

    if not check_for_duplicates(guess):
        print("Цифры повторяются в введенном числе. Введите новочое число")
        continue
    if guess < 1000 or guess > 9999:
        print("Введеное число не в диапозоне от 1000 до 9999. Введите новочое 4-х значное число")
        continue

    bull_cow = cows_or_bulls(number, guess)
    print(f"{bull_cow[0]} Быка, {bull_cow[1]} Коровы")

    if bull_cow[0] == 4:
        print("Поздравляю! Число угадано!!! Игра завершина")
        break


# Задание 2
print()
print()

dct = {
    1:{
        "q1": "Почему подоражали машины?",
        "а1": "Диллеры зазнались",
        "a2": "Почему подоражали машины",
        "а3": "Диллеры зазнались",
        "a4": "Почему подоражали машины",
        "Ответ": "a1"
    },
    2:{
            "q1": "Что написано на заборе?",
            "а1": "Цой жив",
            "a2": "Горький не забыт",
            "а3": "Не брат ты мне",
            "a4": "Ничего",
            "Ответ": "a1"
        },
    3:{
            "q1": "В какой стране часто бывает землятресение?",
            "а1": "Япония",
            "a2": "Америка",
            "а3": "Россия",
            "a4": "Индия",
            "Ответ": "a1"
        },
    4:{
            "q1": "В каком году Брежнев поцеловал человека",
            "а1": "1963",
            "a2": "1979",
            "а3": "1967",
            "a4": "1983",
            "Ответ": "a2"
        }
}


def play_game(dictionary):
    """Выводит вопросы и ответы на экран"""
    false_answer = 0
    for values in dictionary.values():
        if false_answer > 0:
            break
        for key, value in values.items():
            if key == "Ответ":
                answer = input("Введите ваш ответ 'a1, a2, a3  или a4': ")
                if answer == value:
                    print("Верно")
                    print("----------------------")
                    continue
                else:
                    print("Простите, но вы проиграли")
                    false_answer += 1
                    break
            print(key, ":", value)


play_game((dct))