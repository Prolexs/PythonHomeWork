import random

# Запрашиваем у пользователя длину массива
length = int(input("Введите длину массива: "))

# Генерируем случайные числа и записываем их в массив
arr = [random.randint(1, 100) for _ in range(length)]

# Выводим массив на экран
print("Сгенерированный массив:", arr)

# Запрашиваем у пользователя число, для которого нужно найти ближайшее значение
num = int(input("Введите число: "))

# Инициализируем переменные для хранения наименьшего расстояния и наименьшего числа
min_distance = abs(num - arr[0])
closest_num = arr[0]

# Ищем ближайшее число
for i in range(1, length):
    distance = abs(num - arr[i])
    if distance < min_distance:
        min_distance = distance
        closest_num = arr[i]

# Выводим результат
print(f"Ближайшее число к {num} в массиве: {closest_num}")
