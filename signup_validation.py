import re

def validate_username(username):
    if re.match(r"^[a-zA-Z0-9_-]{3,20}$", username):
        return True
    else:
        return False

def validate_password(input_password, confirm_password):
    if re.match(r"^[a-zA-Z0-9_-]{3,20}$", input_password):
        if (input_password == confirm_password):
            return True
    else:
        return False

def validate_email(email):
    if re.match(r"^[\S]+@[\S]+.[\S]+$", email):
        return True
    elif len(email) == 0:
        return True
    else:
        return False
