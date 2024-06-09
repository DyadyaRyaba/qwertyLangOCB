from functools import reduce

def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:  # четное n
        return reduce(lambda x, y: x * y, range(2, n + 1, 2))
    else:  # нечетное n
        return reduce(lambda x, y: x * y, range(1, n + 1, 2))

n = 7
result = double_factorial(n)
print(f"Двойной факториал {n}!! = {result}")
