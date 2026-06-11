    def save_game(name, hp, attack_min ,attack_max, level, xp, xp_to_next):
        with open("save.txt", "a") as f:
            f.write(Player.name)
            f.write(Player.hp)
            f.write(Player.attack_min)
            f.write(Player.attack_max)
            f.write(Player.level)
            f.write(Player.xp)
            f.write(Player.xp_to_next)
        print("Game Saved :D")
# save game method in Player class





    save_choice = input("Do you want to save progress? Y/N")
    if save_choice == "Y":

# in main game loop

# need to add some upgrades to enemies as well :)