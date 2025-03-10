class CustomList:
    def __init__(self, capacity=10):
        self._array =[None] * capacity
        self._capacity = capacity
        self._size=0
        print(f"New CustomList with Capacity: {self._capacity}")
        print(f"Curret Size: {self._size}")
    def append(self, element):
        if self._size < self._capacity:
            self._array[self._size]= element
            self._size += 1
            print(f"Append {element} to the list")
        else:
            print("error, list is full")
    def get(self, index):
        if 0 <= index < self._size:
            print(f"Element at index {index}:{self._array[index]}")
            return self._array[index]
        else:
            print(f"Error: index out of bounds")
            return None
    def set(self, index, element):
        if 0 <= index < self._size:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print(f"Error: index out of bounds")
    def size(self):
        print(f"Current size: {self._size}")
        return self._size
    
CustomList= CustomList()
CustomList.append(5)
CustomList.get(0)
CustomList.set(0, 10)
CustomList.size()
