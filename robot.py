from weapon import Weapon


class Robot:

    def __init__(self, health, name):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Taser Beam's Taser!", 25)

    
    def attack(self, dinosaur):
        print(f"{self.name} attacks {dinosaur} with {self.active_weapon.name}")

        pass