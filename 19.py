class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def get_bosh_products(self):
        if not self.head:
            return []

        bosh_products = []
        current = self.head
        while True:
            if current.data['manufacturer'] == 'Bosh':
                bosh_products.append(current.data)
            current = current.next
            if current == self.head:
                break

        return bosh_products

    def display(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

circular_list = CircularLinkedList()

circular_list.append({'name': 'Product1', 'manufacturer': 'Bosh'})
circular_list.append({'name': 'Product2', 'manufacturer': 'Samsung'})
circular_list.append({'name': 'Product3', 'manufacturer': 'Bosh'})
circular_list.append({'name': 'Product4', 'manufacturer': 'LG'})

print("Все товары в кольцевом списке:")
circular_list.display()

bosh_products = circular_list.get_bosh_products()

print("\nТовары фирмы Bosh:")
for product in bosh_products:
    print(product)
