def get_even_indices(S):
    # Используем enumerate для получения индексов и значений элементов списка
    # Затем фильтруем только четные элементы с помощью lambda
    even_indices = list(map(lambda x: x[0], filter(lambda x: x[1] % 2 == 0, enumerate(S))))
    return even_indices

S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_indices = get_even_indices(S)
print("Индексы четных элементов списка:", even_indices)
