import pygame

pygame.init()

# Assign screen and size
white = (255, 255, 255)
size = (1000, 300)
# Increased width as our image size is quite big in width

# Defining the surface
display_surface = pygame.display.set_mode(size)

# Set the pygame window name
pygame.display.set_caption('Image Display using PyGame')

# Creating a surface object, image is drawn on it
image = pygame.image.load(r'assets/voltry_log.png')

# Infinite Loop
while True:
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Draws the surface object to the screen
        pygame.display.update()

