import random

# Запрашиваем у пользователя длину массива
length = int(input("Введите длину массива: "))

# Генерируем случайные числа и записываем их в массив
arr = [random.randint(1, 10) for _ in range(length)]

# Выводим массив на экран
print("Сгенерированный массив:", arr)

# Запрашиваем у пользователя число, которое нужно найти в массиве
num = int(input("Введите число для поиска: "))

# Считаем количество вхождений числа в массив
count = arr.count(num)

# Выводим результат
print(f"Число {num} встречается в массиве {count} раз(а)")
