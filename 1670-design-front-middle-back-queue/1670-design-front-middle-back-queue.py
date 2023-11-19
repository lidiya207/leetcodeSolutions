class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        middle = len(self.queue) // 2
        self.queue.insert(middle, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.queue:
            middle = (len(self.queue) - 1) // 2
            return self.queue.pop(middle)
        return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1

# Example usage:
# obj = FrontMiddleBackQueue()
# obj.pushFront(1)
# obj.pushBack(2)
# obj.pushMiddle(3)
# param_4 = obj.popFront()  # Returns 1
# param_5 = obj.popMiddle() # Returns 3
# param_6 = obj.popBack()   # Returns 2
