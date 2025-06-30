import pygame


class Music:
    """
    This class represents a music player for handling and playing music tracks using the Pygame library.

    Attributes:
    - current_track: The track that is currently being played.
    - volume: The volume level of the music playback.

    Methods:
    - __init__
    - play
    - pause
    - stop
    - set_volume

    Each method is responsible for different aspects of music playback, such as initializing the player, controlling playback (play, pause, stop), and adjusting the volume of the current track.
    """

    def __init__(self):
        """
        Sets up the Music class instance and loads a specified audio track for playback.

        This method loads the specified music track from the compositions directory
        into the pygame mixer for playback.

        Parameters:
        - None

        Returns:
        None
        """

        self.now_plays = pygame.mixer.music.load("compositions/tracktwo.mp3")

    def ambient(self):
        """
        Initiates continuous playback of ambient music using the Pygame mixer.

        This method starts playing background music indefinitely, creating an immersive ambient sound experience.

        Returns:
            None: This method does not return any value.
        """

        pygame.mixer.music.play(loops=-1)
