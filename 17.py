class Car:
    def __init__(self, brand, power, seats):
        self.brand = brand
        self.power = power
        self.seats = seats

    def quality(self):
        Q = 0.1 * self.power * self.seats
        return Q

    def display_info(self, current_year=None):
        print(f"Марка автомобиля: {self.brand}")
        print(f"Мощность двигателя: {self.power} кВт")
        print(f"Число мест: {self.seats}")
        print(f"Качество: {self.quality()}")

class AdvancedCar(Car):
    def __init__(self, brand, power, seats, year):
        super().__init__(brand, power, seats)
        self.year = year

    def quality(self, current_year):
        base_quality = super().quality()
        Qp = base_quality - 1.5 * (current_year - self.year)
        return Qp

    def display_info(self, current_year):
        print(f"Марка автомобиля: {self.brand}")
        print(f"Мощность двигателя: {self.power} кВт")
        print(f"Число мест: {self.seats}")
        print(f"Год выпуска: {self.year}")
        print(f"Качество с учётом года выпуска: {self.quality(current_year)}")

# Демонстрация работы классов
def main():
    current_year = 2024

    car1 = Car("Toyota", 100, 5)
    car1.display_info()

    print("\n")

    car2 = AdvancedCar("Honda", 150, 4, 2018)
    car2.display_info(current_year)

if __name__ == "__main__":
    main()
