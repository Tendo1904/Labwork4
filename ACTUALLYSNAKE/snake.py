import pygame


class Snake:
    """
    Represents a snake that can move, consume food, and interact with barriers in a game environment.

    This class manages the snake's movement, growth, scoring, and rendering within the game.

    Attributes:
        score: The current score of the snake.
        head: The current position of the snake's head.
        body: The current segments of the snake's body.

    Methods:
        __init__
        moove
        animation
        draw_snake
        check_end_window
        eat
        check_barrier
        count_score

    The methods in this class handle a variety of functionalities:
    - `__init__`: Initializes the snake with a score, head position, and body segments.
    - `moove`: Updates the head position based on the specified control direction.
    - `animation`: Moves the snake forward and adjusts the body segments accordingly.
    - `draw_snake`: Renders the snake on a specified window.
    - `check_end_window`: Adjusts the snake's head position when it reaches the edge of the level.
    - `eat`: Manages the logic for the snake consuming food and updating its body and score.
    - `check_barrier`: Detects collisions with barriers and updates the game state.
    - `count_score`: Updates the score based on interactions with food and barriers.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.

            This method sets up the initial state of the object by initializing
            the score to zero, head position to coordinates [45, 45],
            and body to a list of segments containing initial positions.

            Attributes:
                score: The current score of the instance.
                head: The current position of the head represented as a list of coordinates.
                body: The current segments of the body represented as a list of coordinates.

            Returns:
                None
        """
        self.score = 0
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def moove(self, control):
        """
        Updates the position of the object based on the control direction.

            The method modifies the head position of the object by moving it
            in the direction specified by the control's flag_direction attribute.
            The movement is done in increments of 11 units.

            Args:
                control: An object that contains the flag_direction attribute,
                         which determines the direction of movement (e.g., "RIGHT",
                         "LEFT", "DOWN", "UP").

            Returns:
                None: This method does not return a value.
        """
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        if control.flag_direction == "LEFT":
            self.head[0] -= 11
        if control.flag_direction == "DOWN":
            self.head[1] += 11
        if control.flag_direction == "UP":
            self.head[1] -= 11

    def animation(self):
        """
        Update the position of the animation by moving the head forward and the tail backward.

            This method modifies the current state of the animation by inserting the current position of the
            head at the beginning of the body list and removing the last position from the body list,
            effectively simulating forward movement.

            Parameters:
                None

            Returns:
                None
        """
        # Head ahead and tail gets back
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        """
        Draws the snake on the specified window.

            This method iterates through the segments of the snake's body
            and draws each segment as a rectangle on the provided window.

            Args:
                window: The window surface on which to draw the snake.

            Returns:
                None
        """
        for segment in self.body:
            pygame.draw.rect(
                window, (0, 209, 3), pygame.Rect(segment[0], segment[1], 10, 10)
            )

    def check_end_window(self):
        """
        Checks if the snake has reached the edge of the level and adjusts its position accordingly.

            This method adjusts the snake's head position if it reaches any of the specified edges of the level.
            The positions are represented in a coordinate system, and the method wraps the snake's head to the
            opposite edge of the level when the boundaries are crossed.

            Parameters:
                None

            Returns:
                None
        """
        # Checking if snake reached the level`s edge
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, gui):
        """
        Handles the actions of the snake eating food.

            When the snake's head position matches the position of the food,
            it appends the food position to the snake's body and updates the
            food's position. It also updates the graphical user interface
            to reflect the change.

            Args:
                food: An object representing the food, which includes methods
                      for retrieving the food's position.
                gui: An object representing the graphical user interface,
                     which is updated to reflect new food indicators.

            Returns:
                None
        """
        # Snake eating
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui)
            gui.get_new_indicator()

    def check_barrier(self, gui):
        """
        Check for collisions with barriers and update the game state accordingly.

            This method checks if the current head position of the object intersects with
            any barriers. If a collision is detected with a barrier, the tail of the object
            is removed, and the indicator is updated. The method also checks if the head
            position intersects with the body of the object itself, and if so, performs
            the same actions.

            Args:
                gui: An instance of the GUI class, which contains the current game state
                     including barriers and indicators.

            Returns:
                None
        """
        # Be careful with barriers!
        if self.head in gui.barrier:
            self.body.pop()
            gui.indicator.pop()
            # print(len(gui.indicator))
            # print(gui.game)

        if self.head in self.body[1:]:
            self.body.pop()
            gui.indicator.pop()
            # print(len(gui.indicator))
            # print(gui.game)

    def count_score(self, food, gui):
        """
        Update the score based on the current game state.

            This method checks if the head of the player intersects with the food
            position or any barriers. If the player eats the food, the score is
            increased by 10; if the player hits a barrier or itself, the score is
            decreased by 10.

            Args:
                food: An object representing the food, which contains the position
                      of the food on the game grid.
                gui: An object containing information about the game interface,
                     including the positions of barriers.

            Returns:
                None
        """
        if self.head == food.food_position:
            self.score += 10
        elif self.head in gui.barrier or self.head in self.body[1:]:
            self.score -= 10
