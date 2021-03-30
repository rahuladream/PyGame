import pygame

# Loading package modiles
pygame.init()

# Screen size defination
screen = pygame.display.set_mode((400, 300))

# Loop until pressed quit
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0,125, 255), pygame.Rect(30, 30, 60, 60))
    """
    Dimension of rect and screen place visualization
    (30, 30, 60, 60) -> rect size
    (0, 125, 255) -> Place where it to be drawn
    """
    pygame.display.flip()