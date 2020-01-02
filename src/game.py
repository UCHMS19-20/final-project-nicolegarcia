import pygame
import os
import sys

class PyManMain:
    """The Main PyMan Class – This class handles the main
    initialization and creating of the Game."""
    def __init__(self, width=640, height=480):
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        """This is the Main Loop of the Game"""
        """Load All of our Sprites"""
        self.LoadSprites()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.snake_sprites.draw(self.screen)
            pygame.display.flip()
            
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.pacman = Pacman()
        self.pacman_sprites = pygame.sprite.RenderPlain((self.pacman))

MainWindow = PyManMain()
MainWindow.MainLoop()

class Pacman(pygame.sprite.Sprite):
    """This is our Pacman that will move around the screen"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(pacman.jpg,-1)
        self.pellets = 0