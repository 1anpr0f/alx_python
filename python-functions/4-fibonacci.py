def fibonacci_sequence(n):
    empty = []
    a = 0 
    b = 1
    if n == 0:
        return empty
    else:
        empty.insert(0,0)
    for _ in range(n-1):
        a,b = b,a+b
        empty.append(a)
    return empty

