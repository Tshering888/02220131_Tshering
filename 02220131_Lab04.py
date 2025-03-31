#Part one Array-based_Queue
class ArrayQueue:
    def __init__(self, capacity=10):
        #Initialize the queue with a given capacity
        self.capacity = capacity
        self.queue = [None] * capacity  # Fixed-size array
        self.front = -1  # Index of the front element
        self.rear = -1   # Index of the rear element
        self.size = 0    # Number of elements in the queue
        print(f"Created new Queue with capacity: {capacity}")
        print(f"Queue is empty: {self.is_empty()}")

    def is_empty(self):
        #Check if the queue is empty.
        return self.size == 0

    def is_full(self):
        #Check if the queue is full.
        return self.size == self.capacity

    def enqueue(self, element):
        #Add an element to the rear of the queue.
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        
        if self.is_empty():
            self.front = 0  # First element being added

        self.rear = (self.rear + 1) % self.capacity  # Moves rear index forward & index wraps when reaching the end of array
        self.queue[self.rear] = element
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
       #Remove and return the element at the front.
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None

        element = self.queue[self.front]
        self.queue[self.front] = None  # Clear the dequeued position
        self.front = (self.front + 1) % self.capacity  # Circular increment
        self.size -= 1

        if self.is_empty():
            self.front = self.rear = -1  # Reset when queue is empty

        print(f"Dequeued element: {element}")
        self.display()
        return element

    def peek(self):
        #Return the front element without removing it.
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
            return None
        return self.queue[self.front]

    def get_size(self):
        #Return the number of elements in the queue.
        return self.size

    def display(self):
        #Show all elements in the queue.
        if self.is_empty():
            print("Display queue: []")
            return
        
        elements = []
        index = self.front
        for _ in range(self.size):
            elements.append(self.queue[index])
            index = (index + 1) % self.capacity  # Circular increment
        print(f"Display queue: {elements}")

# Example usage:
queue = ArrayQueue(10)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(f"Front element: {queue.peek()}")
queue.dequeue()
print(f"Queue size: {queue.get_size()}")