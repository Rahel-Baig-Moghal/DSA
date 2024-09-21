from collections import deque

q = deque()

q.append(5)
q.append(6)
q.append(7)
q.append(8)

print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# -------------------------output------------------
# deque([5, 6, 7, 8])
# 8
# 7
# 6
# 5
# --------------------------------------------------