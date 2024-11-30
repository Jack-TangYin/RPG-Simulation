class Item:
    """
    Represents a consumable item.
    """
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, character):
        if self.effect == "heal":
            character.health += 20
            print(f"{character.name} uses {self.name} and heals 20 health!")


class Equipment(Item):
    """
    Represents equipment like weapons or armor.
    """
    def __init__(self, name, effect, power):
        super().__init__(name, effect)
        self.power = power

    def use(self, character):
        if self.effect == "attack":
            character.attack_power += self.power
            print(f"{character.name} equips {self.name} and gains {self.power} attack power!")
