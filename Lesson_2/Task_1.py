import random

n = int(input("Введите количество монет: "))

coins = [random.choice(['Р', 'О']) for _ in range(n)]

min_flips = min(coins.count('Р'), coins.count('О'))

print(f"Последовательность монет: {' '.join(coins)}")
print(f"Минимальное количество монет, которые нужно перевернуть: {min_flips}")