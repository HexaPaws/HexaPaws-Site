import random
import string
import time
print("How long should the password be? :3")
length = int(input(">>>"))

characters = string.ascii_letters + string.digits + string.punctuation

password == ""
def create(length):
    for i in range(length):
        print(f"Your password is: {password}")
    password += random.choice(characters)
create(length)

while True:
    again = input("Generator another one? (y/n)")
    if again.lower() == "n":
        break
    if again == "y":
        password = ""
        create(length)
        
