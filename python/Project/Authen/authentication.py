import time

users = {
    "ali": "pass123",
    "admin": "admin@123"
}

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful")
        print("Login time:", time.ctime())
        break
    else:
        attempts -= 1
        print(f"Wrong credentials. Attempts left: {attempts}")

if attempts == 0:
    print("Account locked")


    import re

def check_password(password):
    requirements = []

    if len(password) < 8:
        requirements.append("at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        requirements.append("at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        requirements.append("at least one lowercase letter")
    if not re.search(r"[0-9]", password):
        requirements.append("at least one digit")
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{}|;':\",.<>/?]", password):
        requirements.append("at least one special character")

    if not requirements:
        print("Strong password ✅")
    else:
        print("Weak password. Missing requirements:")
        for r in requirements:
            print(f"- {r}")

# Example usage:
password_input = input("Enter your password: ")
check_password(password_input)

