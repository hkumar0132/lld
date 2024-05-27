from Robot import IRobot, RobotType
from Robot.impl import HumanoidRobot, RoboticDog
from Graphic import Graphic

from collections import defaultdict

class RoboticFactory:

    def __init__(self) -> None:
        self.cache: dict[str, IRobot] = defaultdict()

    def create_robot(self, robot_type: RobotType) -> IRobot:

        if robot_type.value in self.cache:
            print("hit")
            return self.cache[robot_type.value]

        if robot_type == RobotType.HUMANOID:
            graphic = Graphic(robot_type)
            humanoid_robot = HumanoidRobot(graphic, RobotType.HUMANOID)
            self.cache[robot_type.value] = humanoid_robot
            return humanoid_robot

        elif robot_type == RobotType.ROBOTIC_DOG:
            graphic = Graphic(robot_type)
            robotic_dog = RoboticDog(graphic, RobotType.ROBOTIC_DOG)
            self.cache[robot_type.value] = robotic_dog
            return robotic_dog