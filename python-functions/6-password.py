
def validate_password(password):
    has_space = False
    has_upper = False
    if len(password) < 8:
        return False
    elif len(password) > 8:
           for i in password:
               if i.isupper():
                   has_upper=True
               if i == " ":
                   has_space = True
           if has_upper and not has_space:
               return True
           else:
               return False
  