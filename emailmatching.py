import re

def is_valid_email(email):
    # Define the regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Compile the pattern
    regex = re.compile(pattern)
    
    if regex.match(email):
        ans = "email valid!!"
    else:
        ans = "invalid email"
    return ans