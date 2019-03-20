""" Data regarding music in game """

import pygame

VOLUME = 1.0

class Sound:
    """Sound used in game"""
    sound_walk_against_wall = "sounds/non_walkable.wav"

    @staticmethod
    def play_sound(filename, volume=VOLUME):
        """Play a single sound effect"""
        effect = pygame.mixer.Sound(filename)
        effect.set_volume(volume)
        effect.play()

class Music:
    """Music used in game"""
    background_music = "musics/background.mp3"

    @staticmethod
    def play_music(filename, loop=False, volume=VOLUME):
        """Play music (endlessly or not)"""
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        if loop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()
