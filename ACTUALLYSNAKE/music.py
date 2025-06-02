import pygame


class Music:
    """
    A class that represents a music player for audio tracks using Pygame.

    This class is responsible for loading and playing audio tracks, providing
    functionalities for creating an immersive music experience.

    Methods:
        __init__:
        ambient:

    Attributes:
        None

    The __init__ method initializes the music player by loading the audio
    track "tracktwo.mp3". The ambient method starts playing ambient music
    in a loop to enhance the environment.
    """

    def __init__(self):
        """
        Initializes a music player by loading a specific audio track.

            This method loads the audio track "tracktwo.mp3" using the Pygame
            mixer module, preparing it for playback when the player is used.

            Parameters:
                None

            Returns:
                None
        """
        self.now_plays = pygame.mixer.music.load("compositions/tracktwo.mp3")

    def ambient(self):
        """
        Starts playing ambient music in a loop.

            This method uses the Pygame mixer to start playing background music indefinitely,
            creating an immersive ambient sound environment.

            Returns:
                None: This method does not return any value.
        """
        pygame.mixer.music.play(loops=-1)
