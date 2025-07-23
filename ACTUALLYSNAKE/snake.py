import pygame
class Snake():
    """
    Class representing a Snake object in a snake game.
    
        Class Methods:
        - __init__: 
        Initialize the Snake object with a starting configuration.
    
        Parameters:
        - self: The instance itself.
    
        Fields initialized:
        - self.score
        - self.head
        - self.body
    
        Returns:
        None
    """

    def __init__(self):
        """
        Initialize the Snake object with a starting configuration.
                
                Parameters:
                - self: The instance itself.
                
                Fields initialized:
                - self.score (int): The score of the Snake object initialized to 0.
                - self.head (list): The head position of the Snake object initialized to [45, 45].
                - self.body (list): The body positions of the Snake object initialized to [[45, 45], [34, 45], [23, 45]].
        """
        self.score = 0
        self.head = [45,45]
        self.body = [[45,45],[34,45],[23,45]]
    def moove(self,control):
        """
        Move the head position of the Snake object based on the direction specified in the control object.
        
        Args:
        self: The current Snake object instance.
        control: An object containing the direction flag.
        
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
        Inserts the head of the body list at index 0 and removes the last element from the body list.
                
            Parameters:
            - self: The instance of the class.
                
            Returns: None
        """
        #Head ahead and tail gets back
        self.body.insert(0,list(self.head))
        self.body.pop()

    def draw_snake(self,window):
        """
        Triple-quotes
                Draws the snake on the given Pygame window.
                
                Parameters:
                    - self: instance of the class
                    - window: Pygame window to draw the snake on
                
                Returns:
                    None
        """
        for segment in self.body:
            pygame.draw.rect(window, (0, 209, 3), pygame.Rect(segment[0], segment[1], 10, 10))

    def check_end_window(self):
        """
        Checks and updates the values of self.head based on specific conditions.
        
        Args:
            self: The object instance.
        
        Returns:
            None
        """
        #Checking if snake reached the level`s edge
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34


    def eat(self,food,gui):
        """
        Summary: Adds the food to the snake's body if the head of the snake reaches the current food position, updates the GUI indicator, and generates a new food position for the snake to consume.
        
        Parameters:
        - self: The instance of the Snake class.
        - food: An instance of the Food class representing the current food.
        - gui: An instance of the GUI class to interact with the graphical user interface.
        
        Args:
        - self: The instance of the Snake class.
        - food: An instance of the Food class representing the current food.
        - gui: An instance of the GUI class to interact with the graphical user interface.
        
        Return: None. Modifies the Snake's body, gets a new food position, and updates the GUI indicator.
        """
        #Snake eating
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui)
            gui.get_new_indicator()

    def check_barrier(self,gui):
        """
        Check for collision with barriers and update game state.
        
        Parameters:
            self: The object instance to operate on.
            gui: The game GUI instance containing barrier and game state information.
        
        Args:
            self (Snake): An instance of the Snake class to check collision for.
            gui (GUI): An instance of the game GUI containing barrier and game state information.
        
        Returns:
            None.
        """
        #Be careful with barriers!
        if self.head in gui.barrier:
            self.body.pop()
            gui.indicator.pop()
            #print(len(gui.indicator))
            #print(gui.game)

        if self.head in self.body[1:]:
            self.body.pop()
            gui.indicator.pop()
            #print(len(gui.indicator))
            #print(gui.game)
    def count_score(self,food,gui):
        """
        Counts the score based on the position of the snake's head in relation to the food and barriers.
        
        Args:
        - self: the instance of the Snake class
        - food: the food object representing the food position
        - gui: the Graphical User Interface (GUI) object for displaying the game visuals
        
        Returns:
        None
        
        WHY: The method calculates the score for the Snake game based on the position of the snake's head compared to the food and any barriers on the game board.
        """
        if self.head == food.food_position:
            self.score += 10
        elif self.head in gui.barrier or self.head in self.body[1:]:
            self.score -= 10
