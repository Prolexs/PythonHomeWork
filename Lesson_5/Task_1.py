def power(A, B):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return power(A * A, B // 2)
    else:
        return A * power(A, B - 1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

result = power(a, b)

print(f"{a}^{b} = {result}")
