import pygame

"""
We can load fonts from the systetm and render using
font.SysFont(). 
"""

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False

# Let's laod the font from system
font = pygame.font.SysFont("Inter", 60)

# Render the text in new surface
text = font.render("Hello, Game Creator", True, (158, 16, 16))
# 158, 16, 16 is just coordinate to place

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255))
    # we will see blit() in later tutorial
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()



"""

Additional info

all_font = pygame.font.get_fonts()
is another ways to initiated system default font.

font = pygame.font.Font(None, size)
using this, we can work with the attractive font in game.
"""