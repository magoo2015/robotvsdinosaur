from robot import Robot
from dinosaur import Dinosaur


class Battlefield:


    def __init__(self):
        self.dinosaur = Dinosaur("Ghangas Rex", 15, 100)
        self.robot = Robot(100, "Togra")
        
        pass


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass


    
    def display_welcome(self):
        print("""
        *********************************************************
        Welcome to the Battle of the Century!  Robot Vs. Dinosaur
        *********************************************************
        """
        )
        pass


    def battle_phase(self):
        

        battle_on = True

        robot_health = self.robot.health
        dinosaur_health = self.dinosaur.health
       

        while battle_on:

            self.dinosaur.attack(self.robot.name)
            robot_health -= self.dinosaur.attack_power
            print(f"{self.robot.name} has {robot_health} remaining!")

            self.robot.attack(self.dinosaur.name)
            dinosaur_health -= self.robot.active_weapon.attack_power
            print(f"{self.dinosaur.name} has {dinosaur_health} remaining!")
            #Feel like this loop could be better.
            if robot_health <= 0:
                print(f"{self.dinosaur.name} has defeated {self.robot.name}!")
                #print(f"{self.dinosaur.name} is the winner!") Commenting out since display winner function now works
                battle_on = False
            elif dinosaur_health <= 0:
                print(f"{self.robot.name} has returned {self.dinosaur.name} to the prehistoric era!")
                #print(f"{self.robot.name} is the winner!")Commenting out since display winner function now works
                battle_on = False
            else:
                battle_on = True
        pass

    
    def display_winner(self):
        if self.robot.health > 0:
            print(f"{self.robot.name} is the winner!")
        elif self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} is the winner!")