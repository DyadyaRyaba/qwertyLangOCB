class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_after_nth(self, data, n):
        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < n:
            current = current.next
            count += 1

        if current:
            new_node.next = current.next
            current.next = new_node
        else:
            print("Элемент с указанным индексом не найден.")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Исходный список:")
ll.display()

ll.insert_after_nth(5, 2)

print("\nСписок после вставки элемента после 2-го элемента:")
ll.display()
