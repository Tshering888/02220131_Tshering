class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Created new Linkedlist")
        print(f"Current size: {self.size}")
        print("Head = None")
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"appended {element} to the list")
    def prepend(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        print(f"Prepended {element} to the list")
    def get(self, index):
        if index  < 0 or index >= self.size:
           print(f"Error: index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}:{current.data}")
        return current.data 
    def set(self, index, element):
        if index  < 0 or index >= self.size:
            print(f"Error: index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set the element at index {index} to {element}")
    def size(self):
        return self.size
    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)
        
LinkedList = LinkedList()
LinkedList.append(5)
LinkedList.append(8)
LinkedList.append(8)
LinkedList.get(0)
LinkedList.set(0,7)
print(f"Current size: {LinkedList.size}")
LinkedList.prepend(3)
LinkedList.prepend(1)
print(f"Current size: {LinkedList.size}")
LinkedList.print_list()


    
        