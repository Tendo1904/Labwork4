import pygame
class Music():
    """
    Class Music:
        This class represents a music player that allows users to play, pause, stop and control audio tracks.
    
        Attributes:
        - current_track: a string representing the path to the current audio track
        - is_playing: a boolean indicating whether the music is currently playing
        - volume: an integer representing the volume level of the music player
    
        Methods:
        - play: plays the current audio track
        - pause: pauses the playback of the current audio track
        - stop: stops the playback of the current audio track
        - set_volume: sets the volume level of the music player
    """

    def __init__(self):
        """
        Initializes the objects with the current playing track using pygame mixer.
        
        Args:
            self: the instance itself
        
        Class Fields Initialized:
            now_plays: indicates the currently playing track by loading "compositions/tracktwo.mp3"
        
        Returns:
            None
        """
        self.now_plays = pygame.mixer.music.load("compositions/tracktwo.mp3")
    def ambient(self):
        """
        Plays ambient music continuously in a loop.
        
        Args:
        - loops (int): The number of times the music will loop. Default is -1, which means the music will loop indefinitely.
        
        Returns:
        None
        
        WHY: The method "ambient" inside the Music class plays ambient music continuously in a loop by using the Pygame library function pygame.mixer.music.play() with the loops parameter set to -1, indicating that the music will loop indefinitely. This functionality is likely implemented to provide a continuous and ambient audio experience within the context of the game or application developed in the project.
        """
        pygame.mixer.music.play(loops=-1)
