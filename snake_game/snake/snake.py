#! /usr/bin/python3

# Credits
'''

Main Theme: youtube(8-bit music, by Zuka)

'''


# Config
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
os.environ['SDL_VIDEO_CENTRED'] = '1'


# Imports
import pygame
import config


# Inits
#pygame.mixer.pre_init(*config.mixer.CONFIG) needed for sound effects
pygame.init()
window = pygame.display.set_mode(config.screen.RESOLUTION, pygame.SRCALPHA)
clock = pygame.time.Clock()

# Load assets
pygame.mixer.music.load(config.mixer.MAIN_THEME)

# Setup
pygame.mixer.music.play(-1)

# Funcs

#>	Check for quit
def get_do_events(run):
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    
    return run

# Classes

#>	Snake class
class snake_segment():
    
    def __init__(self):
        self.fade_count = 255
        self.colour = 255, 255, 255, self.fade_count
        self.image = config.snake.circle
        
    def update(self):
        print('seg update', self.fade_count)
        self.image.fill(config.screen.EMPTY)
        pygame.draw.circle(self.image, self.colour, config.snake.CENTRE, config.snake.RADIUS)
        self.image.set_alpha(self.fade_count)
        
        self.fade_count -= 1
        self.colour = 255, 255, 255, self.fade_count
        
        


def main():
    global window
    
    segments = [snake_segment()]
    
    run = True
    
    # Main Loop
    while run:
        for segment in segments:
            segment.update()
            window.blit(segment.image, config.screen.CENTRE)
        
        run = get_do_events(run)
        clock.tick(config.screen.FPS)
        pygame.display.flip()
    
    #Cleanup
    pygame.quit()
    
    
main()