import re

def valid_email(email):
    try:
        pattern = r"(([a-z0-9._%-]+)@([a-z0-9.-]+\.[a-z]{2,}))"
        if re.match(pattern, email) == None:
            return "Email is not valid"
    except (ValueError, TypeError):
        return "Email is not valid"
    else:
        return "Email is valid"
