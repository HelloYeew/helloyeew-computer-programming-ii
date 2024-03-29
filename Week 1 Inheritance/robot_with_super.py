import random

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health_level = random.random()
        
    def say_hi(self):
        print("Hi, I am " + self.name)

    def needs_a_doctor(self):
        if self.health_level < 0.8:
            return True
        else:
            return False


class PhysicianRobot(Robot):

    def say_hi(self):
        super().say_hi()
        print(self.name + " take care of you!")

    def heal(self, robo):
        robo.health_level = random.uniform(robo.health_level, 1)
        print(robo.name + " has been healed by " + self.name + "!")

doc = PhysicianRobot("Dr. Frankenstein")
doc.say_hi()




# print(x, type(x))
# print(y, type(y))

# x.say_hi()
# print()
# y.say_hi()

# print(isinstance(x, Robot), isinstance(y, Robot))
# print(isinstance(x, PhysicianRobot))
# print(isinstance(y, PhysicianRobot))
# 
# print(type(y) == Robot, type(y) == PhysicianRobot)
