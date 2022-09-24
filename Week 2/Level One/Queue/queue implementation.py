class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

t = MyQueue()
t.push(1)
t.push(2)
print(t.peek()) # 1
print(t.pop()) # 1
print(t.empty()) # False
