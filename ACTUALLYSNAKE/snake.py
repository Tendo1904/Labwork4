import pygame


class Snake:
    """
    Represents a Snake game entity that manages the snake's movement and interactions.

    This class handles the snake's position, movement, and collision detection.
    It allows the snake to grow when it eats food and keeps track of the score.

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
        score
        head
        body

    The methods manage game mechanics including moving the snake in response to controls,
    updating the animation to simulate movement, drawing the snake on the screen, and
    handling interactions with food and barriers. The attributes store the current state,
    including the score and positions of the snake's head and body segments.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.

            This method sets up the initial state of the object by initializing
            the score and the position of the head and body of the object.

            Attributes:
                score: The initial score of the object, set to 0.
                head: The starting position of the head, initialized to
                      coordinates [45, 45].
                body: The initial positions of the body segments,
                      initialized to a list of coordinates [[45, 45],
                      [34, 45], [23, 45]].

            Returns:
                None
        """
        self.score = 0
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def moove(self, control):
        """
        Updates the position of the head based on the control direction.

            This method modifies the position of the head attribute of the object
            depending on the direction indicated in the control parameter. It moves
            the head in increments according to the specified direction.

            Args:
                control: An object containing the flag_direction attribute that indicates
                         the direction of movement ('RIGHT', 'LEFT', 'DOWN', or 'UP').

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

            This method modifies the state of the object's animation by inserting
            the current position of the head at the beginning of the body list and
            removing the last element from the body list, effectively creating the
            appearance of movement.

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
        Draws the snake on the given window.

            This method iterates through the segments of the snake's body
            and draws each segment as a rectangle on the specified window.

            Args:
                window: The surface on which the snake is to be drawn.

            Returns:
                None
        """
        for segment in self.body:
            pygame.draw.rect(
                window, (0, 209, 3), pygame.Rect(segment[0], segment[1], 10, 10)
            )

    def check_end_window(self):
        """
        Check and update the position of the snake when it reaches the edge of the level.

            This method determines if the snake's head has reached any edge of the defined level.
            If it has, the method alters the position of the snake's head to the opposite edge, allowing
            the snake to continue moving within the level boundaries.

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
        Handles the action of the snake eating food.

            This method allows the snake to consume food when its head
            coordinates match the food's position. Upon eating, the food
            position is updated, and the snake's body grows accordingly.

            Args:
                food: The food object that contains the current food position
                      and methods to update its location.
                gui: The graphical user interface object that handles the
                     display and indicators for the game.

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
        Check for barriers and update the game state accordingly.

            This method checks if the current head position of the object
            is within a barrier or if it collides with its own body. If a
            barrier is encountered, the last element of the body and the
            game indicator are removed to reflect the collision.

            Args:
                gui: The GUI object that contains the game state, including
                     the barrier information and an indicator.

            Returns:
                None: This method does not return a value.
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
        Calculate and update the score based on the current position of the head.

            This method checks the position of the head in relation to the food and barriers.
            If the head is in the same position as the food, the score is increased by 10 points.
            If the head collides with a barrier or itself, the score is decreased by 10 points.

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
