class Money:
    def __init__(self, rubles, kopecks):
        self.rubles = rubles
        self.kopecks = kopecks

    def __str__(self):
        return f"{self.rubles} руб. {self.kopecks} коп."

    def _normalize(self):
        if self.kopecks >= 100:
            self.rubles += self.kopecks // 100
            self.kopecks = self.kopecks % 100
        elif self.kopecks < 0:
            self.rubles -= (abs(self.kopecks) // 100) + 1
            self.kopecks = 100 - (abs(self.kopecks) % 100)

    def __add__(self, other):
        rubles = self.rubles + other.rubles
        kopecks = self.kopecks + other.kopecks
        result = Money(rubles, kopecks)
        result._normalize()
        return result

    def __sub__(self, other):
        rubles = self.rubles - other.rubles
        kopecks = self.kopecks - other.kopecks
        result = Money(rubles, kopecks)
        result._normalize()
        return result

    def __truediv__(self, divisor):
        total_kopecks = (self.rubles * 100) + self.kopecks
        total_kopecks //= divisor
        rubles = total_kopecks // 100
        kopecks = total_kopecks % 100
        return Money(rubles, kopecks)

    def divide_sum(self, divisor):
        return self.__truediv__(divisor)

money1 = Money(10, 50)
money2 = Money(5, 75)

print("Сложение: ", money1 + money2)
print("Вычитание: ", money1 - money2)
print("Деление: ", money1 / 2)
print("Деление суммы: ", money1.divide_sum(3))
