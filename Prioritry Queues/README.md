### What is a priority Queue?
1. A priority queue is a abstract data type(ADT) that operates similar to a normal queue except each element has a certain priority. 

2. The priority of elements in the priority queue determine the order in which elements are removed from the PRIORITY QUEUE.

3. If two elements have the same priority, they are served according to their order in the queue.
   
**NOTE: priority queue only support comparable data.data must be able to be ordered in the some way for example acending to decending or reverse.**

### When and where Priority Queue is used?

1. Used in certain implementations of Dijkstra's Shortest path algorithm

2. Anytime you need the dynamically fetch the **next best** or **next worst** elements.

3. Used in Huffman coding (used for lossless data compression).

### Types of Priority Queues:

**Acending order Priority Queue:**
-  The element with a lower priority value is given a higher priority.
-  For example, in priority queue 4,6,8,9,10; 4 is the smallest number, therefore, it will get the highest priority.
-  dequeue from this type of priority queue, 4 will remove from the queue and dequeue returns 4.

**Descending order Priority Queue**
