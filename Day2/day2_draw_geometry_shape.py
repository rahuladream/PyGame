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

    # Draw a rectangle outline
    pygame.draw.rect(screen, (0, 0, 0), [75, 10, 50, 20], 2)

    # Draw a solid rectangle
    pygame.draw.rect(screen, (0, 0, 0), [150, 10, 50, 20])

    # This draw an ellipse outline, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, (255, 0, 0), [225, 10, 50, 20], 2)

    # This draw a solid ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, (255, 0, 0), [300, 10, 50, 20])

    # Draw a triangle using the polygon function
    pygame.draw.polygon(screen, (0, 0, 0), [[100, 100], [0, 200], [200, 200]], 5)

    # This draw a circle
    pygame.draw.circle(screen, (0, 0, 255), [60, 250], 40)

    # This draw an arc
    pygame.draw.arc(screen, (0, 0, 0), [210, 75, 150, 125], 0, pi / 2, 2)

    # Fn must write after all the other drawing commands
    pygame.display.flip()

# Quit after execution
pygame.quit()