


class Dinosaur:
    
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        

    
    def attack(self, robot):
        print(f"{self.name} attacks {robot}")
        
        
