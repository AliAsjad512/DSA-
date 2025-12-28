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
