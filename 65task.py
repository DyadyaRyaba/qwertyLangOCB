def generate_purchase_list(products, buyers):

    purchase_list = []
    for i in range(min(len(products), len(buyers))):
        purchase_list.append(f"{buyers[i]} покупает {products[i]}")
    return purchase_list

# Пример использования
products = ["product" + str(i) for i in range(1, 5)]

buyers = ["buyer" + str(i) for i in range(1, 5)]

purchase_list = generate_purchase_list(products, buyers)
for purchase in purchase_list:
    print(purchase)
