import random
import time

time.sleep(1)
print(open)
class Player:
    def __init__(self, name, hp, attack_min, attack_max, level, xp, xp_to_next):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.special_cooldown = 0
        self.level = 1
        self.xp = 0
        self.xp_to_next = 50
        

    def load_game():
        with open("save.txt", "r") as file:
            name = file.readline().strip()
            hp = int(file.readline())
            attack_min = int(file.readline())
            attack_max = int(file.readline())
            level = int(file.readline())
            xp = int(file.readline())
            xp_to_next = int(file.readline())
            player = Player(name, hp, attack_min, attack_max, level, xp, xp_to_next)
        print("📂 Game loaded!")
        return player

    def heal_full(self):
        self.hp = self.max_hp
        print(f"\n{self.name} is now fully healed! 💖")
    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount}")
        while self.xp > self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack_min += 2
        self.attack_max += 3
        self.xp_to_next = int(self.xp_to_next * 1.5)
        
        print(f"\n LEVEL UP! You are now level {self.level}!")
        print("HP increased! Attack increased!")   
        
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
        damage = 0
        self.attack_min = 5
        self.attack_max = 25
        
        if self.special_cooldown > 0:
            self.special_cooldown -= 1
        
        attack_choice = input("Which attack do you want to use? 1. Punch 2. Laser 3. Heal 15 HP 4. Special Move")
        
        while attack_choice not in ["1", "2", "3", "4"]:
            print("Not a usable command!")
            attack_choice = input("Which attack do you want to use? 1. Punch 2. Laser 3. Heal 15 HP, 4. Special Move")
            
            
        if attack_choice == "1":
            damage = random.randint(7, 29)
            print(f"{self.name} attacks for {damage} damage!")
            
        elif attack_choice == "2":
            damage = random.randint(6, 28)
            print(f"{self.name} attacks for {damage} damage!")
                
        elif attack_choice == "3":
            self.hp += 15
            if self.hp > 100:
                self.hp = 100
                print(f"{self.name} healed! HP is now {self.hp}")
            return 0
            
        elif attack_choice == "4":
            if self.special_cooldown > 0:
                print(f"Special move not ready!{self.special_cooldown} turns left.")
                return 0
            else:
                damage = random.randint(25, 45)
                print(f"{self.name} uses their special move for  {damage} damage!")
                self.special_cooldown = 3
            return damage
                
        if self.special_cooldown > 0:
            self.special_cooldown -= 1

        if attack_choice == "1":
            self.attack_min -= 2
            self.attack_max -= 4
        elif attack_choice == "2":
            self.attack_min -= 1
            self.attack_max -= 3
        elif attack_choice == "4":
            self.attack_min -= 20
            self.attack_max -= 20
            
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
        exit()

    
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
player = Player(name, 100, 5, 15, 1, 0, 20)
enemy = Enemy(final_enemy_name, 100, 5, 15)
print(f"\nA wild {enemy.name} appears!")


round_num = 1


while not player.is_dead():
    print(f"\n🔥ROUND {round_num} Begins!🔥")
    
    enemy = Enemy(random.choice(enemy_names), 100, 5, 15)


    print(f"A wild {enemy.name} appears!")
    while not enemy.is_dead() and not player.is_dead():
        player_damage = player.attack()
        enemy.take_damage(player_damage)

        if enemy.is_dead():
            print(f"\n💀 You defeated the {enemy.name}!")
            xp_gain = random.randint(20, 40)
            player.gain_xp(xp_gain)
            break

        enemy_damage = enemy.attack()
        player.take_damage(enemy_damage)
    print(f"\nYour HP: {player.hp}")
    print(f"\nEnemy HP: {enemy.hp}")
    if player.is_dead():
        print("Game over!")
        break
    print(f"\n✅ ROUND {round_num} COMPLETE!")
    player.heal_full()
    print("Prepear for next enemy...\n")
    round_num += 1