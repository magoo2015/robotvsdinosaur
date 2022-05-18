from weapon import Weapon
#from dinosaur import Dinosaur

class Robot:

    def __init__(self, health, name):
        self.name = "Togra"
        self.health = 100
        self.active_weapon = Weapon("Taser Beam's Taser!", 25)

    
    def attack(self, dinosaur):
        print(f"{self.name} attacks {dinosaur} with {self.active_weapon.name}")

        pass