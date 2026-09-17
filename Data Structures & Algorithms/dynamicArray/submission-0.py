class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None for i in range(capacity)]
        self.size = -1

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if self.size >= len(self.array):
            self.resize()
        self.array[self.size] = n
        

    def popback(self) -> int:
        value = self.array[self.size]
        self.array[self.size] = None
        self.size -= 1
        return value

    def resize(self) -> None:
        self.array.extend([None] * len(self.array))

    def getSize(self) -> int:
        return self.size + 1
    
    def getCapacity(self) -> int:
        return len(self.array)
