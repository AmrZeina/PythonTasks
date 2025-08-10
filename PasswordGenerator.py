import random

def generate_password(length):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    specials = "!@#$%^&*()-_=+[]{};:,.<>?"

    all_chars = uppercase + lowercase + digits + specials  # all possible characters


    password = [                                            #to make the pass has at least one of each type
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(specials)
    ]

    for i in range(length - 4):                         #complete the rest of the passwird
        password.append(random.choice(all_chars))

    random.shuffle(password)  
    return "".join(password)  # return as a string


length = int(input("Enter password length: "))              #to let the user enter the length
print("Generated password:", generate_password(length))
