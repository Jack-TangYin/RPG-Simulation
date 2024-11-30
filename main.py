from models.character import Warrior, Mage, Rogue, Enemy
from models.item import Item, Equipment
from models.quest import Quest
from utilities.battle import battle

def main():
    """
    Main function to run the RPG game simulation.
    """
    # Create a player (choose class)
    print("Choose your class: 1. Warrior  2. Mage  3. Rogue")
    choice = input("Enter your choice: ")
    if choice == "1":
        player = Warrior("Hero", 120, 20)
    elif choice == "2":
        player = Mage("Hero", 100, 25)
    elif choice == "3":
        player = Rogue("Hero", 110, 15)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player = Warrior("Hero", 120, 20)

    # Create items and equipment
    potion = Item("Health Potion", "heal")
    sword = Equipment("Steel Sword", "attack", 10)
    player.add_item(potion)
    player.add_item(sword)

    # Assign a quest
    goblin_quest = Quest("Defeat Goblins", "Defeat 3 Goblins to save the village.")
    player.add_quest(goblin_quest)

    # Create enemies
    goblins = [Enemy("Goblin", 50, 10) for _ in range(3)]

    # Start battles
    for goblin in goblins:
        battle(player, goblin)
        if not player.is_alive():
            print("Game Over!")
            return

    # Check quest completion
    goblin_quest.complete(player)

    print("Congratulations! You've completed the game!")

if __name__ == "__main__":
    main()
