class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # PUSH
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # POP
    def pop(self):
        if self.top is None:
            return "Stack is empty"
        
        popped = self.top.data
        self.top = self.top.next
        return popped

    # PEEK
    def peek(self):
        if self.top is None:
            return "Stack is empty"
        return self.top.data

    # IS EMPTY
    def is_empty(self):
        return self.top is None

    # DISPLAY
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------- DRIVER CODE --------

s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()              # 30 -> 20 -> 10 -> None

print("Top:", s.peek())  # Top: 30

print("Empty?", s.is_empty())  # False

print("Popped:", s.pop())      # 30

s.display()              # 20 -> 10 -> None