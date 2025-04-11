def fibonacci_sequence(n):
    a = 0
    b = 1
    for _ in range(n):
        a,b = b,a+b
        return list(map(str,a))
    