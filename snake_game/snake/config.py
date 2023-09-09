# Snake game config

# Config
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# Imports
import pygame
# Init
pygame.init()

# Screen config
class screen():
    
    WIDTH = 800
    HEIGHT = 600
    RESOLUTION = WIDTH, HEIGHT
    
    CENTRE = WIDTH / 2, HEIGHT / 2
    
    CENTRETOP = WIDTH / 2, 0
    CENTREBOTTOM = WIDTH / 2, HEIGHT
    CENTRELEFT = 0, HEIGHT / 2
    CENTRERIGHT = WIDTH, HEIGHT / 2
    
    TOPLEFT = 0, 0
    TOPRIGHT = WIDTH, 0
    BOTTOMLEFT = 0, HEIGHT
    BOTTOMRIGHT = WIDTH, HEIGHT
    
    FPS = 30
    
    FLAGS = pygame.FULLSCREEN
    
    CONFIG = RESOLUTION, FLAGS
    
    EMPTY = 0, 0, 0, 0
    
class mixer:
    CONFIG = 41000, -16, 1, 512
    
    MAIN_THEME = 'assets/Music/Theme.ogg'
class snake:
    WIDTH, HEIGHT = 100, 100
    SIZE = WIDTH, HEIGHT
    CENTRE = WIDTH / 2, HEIGHT / 2
    RADIUS = WIDTH / 2
    
    
    circle = pygame.Surface(SIZE, pygame.SRCALPHA)