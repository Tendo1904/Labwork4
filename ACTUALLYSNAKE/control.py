import pygame
from pygame.locals import *


class Control:
    """
    Control manages the game state and user interactions for a simple game application.

    Attributes:
    - flag_game: Indicates if the game is currently active.
    - flag_direction: Defines the current direction of movement.
    - flag_pause: States whether the game is paused or not.

    Methods:
    - __init__
    - control

    The attributes help maintain and control the flow of the game, such as whether it's active, what direction to move in, and if it should be paused. The methods define the behavior for initializing the game and processing user input.
    """

    def __init__(self):
        """
        Sets up the initial configuration for the control settings, including game status, direction, and pause state.

        This constructor method initializes several flags that control the game's behavior.
        - `flag_game` is set to True, indicating that the game is active.
        - `flag_direction` is set to "RIGHT", establishing the initial direction of movement.
        - `flag_pause` is set to True, indicating that the game starts in a paused state.

        Returns:
            None: This constructor does not return any value.
        """

        self.flag_game = True
        self.flag_direction = "RIGHT"
        self.flag_pause = True

    def control(self):
        """
        Processes user input events to manage game state and update movement direction.

        This method processes incoming events from the pygame event queue. It allows the user to change the direction of the game character based on key presses, pause or resume the game, and quit the game.

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
