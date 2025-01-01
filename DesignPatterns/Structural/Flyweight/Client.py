from Robot import IRobot, RobotType
from Robot.impl import HumanoidRobot, RoboticDog
from Graphic import Graphic
from RoboticFactory import RoboticFactory

class Client:

    robot_factory = RoboticFactory()

    robot1 = robot_factory.create_robot(RobotType.HUMANOID)
    robot1.display(1, 2)

    robot2 = robot_factory.create_robot(RobotType.ROBOTIC_DOG)
    robot2.display(4, 5)

    robot3 = robot_factory.create_robot(RobotType.HUMANOID)
    robot3.display(7, 9)
