import pygame
from math import pi

"""
Pygame provides geometry functions to draw simple shapes to the surface. 

Rectangle:
pygame.draw.rect(surface, color, rect)  

Polygon:
pygame.draw.polygon(surface,color,points)

Ellipse:
pygame.draw.ellipse(surface, color, rect)  

Straight Line:
pygame.draw.line(surface,color,start_pos,end_pos,width)  

Circle:
circle(surface, color, center, radius)

Elliptical arc:
pygame.draw.arc(surface, color, rect, start_angle, stop_angle)   
"""

# Now let's code these and see it by myself

pygame.init()
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Draw Geometry')

done = False
clock = pygame.time.Clock()

while not done:
    # clock.tick() limits the while loop to a max of 10 times per second
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # All drawing code will occurs after the for loop but inside the main
    # while done = False

    # clear the default screen background and set it to white

    screen.fill((0, 0, 0))

    # Draw a green line with 5 px wide
    pygame.draw.line(screen, (0, 255, 0), [0, 0], [50, 40], 5)

    # Fn must write after all the other drawing commands
    pygame.display.flip()

# Quit after execution
pygame.quit()