import string
import secrets
import pyperclip


password_iter = 8
leng = 12
id_counter = 1


def generate_strong_password(leng):
   if leng < 6:
       raise ValueError("Password length must be at least 6 characters.")
   lower = string.ascii_lowercase
   upper = string.ascii_uppercase
   digits = string.digits
   symbols = string.punctuation
   password_parts = [secrets.choice(lower), secrets.choice(upper), secrets.choice(digits), secrets.choice(symbols)]

   all_characters = lower + upper + digits + symbols

   password_parts += [secrets.choice(all_characters) for _ in range(leng - 4)]

   secure_generator = secrets.SystemRandom()
   secure_generator.shuffle(password_parts)
   return ''.join(password_parts)




def check_password_iter():
   password_iter = input("How many passwords do you want to make?")
   while True:
      try:
         password_iter = int(password_iter)
         break
      except ValueError:
         print("Invalid answer! Numbers only.")
         print("1, 2, 3 etc")
         break


def check_leng():
   leng = input("How long do you want each password to be?")
   while True:
      try:
         leng = int(leng)
         break
      except ValueError:
         print("Invalid answer! Numbers only.")
         print("1, 2, 3 etc")
         break

check_password_iter()
check_leng()

for v in range(password_iter):
   print(f"Secure Password:", generate_strong_password(leng))

do_i_copy = input("Do you want to copy a password to your clipboard? y = yes N = No")

if do_i_copy == "y":
   pyperclip.copy(generate_strong_password(leng))