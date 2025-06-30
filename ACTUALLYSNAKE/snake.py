import pygame


class Snake:
    """
    Snake class implements the behavior and attributes of a snake in a game environment, managing its movement, collision detection, and score tracking.

    Class Methods:
    - __init__:
    - moove:
    - animation:
    - draw_snake:
    - check_end_window:
    - eat:
    - check_barrier:
    - count_score:

    Attributes:
        score:
        head:
        body:

    The methods handle various functionalities, including movement control, animation updates, drawing on a window, food consumption, collision detection with barriers, and score counting based on game interactions. The attributes represent the current score of the snake, the position of its head, and the segments that make up its body.
    """

    def __init__(self):
        """
        Initializes a new instance of the Snake class, setting the initial score to zero, defining the starting position of the snake's head, and establishing its body with predefined segments.

        Initializes a new instance of the class.

        This constructor sets the initial score to zero and initializes the
        position of the head and body of the object.

        Attributes:
            score: An integer representing the current score.
            head: A list representing the coordinates of the head's position.
            body: A list of lists representing the coordinates of the body segments.
        """

        self.score = 0
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def moove(self, control):
        """
        Updates the position of the object's head based on the specified control direction.

        The method updates the object's head position by adjusting its coordinates
        according to the direction indicated by the control parameters. The movement
        is performed in increments of 11 units.

        Args:
            control: An object that contains direction flags to determine the movement
                     direction (RIGHT, LEFT, DOWN, UP).

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
        Moves the head of the object forward by adding its current position to the front of the body and removes the last segment, simulating movement.

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
        Renders each segment of the snake on the given window, visually representing its current position.

        Args:
            window: The window surface where the snake segments will be drawn.

        Returns:
            None
        """

        for segment in self.body:
            pygame.draw.rect(
                window, (0, 209, 3), pygame.Rect(segment[0], segment[1], 10, 10)
            )

    def check_end_window(self):
        """
        Handles the position of the snake's head, ensuring it seamlessly transitions from one edge of the level to the opposite edge.

        This method modifies the position of the snake's head based on its current coordinates. If the snake reaches one of the defined edges of the level, it will be repositioned to the opposite edge.

        Returns:
            None: This method does not return a value.
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
        Handles the snake consuming food when its head aligns with the food's coordinates, subsequently updating the snake's body and repositioning the food indicator in the GUI.

        This method checks if the snake's head is on the same position as the food. If it is, the food's position is added to the snake's body, the food's position is updated, and a new indicator is obtained from the GUI.

        Args:
            food: The food object providing the current food position and a method to update it.
            gui: The GUI object to manage user interface updates, including the food indicator.

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
        Evaluates the presence of obstacles and self-collisions during gameplay, adjusting the game's state accordingly.

        This method examines the current position of the game entity's head.
        If the head is located at a barrier position, it removes the last element
        from the entity's body and the indicator from the GUI.
        Additionally, if the head occupies a position that is already part
        of the entity's body (excluding the head), the same removal occurs.

        Args:
            gui: The graphical user interface object that manages the game state,
                 including barrier positions and indicators.

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
        Updates the current score based on the snake's head position, rewarding points for consuming food and penalizing for collisions with barriers or its own body.

        This method updates the score by adding points when the head of the entity coincides with the food's position,
        and subtracting points if the head collides with a barrier or the body of the entity itself.

        Args:
            food: The food object that contains the position of the food.
            gui: The graphical user interface object that contains barrier information.

        Returns:
            None
        """

        if self.head == food.food_position:
            self.score += 10
        elif self.head in gui.barrier or self.head in self.body[1:]:
            self.score -= 10
