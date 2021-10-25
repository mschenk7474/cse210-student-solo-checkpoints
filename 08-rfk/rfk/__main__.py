import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.artifact import Artifact
from game.robot import Robot

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    marquee = Actor()
    marquee.set_text("")
    marquee.set_position(Point(1, 0))
    cast["marquee"] = [marquee]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    robot = Robot()
    robot.set_text("#")
    robot.set_position(position)
    cast["robot"] = [robot]

    artifacts = []
    for n in range(constants.ARTIFACTS):
        text = chr(random.randint(33, 126))
        description = constants.MESSAGES[n]
        
        x = random.randint(0, constants.MAX_X - 1)
        y = random.randint(1, constants.MAX_Y - 1)
        position = Point(x, y)

        artifact = Artifact()
        artifact.set_description(description)
        artifact.set_text(text)
        artifact.set_position(position)
        artifacts.append(artifact)
    cast["artifact"] = artifacts

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()

    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    output_service.open_window("Robot Finds Kitten");
    director = Director(cast, script)
    director.start_game()

if __name__ == "__main__":
    main()
