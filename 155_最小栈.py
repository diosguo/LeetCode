class MinStack:

    def __init__(self):
        self.queue = []
        self.min_queue = []

    def push(self, val: int) -> None:
        """
        还可以通过，只存一个最小值，然后栈中每个元素存储的
        都是和当时最小值的差值，即可以实现只使用常数空间实
        现最小栈
        """
        if self.queue:
            if val < self.min_queue[-1]:
                self.min_queue.append(val)
            else:
                self.min_queue.append(self.min_queue[-1])
        else:
            self.min_queue.append(val)
        self.queue.append(val)

    def pop(self) -> None:
        self.min_queue.pop(-1)
        return self.queue.pop(-1)

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return self.min_queue[-1]