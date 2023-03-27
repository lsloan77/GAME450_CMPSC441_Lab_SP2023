import random

class PyGameAIPlayer:
    def __init__(self):
        pass

class PyGameAICombatPlayer(PyGameAIPlayer):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 100
        self.weapon = None

    def weapon_selecting_strategy(self):
        weapons = ["Sword", "Arrow", "Fire"]
        self.weapon = random.choice(weapons)
        return self.weapon

    def attack(self, target):
        damage = random.randint(10, 30)
        target.health -= damage
        return damage

