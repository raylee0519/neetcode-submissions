class MinStack:

    def __init__(self):
        self.stack = []
        self.getmin = float('inf')
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.getmin = min(val, self.getmin)
        self.minstack.append(self.getmin)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if self.minstack:
            self.getmin = self.minstack[-1]
        else:
            self.getmin = float('inf')
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]