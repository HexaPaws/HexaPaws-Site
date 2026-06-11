import random

global hp
global enemy_hp

hp = 100
enemy_hp = 100


def take_damage():
    global hp
    global enemy_hp
    b = random.randint(0, 20)
    print(f"The {target} attacked you with {b}!")
    hp -= b
    attack()
    if hp <= 0:
        print("Game Over!")
        exit()

def pick_enemy():
    global target
    enemies = ["Zombie", "Skelekton", "Hacker"]
    target = random.choice(enemies)
    print(f"Enemy: {target}")

def attack():
    global hp
    global enemy_hp

    print(f"Your Health: {hp}")
    print("Which attack would you like to use?")

    v = input("1. Punch, 2. Laser")
    w = int(v)

    if w in range(0, 3):
        if w == 1:
            a = random.randint(0, 10)
            print(f"Attacked {target} with {a} damage!")
            enemy_hp -= a
            print(f"Enemy HP: {enemy_hp}")
            if enemy_hp <= 0:
                print(f"The {target} died. You win!")
                exit()
            else:
                take_damage()
        if w == 2:
            a = random.randint(0, 30)
            print(f"Attacked {target} with {a} damage!")
            enemy_hp -= a
            print(f"Enemy HP: {enemy_hp}")
            if enemy_hp <= 0:
                print(f"The {target} died. You win!")
                exit()
            else:
                take_damage()
                
avatar = input("Pick from a human, a cat or cybercat. 1, 2 or 3.")
avatar = int(avatar)
username = input("Create a Username")

if avatar not in range(1, 4):
    print(avatar)
else:
    if avatar == 1:
        print(f"Let's fight the enemy, {username} the warrior!")
        pick_enemy()
        attack()

    if avatar == 2:
        print(f"Let's fight the enemy, {username} the cat!")
        pick_enemy()
        attack()

    if avatar == 3:
        print(f"Let's fight the enemy, {username} the cybercat!")
        pick_enemy()
        attack()