class Character:
    """
    Represents a generic character in the RPG game.
    """
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        """
        Attacks another character and reduces their health.
        """
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def is_alive(self):
        """
        Checks if the character is alive.
        """
        return self.health > 0

    def display_status(self):
        """
        Displays the character's health status.
        """
        print(f"{self.name} - Health: {self.health}")


class Player(Character):
    """
    Represents the player character with classes, inventory, and quests.
    """
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.inventory = []
        self.quests = []

    def add_item(self, item):
        """
        Adds an item to the player's inventory.
        """
        self.inventory.append(item)
        print(f"{item.name} added to inventory!")

    def use_item(self, item_name):
        """
        Uses an item from the inventory. Input is case-insensitive.
    
        Args:
        item_name (str): The name of the item to use.
        """
        item_name = item_name.lower()  # Convert input to lowercase
        for item in self.inventory:
            if item.name.lower() == item_name:  # Compare normalized names
                item.use(self)
                self.inventory.remove(item)
                return
        print(f"{item_name} not found in inventory!")


    def add_quest(self, quest):
        """
        Adds a quest to the player's active quests.
        """
        self.quests.append(quest)
        print(f"Quest added: {quest.title}")


class Warrior(Player):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.special_ability = "Berserk"

    def use_special(self, target):
        """
        Warrior's special ability: Deals double damage.
        """
        damage = self.attack_power * 2
        target.health -= damage
        print(f"{self.name} uses Berserk and deals {damage} damage to {target.name}!")


class Mage(Player):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.special_ability = "Fireball"

    def use_special(self, target):
        """
        Mage's special ability: A powerful magic attack.
        """
        damage = self.attack_power + 15
        target.health -= damage
        print(f"{self.name} casts Fireball and deals {damage} damage to {target.name}!")


class Rogue(Player):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.special_ability = "Backstab"

    def use_special(self, target):
        """
        Rogue's special ability: A sneak attack that ignores defense.
        """
        damage = self.attack_power + 10
        target.health -= damage
        print(f"{self.name} performs Backstab and deals {damage} damage to {target.name}!")


class Enemy(Character):
    """
    Represents an enemy character.
    """
    pass
