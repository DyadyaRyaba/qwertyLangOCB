class Order:
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def __str__(self):
        return f"Код товара: {self.code}, Цена: {self.price}, Количество: {self.count}"

class Opt(Order):
    def __init__(self, code, price, count):
        super().__init__(code, price, count)

    def summa(self):
        if self.count > 500:
            unit_price = 0.9 * self.price
        else:
            unit_price = 0.95 * self.price
        return unit_price * self.count

    def __str__(self):
        return super().__str__() + f", Сумма заказа: {self.summa()}"

class Retail(Order):
    def __init__(self, code, price, count):
        super().__init__(code, price, count)

    def summa(self):
        return self.price * self.count

    def __str__(self):
        return super().__str__() + f", Сумма заказа: {self.summa()}"

orders = [
    Order('A001', 100, 50),
    Order('A002', 200, 30),
    Opt('B001', 150, 600),
    Opt('B002', 150, 400),
    Retail('C001', 50, 10),
    Retail('C002', 75, 20)
]
for order in orders:
    print(order)

total_opt_retail = sum(order.summa() for order in orders if isinstance(order, (Opt, Retail)))
print(f"\nОбщая стоимость заказов для объектов Opt и Retail: {total_opt_retail}")
