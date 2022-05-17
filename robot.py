from weapon import Weapon

class Robot:

    def __init__(self, health, name):
        self.name = "Togra"
        self.health = 100
        active_weapon = Weapon("Togra", 25)

    
    def attack(self, dinosaur):
        pass