def check_password(password):
    issues = []

    if len(password) < 8:
        issues.append("minimum 8 characters")
    if not any(c.isupper() for c in password):
        issues.append("uppercase letter")
    if not any(c.islower() for c in password):
        issues.append("lowercase letter")
    if not any(c.isdigit() for c in password):
        issues.append("digit")
    if not any(c in "!@#$%^&*" for c in password):
        issues.append("special character")

    if not issues:
        print("Strong Password")
    else:
        print("Weak Password, missing:")
        for issue in issues:
            print("-", issue)

pwd = input("Enter password: ")
check_password(pwd)
