import pygame

# Load required modules
pygame.init()

# Desired window size
screen = pygame.display.set_mode((400, 500))
done = False # Set True for quiting

while not done:
    for event in pygame.event.get():
        # use to empty the event queue
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()