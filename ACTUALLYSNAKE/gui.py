import pygame
from snake import Snake
class Gui(Snake):
    """
    Class Gui: 
    
        A class that handles the graphical user interface of a game application.
    
        Class Methods:
        - __init__: 
        Constructs a new instance of the class.
    
        Attributes initialized:
            - level: Represents the game level.
            - gui_image: Represents the GUI image.
            - win: Represents the winning image.
            - lose: Represents the losing image.
            - barrier: Empty list to store barriers.
            - field: Empty list to store field data.
            - indicator: List containing coordinates for an indicator.
            - game: String representing the game name.
    
        - create_image:
        Creates an image based on the level layout and saves it as a PNG file.
    
        - draw_level:
        Draws the level onto the given window.
    
        - init_field:
        Initialize the field and barrier coordinates based on the level configuration.
    
        - get_new_indicator:
        Updates the indicator list with a new value based on the previous value.
    
        - draw_indicator:
        Draws indicators on the given window at the specified coordinates.
    
        - draw_win:
        Draws a window on a specified position on the screen.
    
        - draw_lose:
        Draws the losing screen image onto the window at the specified position.
    
        - check_win_lose:
        Checks the game status based on the length of the 'indicator' list.
    
        - render:
        Renders the current score of the snake game onto the game window.
    """

    def __init__(self):
        """
        Constructs a new instance of the class.
        
        Parameters:
           self: Represents the instance of the class.
        
        Attributes initialized:
            - level: Represents the game level.
            - gui_image: Represents the GUI image.
            - win: Represents the winning image.
            - lose: Represents the losing image.
            - barrier: Empty list to store barriers.
            - field: Empty list to store field data.
            - indicator: List containing coordinates for an indicator.
            - game: String representing the game name.
        
        Args:
            None
        
        Returns:
            None
        """
        self.level = [
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                ]

        self.gui_image = pygame.image.load("images/gui.png")
        self.win = pygame.image.load("images/win.png")
        self.lose = pygame.image.load("images/lose.png")
        self.barrier = []
        self.field = []
        self.indicator = [[12,12]]
        self.game = "GAME"

    def create_image(self):
        """
        Creates an image based on the level layout and saves it as a PNG file.
        
        Args:
            self: The instance of the class.
        
        Returns:
            None
        """
        #creates image on list`s data
        screen = pygame.Surface((441,491),pygame.SRCALPHA,32)
        x = 1
        y = 1
        for i in self.level:
            if i == 0:
                pygame.draw.rect(screen, pygame.Color("Grey"), pygame.Rect(x,y,10,10))
            x += 11
            if x == 441:
                y += 11
                x = 1
        pygame.image.save(screen,"images/gui.png")

    def draw_level(self,window):
        """
        Draws the level onto the given window.
                
                Parameters:
                - self: The instance of the class.
                - window: The window onto which the level will be drawn.
                
                Returns:
                None.
        """
        #Level painting
        window.blit(self.gui_image, (0,0))

    def init_field(self):
        """
        Initialize the field and barrier coordinates based on the level configuration.
        
        Parameters:
        - self: The object instance.
        
        Args:
        - self (object): An instance of the Gui class.
        
        Returns:
        None
        """
        #Fills lists with coordinates
        x = 1
        y = 1
        for i in self.level:
            if i == 0:
                self.barrier.append([x,y])
            elif i == 1 and y != 12:
                self.field.append([x,y])
            x += 11
            if x == 441:
                y += 11
                x = 1

    def get_new_indicator(self):
        """
        Updates the indicator list with a new value based on the previous value.
        
        Parameters:
            self: The current instance of the class.
        
        Returns:
            None
        
        Args:
            None
        
        Returns:
            None
        """
        #The length indicator
        self.indicator.append([self.indicator[-1][0] + 11,12])
        #print(len(self.indicator))

    def draw_indicator(self,window):
        """
        Draws indicators on the given window at the specified coordinates.
        
        Parameters:
        - self: The instance of the class.
        - window: The surface where indicators will be drawn.
        
        Returns:
        None
        
        Args:
        - self: Gui class instance.
        - window: pygame.Surface object where indicators will be drawn.
        
        Return:
        None
        """
        #Indicator`s painting
        for i in self.indicator:
            pygame.draw.rect(window, (0, 209, 3), pygame.Rect(i[0], i[1], 10, 10))

    def draw_win(self,window):
        """
        Draws a window on a specified position on the screen.
                
                Parameters:
                    - self: The instance of the class.
                    - window: The window object to be displayed.
                
                Returns:
                    None
                ``` 
        
        Args:
             self (object): An instance of the Gui class.
             window (object): The window object to be displayed on the screen.
        
        Return:
             None
        
        WHY: The draw_win method is responsible for displaying a window object at a specific position on the screen within the Snake game implementation.
        """
        #Draws winscreen
        window.blit(self.win, (23,100))

    def draw_lose(self,window):
        """
        Draws the losing screen image onto the game window at the specified position.
        
        Args:
            self: The instance of the Gui class.
            window: The pygame surface representing the game window.
        
        Returns:
            None
        """
        #Draws losescreen
        window.blit(self.lose, (23,100))

    def check_win_lose(self):
        """
        Checks the game status based on the length of the 'indicator' list.
                
                Parameters:
                - self: the object instance
                
                If 'indicator' is empty, sets the 'game' property to 'LOSE'.
                If 'indicator' has a length of 37, sets the 'game' property to 'WIN'.
                
                Returns:
                None
        """
        #Checks game status
        if len(self.indicator) == 0:
            self.game = "LOSE"
        elif len(self.indicator) == 37:
            self.game = "WIN"
    def render(self,snake,window):
        """
        Renders the current score of the snake game onto the game window.
        
        Args:
            self: The current instance of the class.
            snake: The snake object containing the game score information.
            window: The game window to render the score display.
        
        Returns:
            None
        
        WHY: The method renders the current score of the snake game onto the game window to provide visual feedback to the player about their current score progress.
        """
        font_score = pygame.font.SysFont('Arial', 26, bold=True)
        render_score = font_score.render(f'SCORE: {snake.score}', 1, pygame.Color('red'), (0,0,255))
        window.blit(render_score, (280, 440))
