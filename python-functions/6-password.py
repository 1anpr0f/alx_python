

def validate_password(password):
    if len(password) < 8:
        return False
    elif len(password) > 8:
        for i in password:
            if i.islower():
                return False
            elif i == " ":
                return False
            return True
        
    