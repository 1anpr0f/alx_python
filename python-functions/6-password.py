
def validate_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_space = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char == " ":
            has_space = True

    if has_upper and has_lower and has_digit and not has_space:
        return True
    else:
        return False                              