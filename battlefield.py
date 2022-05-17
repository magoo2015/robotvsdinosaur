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
        print(f"{self.dinosaur.name} attacks {self.robot.name}")
        print(f"Dinosaur health is: {self.dinosaur.health}")

        pass

    
    def display_winner(self):
        pass