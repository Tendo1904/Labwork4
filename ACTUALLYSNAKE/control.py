import pygame
from pygame.locals import *

class Control:
    """
    Control class to manage game controls and settings.
    
        Class Methods:
        - __init__:
    """

    def __init__(self):
        """
        Initialize the game flags and direction settings.
        
        Args:
        - self: the instance of the class
        
        Initializes the following class fields:
        - flag_game: a boolean indicating whether the game is in progress
        - flag_direction: a string representing the current direction of movement
        - flag_pause: a boolean indicating whether the game is paused
        
        Return:
        - None
        """
        self.flag_game = True
        self.flag_direction = "RIGHT"
        self.flag_pause = True

    def control(self):
        """
        Controls the game based on user input events and updates the game state accordingly.
        
        Args:
            self: The object instance representing the game state.
        
        Returns:
            None
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.flag_game = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.flag_direction != "LEFT":
                    self.flag_direction = "RIGHT"
                elif event.key == K_LEFT and self.flag_direction != "RIGHT":
                    self.flag_direction = "LEFT"
                elif event.key == K_DOWN and self.flag_direction != "UP":
                    self.flag_direction = "DOWN"
                elif event.key == K_UP and self.flag_direction != "DOWN":
                    self.flag_direction = "UP"
                elif event.key == K_x:
                    self.flag_game = False
                elif event.key == K_RETURN:
                    if self.flag_pause:
                        self.flag_pause = False
                    elif self.flag_pause == False:
                        self.flag_pause = True
