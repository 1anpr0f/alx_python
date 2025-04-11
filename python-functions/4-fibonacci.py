def fibonacci_sequence(n):
    empty = []
    for _ in range(n):
        a = 0 
        b = 1
        a,b = b,a+b
        empty.append(a)
    return empty
    