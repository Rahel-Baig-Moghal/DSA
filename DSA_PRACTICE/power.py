def power(base, exponent):
    assert exponent>=0 and int(exponent) == exponent, 'The exponent must be a positive integer'
    if exponent==0:
        return 1
    elif exponent==1:
        return base
    else:
        return base * power(base, exponent-1)
    
print(power(2, 1))