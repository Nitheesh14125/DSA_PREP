class Node:
    def __init__(self, k):
        self.k = k
        self.next = None

    def __str__(self):
        return str(self.k)

temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2
temp2.next = temp3
head = temp1

print(f"{temp1}->{temp2}->{temp3}")