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
print(number)

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

dct = dict{

}