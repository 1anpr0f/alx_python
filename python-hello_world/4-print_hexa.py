def div(i):
    hex_chars = "0123456789ABCDEF"
    result = ""
    if i == 0:
        return "0"

    while i > 0:
        rem = i % 16
        result = hex_chars[rem] + result  # prepend the character
        i = i // 16

    return result

# Test for numbers 0–98
for i in range(99):
    print(f"{i} => {div(i)}")