# Функція для обчислення чисел Фібоначчі
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

# Введення кількості чисел у послідовності Фібоначчі
n = int(input("Введіть кількість чисел Фібоначчі: "))

# Виклик функції і виведення результату
print(f"Перші {n} чисел Фібоначчі: {fibonacci(n)}")

