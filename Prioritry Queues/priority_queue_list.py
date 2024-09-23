class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def insert(self, val, priority):
        self.queue.append((priority, val))
        self.queue.sort(reverse=True)

    def delete(self):
        if self.is_empty():
            return 'PriorityQueue is empty'
        return self.queue[0][1]
    
    def peek(self):
        if self.is_empty():
            return 'PriorityQueue is empty'     
        return self.queue[0][1]  
    

pq = PriorityQueue()
pq.insert("Task 1", 3)
pq.insert("Task 2", 1)
pq.insert("Task 3", 4)
pq.insert("Task 4", 2)


print(pq.delete())    

print(pq.peek())