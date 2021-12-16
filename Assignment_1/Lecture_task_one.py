from random import randint
# First task solution
print("------------------------------------------------------------")
print("Решение первого задания: ")
i = 100
sum = 0
while i < 200:
    if i % 3 == 0:
        print("целое число", i, "кратно 3", sep=" ")
        sum += i
    i += 1
print("Сумма всех целых чисел от 100 до 200 кратные 3 равна", sum, sep=" ")

# Second task solutionprint
print("------------------------------------------------------------")
print("Решение второго задания: ")
num = 2
while(num <= 100):
    count = 0
    i = 2
    while(i <= num//2):
        if(num % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and num!= 1):
        print(" %d" %num, end = '  ')
    num += 1
print()
print("------------------------------------------------------------")
print("Решение 3 задания")

initial_number_of_money = int(input("Введите исходную сумму средств: "))

if initial_number_of_money >= 1000:
    guess_number = ""
    while initial_number_of_money != 0:
        if guess_number == "STOP":
            break
        print("Сумма ваших денег", initial_number_of_money, sep=" ")
        sum_bet = int(input("Введите сумму ставки: "))
        print("------------------------------------------------------------")
        if initial_number_of_money - sum_bet < 0:
            print("Сумма ставки не может быть больше ваших исходных средств.")
            print("------------------------------------------------------------")
            continue
        i = 1
        random_number = randint(1, 10)
        while i <= 3:
            print("Количество попыток угадать число {attempt} из 3".format(attempt = i))
            guess_number = input("Введите число от 1 до 10 или слово 'STOP' чтобы завершить игру: ")
            if  guess_number == "STOP":
                break
            elif int(guess_number) == random_number:
                print("Ура!!! Число угадано. Сумма вашей ставки удваивается")
                sum_bet *= 2
                initial_number_of_money += sum_bet
                print("------------------------------------------------------------")
                break
            elif i == 3:
                print("Использованы все попытки угадать число. Ваша ставка сгорает")
                initial_number_of_money -= sum_bet
                print("------------------------------------------------------------")
                break
            print("Увы. Вы не угадали число. Попробуйет еще раз!")
            print("------------------------------------------------------------")
            i += 1
    print("Игра окончена")
else:
    print("Исходная сумма средств должна быть от 1000 у.е.для игры")
    print("------------------------------------------------------------")
