import pygame
import random


class Food:
    """
    Represents a food item in a game environment, handling its position and rendering.

    Methods:
        __init__
        get_food_position
        draw_food

    Attributes:
        food_position: A list that stores the positions of food items.

    The class initializes with an empty list for food positions.
    It provides methods to get a random food position within a GUI field
    and to draw the food on a specific window surface using visual representation.
    """

    def __init__(self):
        """
        Initializes the object and sets up the initial state.

            This method initializes the instance of the class by creating an empty list
            to hold food positions.

            Attributes:
                food_position: A list that will store the positions of food items.

            Returns:
                None
        """

        self.food_position = []

    def get_food_position(self, gui):
        """
        Get a random position for food on the GUI field.

            This method selects a random position from the provided GUI field
            and assigns it to the food_position attribute.

            Args:
                gui: The GUI object containing the field from which to select
                     a random position for food.

            Returns:
                None
        """
        # For getting random position for food
        self.food_position = random.choice(gui.field)

    def draw_food(self, window):
        """
        Draws food on the given window.

            This method renders a yellow rectangle representing food at the
            current food position within the provided window.

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
