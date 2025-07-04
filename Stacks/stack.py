class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity
        self.top = -1

    def push(self, value):
        if self.top == self.capacity - 1:
            print("capacity reached, cannot push value onto stack")
            return

        self.top += 1
        self.stack[self.top] = value
        print(f"{value} pushed onto the stack")

    def pop(self):
        if self.isEmpty():
            print("Nothing to pop from the stack, stack is empty")
            return
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return -1
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1


if __name__ == "__main__":
    stack = StackArray(5)

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())  # Output: 30

    print("Popped:", stack.pop())  # Output: 30
    print("Popped:", stack.pop())  # Output: 20

    print("Is stack empty?", stack.isEmpty())  # Output: False
    stack.pop()  # Popping last element
    print("Is stack empty?", stack.isEmpty())  # Output: True
