
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        size = len(self.q)
        for _ in range(size - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        size = len(self.q)
        for _ in range(size - 1):
            self.q.append(self.q.popleft())
        top_element = self.q.popleft()
        self.q.append(top_element)
        return top_element

    def empty(self) -> bool:
        return len(self.q) == 0
