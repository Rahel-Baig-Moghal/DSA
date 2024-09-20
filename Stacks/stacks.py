# stacks is last in first out data structure (LIFO)
# stack.push() method to add element to the top
# stack.pop() removes and returns elements from the top
# stack.peek() to returns elements at the top
# stack.isEmpty() Checks if the stack is empty
# stack.Size() finds the number of elements in the stack

# Implementation of Stack in python using arrays

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]   

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
my_stack = Stack()

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

print("Stack: ", my_stack.stack)

print("Pop: ", my_stack.pop())

print("Peek: ", my_stack.peek())

print("isEmpty: ", my_stack.isEmpty())

print("Size: ", my_stack.size())


# output :
#  
# Stack:  ['A', 'B', 'C']
# Pop:  C
# Peek:  B
# isEmpty:  False
# Size:  2