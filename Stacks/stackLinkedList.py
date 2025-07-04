class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None  # Top of the stack

    # Push operation
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        print(f"{value} pushed to stack.")

    # Pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! No elements to pop.")
            return -1
        poppedValue = self.top.val
        self.top = self.top.next
        return poppedValue

    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return -1
        return self.top.val

    # Check if the stack is empty
    def isEmpty(self):
        return self.top is None


# Main method to demonstrate stack operations
if __name__ == "__main__":
    stack = StackLinkedList()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())  # Output: 30

    print("Popped:", stack.pop())  # Output: 30
    print("Popped:", stack.pop())  # Output: 20

    print("Is stack empty?", stack.isEmpty())  # Output: False
    stack.pop()  # Popping last element
    print("Is stack empty?", stack.isEmpty())  # Output: True
