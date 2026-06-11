class Human:
  def __init__(self, name, age, yt, favpet):
    self.name = name
    self.age = age
    self.yt = yt
    self.favpet = favpet
    
  def __str__(self):
    if self.favpet and self.favpet[0].lower() in "aeiou":
      article = "an"
    else:
      article = "a"
      
    return f"My name is {self.name}, I'm {self.age}, I have a YouTube channel called {self.yt}, and my favorite animal is {article} {self.favpet}."


# 📦 Load existing people
people = []

try:
  with open("people.txt", "r") as file:
    for line in file:
      name, age, yt, favpet = line.strip().split("|")
      people.append(Human(name, age, yt, favpet))
except FileNotFoundError:
  pass


# 🎮 Main loop (menu system)
while True:
  print("\n--- MENU ---")
  print("1. Add person")
  print("2. Show all people")
  print("3. Save & exit")

  choice = input("Choose: ")

  # ➕ Add person
  if choice == "1":
    x = input("Type in your name: ")
    y = input("Now your age: ")
    z = input("Now your YouTube Channel: ")
    a = input("And finally your favorite pet: ")

    people.append(Human(x, y, z, a))
    print("Added! 😄")

  # 👀 Show people
  elif choice == "2":
    print("\n--- PEOPLE ---")
    for p in people:
      print(p)

  # 💾 Save + exit
  elif choice == "3":
    with open("people.txt", "w") as file:
      for p in people:
        file.write(f"{p.name}|{p.age}|{p.yt}|{p.favpet}\n")

    print("Saved! 💾✨ Byeee!")
    break

  else:
    print("Invalid option 😹 try again")