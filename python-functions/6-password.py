def validate_password(password):
    if len(password) < 8:
        return False
    for i in password:
        if i.isupper():
            return True
        return False
    for i in password():
        if i == " ":
            return False
        return True