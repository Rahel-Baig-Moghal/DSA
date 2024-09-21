# queue is a first in first out data structure (FIFO) 
# a collection designed for holding elements prior to processing linear data structure
# enqueue() adds new element to the queue
# dequeue() removes and returns the first element from the queue
# peek() returns the first element in the queue
# isEmpty() checks if the queue is empty
# size() finds the number of elements in the queue

# Queue implementation with python list
stock_price_tata = []

stock_price_tata.insert(0, 100.10) 
stock_price_tata.insert(0, 101.13)
stock_price_tata.insert(0, 110.17)
stock_price_tata.insert(0, 105.00)

print(stock_price_tata)
print(stock_price_tata.pop())
print(stock_price_tata.pop())
print(stock_price_tata.pop())

# -----------------output--------------------------------
# [105.0, 110.17, 101.13, 100.1]
# 100.1
# 101.13
# 110.17
# ----------------------------------------------------------