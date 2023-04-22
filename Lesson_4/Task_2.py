import random

n = int(input("Введите количество кустов на окружности: "))

# Создаем список кустов с случайным количеством ягод от 2 до 15
bushes = [[i, random.randint(2, 15)] for i in range(n)]

# Связываем каждый куст с его левым и правым соседом
for i in range(n):
    bushes[i].append(bushes[(i-1) % n])
    bushes[i].append(bushes[(i+1) % n])

# Выводим информацию о каждом кусте
for i in range(n):
    print(f"Куст {bushes[i][0]}: {bushes[i][1]} ягод, левый сосед - {bushes[i][2][0]}, правый сосед - {bushes[i][3][0]}")

# Запрашиваем у пользователя номер куста
bush_number = int(input("Введите номер куста: "))

# Вычисляем количество ягод на выбранном кусте и его соседях
berries_count = bushes[bush_number][1] + bushes[bush_number][2][1] + bushes[bush_number][3][1]

# Выводим результат
print(f"Количество ягод на кусте {bush_number} и его соседях: {berries_count}")
