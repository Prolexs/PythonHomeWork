# Задача 6:  Вам требуется написать программу, которая проверяет счастливость билета.

num = input("Введите шестизначное число: ") # получаем шестизначное число от пользователя

# проверяем, является ли число шестизначным
if len(num) != 6:
    print("Вы ввели неверное число.")
else:
    # вычисляем сумму первых трех чисел и вторых трех чисел
    sum1 = int(num[0]) + int(num[1]) + int(num[2])
    sum2 = int(num[3]) + int(num[4]) + int(num[5])

    # сравниваем суммы и выводим результат
    if sum1 == sum2:
        print("Поздравляем! Вам выпал счастливый билет.")
    else:
        print("К сожалению, это не счастливый билет.")
