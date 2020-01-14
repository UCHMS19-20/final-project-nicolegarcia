import pygame
import os
import sys
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Sets width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3
 
# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
 
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
 
        # Make top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Snake Game')
 
allspriteslist = pygame.sprite.Group()
apple_image = pygame.image.load('src/img/apple.png') 
apple_position = (random.randrange(1,70)*10,random.randrange(1,50)*10)
apple_rect = pygame.Rect(apple_position, (20, 20))

# Create an initial snake
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()
done = False
 
while not done:
    # Clear screen
    screen.fill(BLACK)
     # Draw apple
    print(apple_rect)
    pygame.draw.rect(screen, (255,0,0), apple_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
            if event.key == pygame.K_SPACE:
                apple_rect.x = random.randrange(1,70)*10
                apple_rect.y = random.randrange(1,50)*10

 
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
 
    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)
 
    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)
 
    # Draw apple
    
    # screen.blit(apple_image, apple_rect)
   
    
    allspriteslist.draw(screen)
 
    # Flip screen
    pygame.display.flip()
 
    # Pause, snake will never go more quickly than 5 frames
    clock.tick(5)
 
pygame.quit()