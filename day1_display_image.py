import pygame

pygame.init()

# Assign screen and size
white = (255, 255, 255)
size = (400, 400)

# Defining the surface
display_surface = pygame.display.set_mode(size)

# Set the pygame window name
pygame.display.set_caption('Image Display using PyGame')

# Creating a surface object, image is drawn on it
image = pygame.image.load(r'')
