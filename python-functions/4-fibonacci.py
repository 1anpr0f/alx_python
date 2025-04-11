def fibonacci_sequence(n):
    empty = []
    a = 0 
    b = 1
    for _ in range(n):
        a,b = b,a+b
        empty.insert(0,0)
        empty.append(a)
    return empty
    