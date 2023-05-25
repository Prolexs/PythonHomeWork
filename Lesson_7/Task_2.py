def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            print(f'{result:5}', end=' ')
        print()

# Функция для вычисления произведения
def multiply(x, y):
    return x * y

# Вывод таблицы произведений чисел от 1 до 6
print_operation_table(multiply)
