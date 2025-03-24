#The first part which is Array based stack  is done here and the other part using LinkedList based stack is done by my Partner"""
class ArrayStack:
    def __init__(self, capacity=10):
        #Initialize the stack with a default capacity.
        self._stack = [None] * capacity  # Private array to store elements
        self._top = -1  # Variable to track the top of the stack
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")
        print("Stack is empty:", self.is_empty())

    def push(self, element):
        #Add an element to the top of the stack.
        if self._top == self._capacity - 1:
            print("Stack overflow! Cannot push", element)
            return
        self._top += 1
        self._stack[self._top] = element #new element at the top
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        #Remove and return the element at the top of the stack.
        if self.is_empty():
            print("Stack underflow! Cannot pop")
            return None
        element = self._stack[self._top] 
        self._stack[self._top] = None  # Clear the reference
        self._top -= 1 #decrements top
        print(f"Popped element: {element}")
        self.display()
        return element

    def peek(self):
        #Return the element at the top without removing it.
        if self.is_empty():
            print("Stack is empty! No top element")
            return None
        print(f"Top element: {self._stack[self._top]}")
        return self._stack[self._top]

    def is_empty(self):
        #Check if the stack is empty.
        return self._top == -1

    def size(self):
        #Return the current number of elements in the stack.
        print(f"Stack size: {self._top + 1}")
        return self._top + 1

    def display(self):
        #Show all elements in the stack.
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Display stack:", self._stack[:self._top + 1])



stack = ArrayStack()  # Initialize the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.peek()
stack.pop()
stack.size()
stack.display()