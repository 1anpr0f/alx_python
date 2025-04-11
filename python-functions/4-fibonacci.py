def fibonacci_sequence(n):
    empty = []
    a,b = 0,1 
    for _ in range(n):
        empty.append(a)
        a,b = b,a+b
        
    return empty

