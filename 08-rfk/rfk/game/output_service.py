import sys
from game import constants
import raylibpy

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        None
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
        """

    def open_window(self, title):
        """
        Opens a new window with the provided title.
        """
        raylibpy.init_window(constants.MAX_X, constants.MAX_Y, title)
        raylibpy.set_target_fps(constants.FRAME_RATE)
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.begin_drawing()
        raylibpy.clear_background(raylibpy.WHITE)

    def draw_box(self, x, y, width, height):
        """
        Draws at rectangular box with the provided specifications.
        """
        raylibpy.draw_rectangle(x, y, width, height, raylibpy.BLUE)

    def draw_text(self, x, y, text, is_dark_text):
        """
        Outputs the provided text at the desired location.
        """
        color = raylibpy.WHITE

        if is_dark_text:
            color = raylibpy.BLACK

        raylibpy.draw_text(text, x + 5, y + 5, constants.DEFAULT_FONT_SIZE, color)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()

        if text != "":
            self.draw_text(x, y, text, True)
        elif width > 0 and height > 0:
            self.draw_box(x, y, width, height)
        
    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.end_drawing()
