class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display_info(self):
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Площадь: {self.area()}")

class AdvancedRectangle(Rectangle):
    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        super().display_info()
        print(f"Периметр: {self.perimeter()}")

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Вычислить площадь прямоугольника")
        print("2. Вычислить периметр прямоугольника")
        print("3. Выход")
        choice = input("Выберите действие (1/2/3): ")

        if choice == '1' or choice == '2':
            length = float(input("Введите длину: "))
            width = float(input("Введите ширину: "))
            if choice == '1':
                rect = Rectangle(length, width)
                rect.display_info()
            elif choice == '2':
                adv_rect = AdvancedRectangle(length, width)
                adv_rect.display_info()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main_menu()
