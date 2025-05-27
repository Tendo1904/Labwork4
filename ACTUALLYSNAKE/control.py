import pygame
from pygame.locals import *


class Control:
    """
    Manages the state and behavior of the game.

    This class is responsible for initializing the game with default settings
    and handling user input to update the game's state based on events. It
    allows for control over the game's direction and pause functionality.

    Methods:
        __init__
        control

    Attributes:
        flag_game
        flag_direction
        flag_pause

    - __init__: Initializes the game with default settings, setting up the
      initial state of the game and defining several flags that control the
      game's behavior.
    - control: Handles user input and updates the game state based on events,
      modifying flags that track the game's direction and whether it is paused
      or running.
    """

    def __init__(self):
        """
        Initializes the game with default settings.

            This method sets up the initial state of the game by defining
            several flags that control the game's behavior.

            Attributes:
                flag_game: A boolean indicating if the game is currently active.
                flag_direction: A string representing the current movement direction of the game.
                flag_pause: A boolean indicating if the game is currently paused.

            Returns:
                None
        """
        self.flag_game = True
        self.flag_direction = "RIGHT"
        self.flag_pause = True

    def control(self):
        """
        Handles user input and updates game state based on events.

            This method processes keyboard and quit events to control the
            game's state, including direction changes and pause functionality.
            It modifies the internal flags that track the game's direction and
            whether the game is paused or running.

            Parameters:
                None

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
