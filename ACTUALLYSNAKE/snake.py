import pygame


class Snake:
    """
    A class representing a snake in a grid-based game.

    This class handles the functionality of a snake, including
    movement, eating food, collision detection, and score management.

    Methods:
        __init__
        moove
        animation
        draw_snake
        check_end_window
        eat
        check_barrier
        count_score

    Attributes:
        score: An integer representing the current score of the snake.
        head: A list representing the current coordinates of the snake's head.
        body: A list of lists representing the coordinates of the segments of the snake's body.

    The methods allow the snake to move, animate its motion, draw its segments on a window,
    handle edge wrapping, consume food, check for collisions with barriers, and update the score
    based on gameplay events.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.

            This method sets up the initial state of the instance by initializing
            the score, head position, and body segments.

            Attributes:
                score: An integer representing the initial score of the instance.
                head: A list representing the initial coordinates of the head position.
                body: A list of lists representing the initial coordinates of the body segments.

            Returns:
                None
        """
        self.score = 0
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def moove(self, control):
        """
        Updates the position of the head attribute based on the control direction.

            The method modifies the head's coordinates by adjusting the x or y values
            depending on the direction indicated by the control flag.

            Args:
                control: An object containing direction flags which indicate
                         whether to move the head "RIGHT", "LEFT", "DOWN", or "UP".

            Returns:
                None
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
        Update the animation by moving the head forward and removing the tail.

            This method modifies the position of the animated object by inserting
            the current position of the head at the beginning of the body list
            and removing the last element of the body list to create the effect
            of movement.

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

            This method iterates over the segments of the snake's body and draws each segment as a rectangle
            on the provided window using Pygame.

            Args:
                window: The Pygame window surface where the snake will be drawn.

            Returns:
                None
        """
        for segment in self.body:
            pygame.draw.rect(
                window, (0, 209, 3), pygame.Rect(segment[0], segment[1], 10, 10)
            )

    def check_end_window(self):
        """
        Check and wrap the snake's position when it reaches the level's edge.

            This method modifies the snake's head position if it has reached
            any of the predefined edges of the level. When the snake's head
            reaches the right edge (419), it wraps around to the left edge
            (23). Similarly, when it reaches the left edge (12), it wraps
            around to the right edge (419). The top and bottom edges are also
            handled, with the top edge (23) wrapping to the bottom edge (419)
            and the bottom edge (419) wrapping to a position (34).

            Attributes:
                head: A list representing the current position of the snake's head.

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
        Process the action of the snake eating food.

            If the serpent's head coincides with the position of the food,
            it consumes the food, adds the food position to its body, and
            triggers updates on the food position and game indicator.

            Args:
                food: An object representing the food, which includes the
                    attribute food_position and a method to regenerate its
                    position.
                gui: An object managing the graphical user interface, which
                    provides the method to update indicators.

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
        Check for collisions with barriers and handle them accordingly.

        This method checks if the current position of the object's head is
        within any barriers defined in the GUI. If a collision is detected,
        it removes the last segment of the object's body and updates the
        indicator.

        Args:
            gui: The graphical user interface object containing barrier
                 definitions and methods to manage the indicator.

        Returns:
            None: This method does not return a value, but it modifies
                  the object's body and the gui's indicator when a
                  collision occurs.
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
        Calculate and update the score based on the current game state.

            This method checks the position of the game entity (head) against the food position
            and barriers. If the head is on the food position, the score is increased by 10.
            If the head collides with a barrier or a part of the body, the score is decreased by 10.

            Args:
                food: An object representing the food, which contains its position.
                gui: An object representing the graphical user interface, which contains barriers.

            Returns:
                None
        """
        if self.head == food.food_position:
            self.score += 10
        elif self.head in gui.barrier or self.head in self.body[1:]:
            self.score -= 10
