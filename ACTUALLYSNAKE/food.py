import pygame
import random


class Food:
    """
    Represents a food item in a game.

        The Food class is responsible for managing the position of food items in a game environment.
        It can place food at random locations within a specified graphical user interface (GUI) field
        and draw the food on a designated game window.

        Methods:
            __init__
            get_food_position
            draw_food

        Attributes:
            food_position: A list that holds the positions of food items.

        The __init__ method initializes the food_position attribute as an empty list.
        The get_food_position method selects a random position for the food within the GUI field.
        The draw_food method renders a representation of the food on the game window.
    """

    def __init__(self):
        """
        Initializes an instance of the class.

            This method sets up the initial state of the object by defining
            the food_position attribute as an empty list.

            Attributes:
                food_position: A list that will hold the positions of food items.
        """

        self.food_position = []

    def get_food_position(self, gui):
        """
        Selects a random position for food within the specified GUI field.

            This method retrieves a random position from the GUI's field attribute
            to place the food in the game.

            Args:
                gui: The graphical user interface object that contains the
                     field attribute from which to choose the food's position.

            Returns:
                None: This method does not return a value; it updates the
                food_position attribute of the instance.
        """
        # For getting random position for food
        self.food_position = random.choice(gui.field)

    def draw_food(self, window):
        """
        Draws food on the given window.

            This method renders a yellow rectangle representing food at the
            specified position within the game window.

            Args:
                window: The surface on which the food will be drawn.

            Returns:
                None
        """
        # Draws food
        pygame.draw.rect(
            window,
            pygame.Color("Yellow"),
            pygame.Rect(self.food_position[0], self.food_position[1], 10, 10),
        )
