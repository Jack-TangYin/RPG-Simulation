def battle(player, enemy):
    """
    Simulates a battle between a player and an enemy.
    """
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print("\n=== Battle ===")
        player.display_status()
        enemy.display_status()

        action = input("Choose your action: (1) Attack (2) Use Item (3) Special Ability: ")
        if action == "1":
            player.attack(enemy)
        elif action == "2":
            item_name = input("Enter the item name to use: ")
            player.use_item(item_name)
        elif action == "3":
            player.use_special(enemy)
        else:
            print("Invalid action!")

        if enemy.is_alive():
            enemy.attack(player)

    if player.is_alive():
        print(f"{enemy.name} is defeated!")
    else:
        print(f"{player.name} has been defeated!")
