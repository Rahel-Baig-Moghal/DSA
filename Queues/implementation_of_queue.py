from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.buffer.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.buffer[-1]
    
    def isEmpty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.peek())
print(pq.size())
print(pq.isEmpty())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())

# ===========output========================================================
# {'company': 'Wall Mart', 'timestamp': '15 apr, 11.01 AM', 'price': 131.1}# 3
# False
# {'company': 'Wall Mart', 'timestamp': '15 apr, 11.01 AM', 'price': 131.1}
# {'company': 'Wall Mart', 'timestamp': '15 apr, 11.02 AM', 'price': 132}
# {'company': 'Wall Mart', 'timestamp': '15 apr, 11.03 AM', 'price': 135}
# ==========================================================================