class MinStack:

    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        self.q.append(val)
    def pop(self) -> None:
        val = self.top()
        self.q.pop()
        return val

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return min(self.q)
        
