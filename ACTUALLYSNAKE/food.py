import pygame
import random

class Food:
    """
    A class representing food items that can be placed on a GUI field.
    
        Class Methods:
        - __init__:
    """

    def __init__(self):
        """
        Initialize the class object.
        
        Args:
        - self: The instance of the class.
        
        Fields Initialized:
        - food_position: An empty list to store the position of food items.
        
        Returns:
        - None
        """

        self.food_position = []

    def get_food_position(self,gui):
        """
        Assigns a random position for the food item on the GUI field.
        
        Parameters:
        - self: The Food instance.
        - gui: The GUI instance where the food will be positioned.
        
        Returns:
        None
        
        Args:
            self (Food): An instance of the Food class.
            gui (GUI): An instance of the GUI class where the food will be positioned.
        
        Return:
            None
        """
        #For getting random position for food
        self.food_position = random.choice(gui.field)

    def draw_food(self,window):
        """
        Draws a yellow rectangle representing the food at the specified position on the given window.
        
        Parameters:
        - self: The instance of the class.
        - window: The Pygame window to draw the food rectangle.
        
        Returns:
        None
        
        Args:
        - self: The instance of the Food class.
        - window (Pygame Surface): The Pygame window object where the food rectangle will be drawn.
        
        Return:
        None
        """
        #Draws food
        pygame.draw.rect(window, pygame.Color("Yellow"), pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))
