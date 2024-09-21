# Examples of recursion in python

def recursion(n):
    if n<1:
        print("complete")
        return
    else:
        recursion(n-1)
        print(n)



# output of recursion(10):

# complete
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# factorial in recursion

def factorial(n):
    if n==0 or n==1:
        print('1')
        return
    else:
        x = n*factorial(n-1)        