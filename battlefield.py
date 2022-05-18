from robot import Robot
from dinosaur import Dinosaur


class Battlefield:


    def __init__(self):
        self.dinosaur = Dinosaur("Ghangas Rex", 25, 100)
        self.robot = Robot(100, "T1000 + 1")
        pass


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        pass


    
    def display_welcome(self):
        print("Here is a test")
        pass


    def battle_phase(self):
        robot_health = self.robot.health
        dinosaur_health = self.dinosaur.health

        self.dinosaur.attack(self.robot.name)
        robot_health -= self.dinosaur.attack_power
        print(f"{self.robot.name} has {robot_health} remaining!")

        self.robot.attack(self.dinosaur.name)
        dinosaur_health -= self.robot.active_weapon.attack_power
        print(f"{self.dinosaur.name} has {dinosaur_health} remaining!")
        #dinosaur_health -= self.robot
        

        pass

    
    def display_winner(self):
        pass