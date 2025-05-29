import pygame


class Music:
    """
    A class to manage and play music tracks using the pygame library.

    This class is designed to load and play music tracks, providing an
    easy way to manage background sound in games or applications.

    Methods:
        __init__
        ambient

    Attributes:
        now_plays

    The __init__ method initializes a new instance and loads a specific
    music track from the compositions directory. The now_plays attribute
    holds the music track that is currently loaded into the mixer. The
    ambient method starts playing ambient music in a loop, creating an
    immersive background sound suitable for various applications.
    """

    def __init__(self):
        """
        Initializes a new instance and loads a music track.

            This method sets up the object by loading a specific music file
            from the compositions directory using the pygame library.

            Attributes:
                now_plays: The music track that is loaded into the mixer.

            Returns:
                None
        """
        self.now_plays = pygame.mixer.music.load("compositions/tracktwo.mp3")

    def ambient(self):
        """
        Start playing ambient music in a loop.

            This method uses the pygame mixer to play music continuously in a loop,
            creating an immersive background sound suitable for games or applications.

            Parameters:
                None

            Returns:
                None
        """
        pygame.mixer.music.play(loops=-1)
