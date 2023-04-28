def find_indexes(lst, min_val, max_val):
    """
    Функция, которая принимает список, минимальное и максимальное значения,
    и возвращает индексы элементов списка, значения которых находятся в заданном диапазоне.
    """
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

# Запрос ввода данных у пользователя
lst = [int(x) for x in input("Введите элементы списка через пробел: ").split()]
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

# Вызов функции и вывод результата
result = find_indexes(lst, min_val, max_val)
print(result)
