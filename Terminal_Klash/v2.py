import random

class Player:
    def __init__(self, name, hp, attack_min, attack_max):
        self.name = name
        self.hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max
        
    def return_status(self, hp):
        if self.hp == 100:
            return "Max Health"
        if 75 <= self.hp < 100:
            return "Fine"
        if 50 <= self.hp < 75:
            return "A little hurt"
        if 25 < self.hp < 50:
            return "Be Careful"
        if 10 < self.hp < 25:
            return "Cautions required"
        if self.hp <= 10:
            return "Ok you're cooked"

    def attack(self):
            self.attack_min = 5
            self.attack_max = 25
            attack_choice = input("Which attack do you want to use? 1. Punch 2. Laser 3. Heal 15 HP")
            if attack_choice == "1":
                self.attack_min += 2
                self.attack_max += 4
                damage = random.randint(self.attack_min, self.attack_max)
                print(f"{self.name} attacks for {damage} damage!")
            
            elif attack_choice == "2":
                self.attack_min += 1
                self.attack_max += 3
                damage = random.randint(self.attack_min, self.attack_max)
                print(f"{self.name} attacks for {damage} damage!")
                
            elif attack_choice == "3":
                self.hp += 15
                return 0

            if attack_choice == "1":
                self.attack_min -= 2
                self.attack_max -= 4
            elif attack_choice == "2":
                self.attack_min -= 1
                self.attack_max -= 3
                
            return damage
            
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            return "Game Over!"
            exit()
            
    def is_dead(self):
        is_dead = self.hp <= 0
        return is_dead

    
class Enemy:
    def __init__(self, name, hp, attack_min, attack_max):
        self.name = name
        self.hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max
        
    def attack(self):
            self.attack_min = 5
            self.attack_max = 25
            damage = random.randint(self.attack_min, self.attack_max)
            print(f"{self.name} attacks for {damage} damage!")
            return damage
            
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            
            
    def is_dead(self):
        return self.hp <= 0
        
name = input("What is your username? Don't use your real name.")
species = input("What is your species?")
print(f"Alright, {name} the {species}, get ready for war!")

enemy_names = ["Zombie", "Skelekton", "Monster", "Hacker"]

final_enemy_name = random.choice(enemy_names)

player = Player(name, 100, 5, 15)
enemy = Enemy(final_enemy_name, 100, 5, 15)

while True:
    player_damage = player.attack()
    enemy.take_damage(player_damage)
    if enemy.is_dead():
        print("You win!")
        exit()
    else:
        print(f"Your HP: {player.hp}")
        print(f"Enemy HP: {enemy.hp}")
    enemy_damage = enemy.attack()
    player.take_damage(enemy_damage)
    if player.is_dead():
        print("Game Over!")
        exit()