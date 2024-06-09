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

    def split_groups(self):
        if not self.head:
            return [], []

        group1 = []
        group2 = []

        current = self.head
        index = 0
        while len(group1) < 10 or len(group2) < 10:
            index += 1
            if index % 11 == 0:
                group2.append(current.data)
            else:
                group1.append(current.data)

            current = current.next
            if current == self.head:
                break

        return group1, group2

students = ["Student" + str(i) for i in range(1, 21)]
circular_list = CircularLinkedList()
for student in students:
    circular_list.append(student)

group1, group2 = circular_list.split_groups()

print("Группа 1:", group1)
print("Группа 2:", group2)
