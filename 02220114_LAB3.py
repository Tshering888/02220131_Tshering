#Second part: Implementing stack using linkedlist representation.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0
        print("Created new LinkedStack")
        print(f"Stack is empty: {self.is_empty()}")

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_element = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Popped element: {popped_element}")
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        stack_elements = []
        while current:
            stack_elements.append(str(current.data))
            current = current.next
        print("Display stack: [" + ", ".join(stack_elements) + "]")

stack = LinkedStack()
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.peek()
stack.pop()
stack.display()
print(f"Stack size: {stack.size}")