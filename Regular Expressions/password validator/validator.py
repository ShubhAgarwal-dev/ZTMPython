import re

email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
password_pattern = re.compile(
    "^(?:(?:(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]))|(?:(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))|(?:(?=.*[0-9])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))|(?:(?=.*[0-9])(?=.*[a-z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]))).{8,32}$")


while True:
    email_address = input("Enter Your Email address please: ")
    a = email_pattern.search(email_address)

    if a is not None:
        print("Yes it is an email address")
        break
    else:
        print("Please check your email address")

while True:
    password = input("Enter your password please: ")
    b = password_pattern.search(password)

    if b is None:
        print("Please check your password!")
        continue
    else:
        print("Your password is Correct")
        break
