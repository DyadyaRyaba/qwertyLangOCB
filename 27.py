class Student:
    def __init__(self, name):
        self.__name = name
        self.__disciplines = {}

    def put(self, discipline, grade):
        if isinstance(discipline, str) and isinstance(grade, (int, float)):
            self.__disciplines[discipline] = grade
        else:
            raise ValueError("Название дисциплины должно быть строкой, а оценка числом")

    @property
    def name(self):
        return self.__name

    @property
    def disciplines(self):
        return self.__disciplines

    @property
    def passed_disciplines(self):
        return list(self.__disciplines.keys())

    def __str__(self):
        disciplines_str = ', '.join(f"{key}: {value}" for key, value in self.__disciplines.items())
        return f"Студент: {self.__name}, Дисциплины: {disciplines_str}"

student = Student("Иванов")

student.put("Математика", 5)
student.put("Физика", 4)
student.put("Химия", 3)

print(student)
print("Список сданных дисциплин:", student.passed_disciplines)
print("Имя студента:", student.name)
