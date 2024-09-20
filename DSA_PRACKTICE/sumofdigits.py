def sum_of_digits(n):
    assert n>=0 and int(n) == n, 'Positive integer only'
    if int(n/10) <=9:
        return int(n%10) + int(n/10)
    else:
        return int(n%10) + sum_of_digits(int(n/10))


print(sum_of_digits(0))