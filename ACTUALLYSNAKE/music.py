import pygame


class Music:
    """
    A class to represent and manage music playback.

    This class is responsible for initializing and playing music tracks
    using the Pygame mixer. It allows for ambient music to be played in
    a loop, providing an audio background for different applications.

    Methods:
        __init__
        ambient

    Attributes:
        None

    The __init__ method initializes a new instance of the Music class
    and loads a music track from a specified file path. The ambient method
    starts playing the loaded ambient music in a loop, continuing to play
    until it is explicitly stopped.
    """

    def __init__(self):
        """
        Initializes a new instance and loads a music track.

        This method sets up the instance by loading the specified music track
        from the given file path using the pygame mixer.

        Parameters:
            None

        Returns:
            None
        """
        self.now_plays = pygame.mixer.music.load("compositions/tracktwo.mp3")

    def ambient(self):
        """
        Play ambient music in a loop.

            This method starts playing the ambient music using the Pygame mixer. The music will loop indefinitely until stopped.

            Parameters:
                None

            Returns:
                None
        """
        pygame.mixer.music.play(loops=-1)
