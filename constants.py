#!/usr/bin/env python3
# Created by: Van Nguyen
# Created on: Jan, 12 2023
# This is the constants file for the "Climb to the sky" game on the PyBadge


# PyBadge screen size is 160x128 | Sprites are 16x16
# Declared Constants
# Screen Size
SCREEN_X = 160
SCREEN_Y = 128

# Defines grid size of the screen
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8

# Defines sprite size
SPRITE_SIZE = 16

# Defines the number of lighting bolts in the game
TOTAL_NUMBER_OF_LIGHTING_BOLTS = 5

# Defines the frames per second
FPS = 60

# Defines the sprite movement speed
SPRITE_MOVEMENT_SPEED = 1

# For button states
button_states = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
