import pygame
from pygame.locals import *


class Control:
    """
    Manages the control and state of the game, handling user inputs to update game behavior.

    This class initializes the game with default settings and processes user input events
    to control the game state, direction of movement, and pause functionality.

    Methods:
        __init__()
        control()

    Attributes:
        flag_game: Indicates whether the game is currently active.
        flag_direction: The current direction of movement in the game.
        flag_pause: Indicates whether the game is paused or not.

    The __init__() method sets up the initial state of the game with default flags, while
    the control() method processes user inputs to update the game state, manage movement
    direction, and pause functionality.
    """

    def __init__(self):
        """
        Initializes the game with default settings.

            This method sets up the initial state of the game by defining
            various flags that control the game's behavior. The game is
            started with the flags indicating that the game is active,
            the movement direction is to the right, and the game is paused.

            Attributes:
                flag_game: Indicates whether the game is currently active.
                flag_direction: The initial direction of movement in the game.
                flag_pause: Indicates whether the game is paused or not.

            Returns:
                None
        """
        self.flag_game = True
        self.flag_direction = "RIGHT"
        self.flag_pause = True

    def control(self):
        """
        Handle user input events to control game state and direction.

            This method processes events from the Pygame event queue. It updates the
            game state based on user input. If the quit event is detected, it sets
            the game flag to false, indicating that the game should terminate. The
            method also changes the direction of the game based on arrow key presses
            and manages the pause state with the Enter key.

            Attributes:
                flag_game: Indicates whether the game is running.
                flag_direction: The current direction of the game element.
                flag_pause: Indicates whether the game is paused.

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
