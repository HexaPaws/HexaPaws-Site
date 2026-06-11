import random
import json

class Character:
    def __init__(self, name, hp, atk_min, atk_max):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk_min = atk_min
        self.atk_max = atk_max

    def attack(self):
        dmg = random.randint(self.atk_min, self.atk_max)
        print(f"{self.name} hits for {dmg}")
        return dmg

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def is_dead(self):
        return self.hp <= 0

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 5, 15)
        self.level = 1
        self.xp = 0
        self.xp_to_next = 50
        self.special_cd = 0

    def heal(self):
        self.hp = min(self.max_hp, self.hp + 15)
        print("Healed +15 HP")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"+{amount} XP")

        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.atk_min += 2
        self.atk_max += 3
        self.xp_to_next = int(self.xp_to_next * 1.4)

        print(f"LEVEL UP → {self.level}!")
SAVE_FILE = "save.json"

def save_game(player):
    data = {
        "name": player.name,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "level": player.level,
        "xp": player.xp,
        "xp_to_next": player.xp_to_next,
        "atk_min": player.atk_min,
        "atk_max": player.atk_max
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

    print("💾 Saved!")

def load_game():
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    p = Player(data["name"])
    p.hp = data["hp"]
    p.max_hp = data["max_hp"]
    p.level = data["level"]
    p.xp = data["xp"]
    p.xp_to_next = data["xp_to_next"]
    p.atk_min = data["atk_min"]
    p.atk_max = data["atk_max"]

    print("📂 Loaded!")
    return p
enemy_names = ["Zombie", "Skeleton", "Monster", "Hacker"]

def spawn_enemy(player):
    return Character(
        random.choice(enemy_names),
        100 + player.level * 10,
        5 + player.level,
        15 + player.level
    )


def battle(player, enemy):
    print(f"\n⚔️ {enemy.name} appears!")

    while not player.is_dead() and not enemy.is_dead():

        choice = input("\n1 Attack  2 Heal  3 Save\n> ")

        if choice == "1":
            enemy.take_damage(player.attack())

        elif choice == "2":
            player.heal()

        elif choice == "3":
            save_game(player)
            continue

        if enemy.is_dead():
            print("Enemy defeated!")
            player.gain_xp(random.randint(20, 40))
            break

        player.take_damage(enemy.attack())

        if player.is_dead():
            print("Game Over 💀")
            break

choice = input("1 New Game  2 Load Game\n> ")

player = load_game() if choice == "2" else Player(input("Name: "))

round_num = 1

while not player.is_dead():
    print(f"\n🔥 ROUND {round_num}")
    enemy = spawn_enemy(player)

    battle(player, enemy)

    if player.is_dead():
        break

    player.hp = player.max_hp
    print("❤️ Fully healed between rounds!")

    round_num += 1