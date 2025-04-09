print(f'"".join("0123456789ABCDEF"[int(d)] for d in hex(int(input()))[2:].upper())')
