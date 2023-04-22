def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = sum(a, b)

print(f"{a} + {b} = {result}")
