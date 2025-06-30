import pygame
import random


class Food:
    """
    This class represents a food item in a game, managing its position and rendering it on the screen.

    Attributes:
        food_position: A list that stores positions related to food.

    Methods:
    - __init__
    - get_food_position
    - draw_food

    """

    def __init__(self):
        """
        Sets up the initial state of the Food object, including an empty list to track food positions.

        This constructor sets up the initial state of the object by creating an empty list
        to hold the food positions.

        Attributes:
            food_position: A list that will store positions related to food.

        Returns:
            None
        """

        self.food_position = []

    def get_food_position(self, gui):
        """
        Determines a random location for the food item within the specified game area.

        Args:
            gui: The graphical user interface object containing the game field.

        Returns:
            None
        """

        # For getting random position for food
        self.food_position = random.choice(gui.field)

    def draw_food(self, window):
        """
        Renders a visual representation of food at its current position on the specified window.

        This method renders a rectangular piece of food at the specified food position in the color yellow.

        Args:
            window: The surface on which to draw the food.

        Returns:
            None
        """

        # Draws food
        pygame.draw.rect(
            window,
            pygame.Color("Yellow"),
            pygame.Rect(self.food_position[0], self.food_position[1], 10, 10),
        )
