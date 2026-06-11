import string
import random
import pyperclip
import secrets

x = random.randint(1, 5)

password = ""

def generate_password():
  global x
  global password
  leng = input("How long would you like your password to be? Only actual numbers like 1, 2, 3 etc 🐱")

  leng = int(leng)

  for v in range(leng):
    match x:
      case 1:
        uppercase = secrets.choice(string.ascii_uppercase)
        password += uppercase
      case 2:
        lowercase = secrets.choice(string.ascii_lowercase)
        password += lowercase
      case 3:
        digits = secrets.choice(string.digits)
        password += digits
      case 4:
        punctuation = secrets.choice(string.punctuation)
        password += punctuation
    x = random.randint(1, 5)

  print(f"Password: {password} 🐱")

  print("Do you want to copy the password to clipboard? nya! y/n")
  do_i_copy = input(">>>")

  if do_i_copy == "y":
    pyperclip.copy(password)

  print("Do you want to create a new password? meow! y/n")
  do_i_copy = input(">>>")

  if do_i_copy == "y":
    generate_password()

generate_password()