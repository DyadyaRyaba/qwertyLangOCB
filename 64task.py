def transfer_students_iterative(group1, group2, n, k):

    for _ in range(k):
        if n > len(group1):
            raise ValueError("Количество студентов для перевода больше, чем количество студентов в первой группе.")

        # Переносим n студентов из group1 в group2
        students_to_transfer = group1[:n]
        group2.extend(students_to_transfer)

        # Удаляем этих студентов из group1
        group1 = group1[n:]

    return group1, group2


# Пример использования
group1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]
group2 = ["Кузьмин", "Попов", "Соколов"]

n = 1  # Переводим по 1 студенту за итерацию
k = 1  # Количество итераций

group1, group2 = transfer_students_iterative(group1, group2, n, k)
print("Первая группа после перевода:", group1)
print("Вторая группа после перевода:", group2)
