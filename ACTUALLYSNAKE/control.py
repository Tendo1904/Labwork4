import pygame
from pygame.locals import *


class Control:
    """
    Manages the game state and user control events.

    This class is responsible for initializing and managing the game state,
    including active game status, movement direction, and pause functionality.
    It processes user input to control the game based on events from the
    pygame library.

    Methods:
        __init__
        control

    Attributes:
        flag_game
        flag_direction
        flag_pause

    The __init__ method sets up the initial state of the game by initializing
    several flags indicating if the game is active, the direction of movement,
    and whether the game is paused. The control method processes user input to
    update the game's state based on direction changes and to handle pause or
    quit actions while preventing selection of opposite movement directions.
    """

    def __init__(self):
        """
        Initializes the game state with default flags.

            This constructor method sets up the initial state of the game by
            initializing several flags. The flags indicate whether the game
            is currently active, the direction of movement, and whether the
            game is paused.

            Attributes:
                flag_game: A boolean indicating if the game is currently active.
                flag_direction: A string representing the current direction of movement.
                flag_pause: A boolean indicating whether the game is paused.

            Returns:
                None
        """
        self.flag_game = True
        self.flag_direction = "RIGHT"
        self.flag_pause = True

    def control(self):
        """
        Handle game control events.

            This method processes user input events from the pygame library to control
            the game's state, including direction changes for movement and handling
            game pause and quit actions. It updates the direction of movement based on
            key presses while ensuring that opposite directions cannot be selected.

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
