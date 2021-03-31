import pygame

"""
KEYDOWN detects the key press and, KEYUP detects the key
release. Both events have two attributes

- key: an integer id which represents every key on keyboard.
- mod: bitmast of all the modifier keys that were in the pressed state
"""

pygame.init()

# Set screen title
pygame.display.set_caption(u'Keyboard Press Event')

# Set screen display size
pygame.display.set_mode((400, 400))

while True:
    # Gets an single event from the event queue
    event = pygame.event.wait()
    # if the 'close' button clicked window must be closed
    if event.type == pygame.QUIT:
        break

    # Now let's detect 'KEYDOWN' and 'KEYUP' events
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        key_name = pygame.key.name(event.key) # Get the name of key pressed
        key_name = key_name.upper() # convert the key name in upper case

        if event.type == pygame.KEYDOWN:
            print(u'{} key pressed'.format(key_name))

        elif event.type == pygame.KEYUP:
            print('{} key released'.format(key_name))