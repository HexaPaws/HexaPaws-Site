print("Hello! Welcome to our smart bank called HexaBank!")
name = input("What is your name? >>>>")
money = input("How much money do you currently have? >>>>")
moneynum = float(money)
print(moneynum)
while True:
 v = input("Add more money or decrease money. + - >>>>")
 if v == "+":
   a = input(f"How much money is added to your {moneynum}? >>>>")
   b = float(a)
   moneynum +=b
   print(f"Your new value is {moneynum}!") 
 elif v == "-":
   s = input(f"How much money is subtracted from your {moneynum}? >>>>")
   t = float(s)
   moneynum -=t
   print(f"Your new value is {moneynum}!") 
 else:
   print("Not a valid command! >>>>")