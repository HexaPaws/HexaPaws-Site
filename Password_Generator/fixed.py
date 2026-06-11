import random
import string

global length

chars = ""


try:
    loop = input("How many times should I create a password?")
    loop = int(loop)
except ValueError:
    print("Invalid number!")

def ask_for_numbers():
    numbers = input("Should I include numbers? Y/n")
    if numbers == "Y":
        return True
    elif numbers == "n":
        return False
    else:
        print("Invalid input! Please type Y or n.")
        return ask_for_numbers()
            

def ask_for_symbols():
    symbols = input("Should I include symbols? Y/n")
    if symbols == "Y":
        return True
    elif symbols == "n":
        return False
    else:
        print("Invalid input! Please type Y or n.")
        return ask_for_symbols()
        
def ask_for_capletters():
    capletters = input("Should I include capital letters? Y/n")
    if capletters == "Y":
        return True
    elif capletters == "n":
        return False
    else:
        print("Invalid input! Please type Y or n.")
        return ask_for_capletters()

def ask_for_lowerletters():
    lowerletters = input("Should I include lowercase letters? Y/n")
    if lowerletters == "Y":
        return True
    elif lowerletters == "n":
        return False
    else:
        print("Invalid input! Please type Y or n.")
        return ask_for_lowerletters()

try:
    length = input("How long should the password be?")
    length = int(length)
except ValueError:
    print("Invalid number!")

include_numbers = ask_for_numbers()
include_symbols = ask_for_symbols()
include_capletters = ask_for_capletters()
include_lowerletters = ask_for_lowerletters()
print(f"Length: {length}")
print(f"Include numbers: {include_numbers}")
print(f"Include symbols: {include_symbols}")
print(f"Include capital letters: {include_capletters}")
print(f"Include lowercase letters: {include_lowerletters}")

if include_capletters == True:
    chars += string.ascii_uppercase
if include_lowerletters == True:
    chars += string.ascii_lowercase
if include_numbers == True:
    chars += string.digits
if include_symbols == True:
    chars += string.punctuation

print("Password created:")
print(chars)

if chars == "":
    print("You didn't choose any types")
    exit()
password = ""


with open("passwords.txt", "a") as file:
    file.write("New session:\n")
    print("Created Passwords:")
    
    for _ in range(loop):
        password = ""
        
        for _ in range(length):
            password += random.choice(chars)
            
        print(password)
        print("--------------")
        file.write(password + "\n")