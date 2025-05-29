import pygame
import random


class Food:
    """
    Represents a food item that can be displayed in a GUI environment.

    This class manages the position of food items and provides methods
    to retrieve and draw food in a graphical interface.

    Methods:
        __init__
        get_food_position
        draw_food

    Attributes:
        food_position: A list that will store the positions of food items.

    The __init__ method initializes a new instance of the class by
    setting up an empty list for food positions. The get_food_position
    method randomly selects a position for the food in the provided
    GUI field, while the draw_food method draws the food at that
    position on the specified window.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.

            This method sets up the initial state of the instance by defining
            an empty list to hold the position of food items.

            Attributes:
                food_position: A list that will store the positions of food items.
        """

        self.food_position = []

    def get_food_position(self, gui):
        """
        Get a random position for food in the GUI field.

            This method selects a random position from the available field in the provided GUI
            object and assigns it to the food_position attribute of the current instance.

            Args:
                gui: The GUI object containing the field from which to select the food position.

            Returns:
                None
        """
        # For getting random position for food
        self.food_position = random.choice(gui.field)

    def draw_food(self, window):
        """
        Draws food on the given window.

            This method draws a yellow rectangle representing food at the specified
            position on the provided window using Pygame's drawing functions.

            Args:
                window: The window surface on which the food will be drawn.

            Returns:
                None
        """
        # Draws food
        pygame.draw.rect(
            window,
            pygame.Color("Yellow"),
            pygame.Rect(self.food_position[0], self.food_position[1], 10, 10),
        )
