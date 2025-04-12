
def validate_password(password):
    if len(password) < 8:
        return False
    has_space = False
    has_upper = False
    
    for i in password:
        if i.isupper():
            has_upper=True
        if i == " ":
            has_space = True
    if has_upper and not has_space:
        return False
    else:
        return True
    
  