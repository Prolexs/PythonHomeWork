a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = [a1 + (i * d) for i in range(n)]
print("Элементы прогрессии:", progression)
