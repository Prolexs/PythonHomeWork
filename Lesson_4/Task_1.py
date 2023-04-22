n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    set1.add(int(input()))

print("Введите элементы второго множества:")
for i in range(m):
    set2.add(int(input()))

intersection = sorted(list(set1 & set2))

print("Элементы, которые встречаются в обоих множествах без повторений и в порядке возрастания:")
for elem in intersection:
    print(elem)
