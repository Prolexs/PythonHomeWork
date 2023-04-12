import random
import math

# генерируем два случайных целых числа
x = random.randint(0, 999)
y = random.randint(0, 999)

print("Сгенерированные числа:", x, "и", y)

# считаем сумму и произведение
sum = x + y
prod = x * y

# находим сгенерированные числа
D = sum * sum - 4 * prod
if D < 0:
    print("Нет решения")
elif D == 0:
    x = y = sum // 2
    print("Сгенерированные числа: ", x, y)
else:
    x1 = (sum + math.sqrt(D)) // 2
    x2 = (sum - math.sqrt(D)) // 2
    y1 = sum - x1
    y2 = sum - x2
    print("Сгенерированные числа: ", int(x1), int(y1), "или", int(x2), int(y2))