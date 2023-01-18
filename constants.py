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

# Defines the limit of lasers in the game
TOTAL_NUMBER_OF_LASERS = 10

# Defines the frames per second
FPS = 60

# Sets the sprite movement speed
SPRITE_MOVEMENT_SPEED = 1

# Sets the ship speed
SHIP_SPEED = 1

# Sets the alien speed
ALIEN_SPEED = 1

# Sets the laser speed
LASER_SPEED = 2

# Sets how far the lasers/aliens will be off the screen for x coordinate
OFF_SCREEN_X = -100

# Sets how far the lasers/aliens will be off the screen for y coordinate
OFF_SCREEN_Y = -100

# Makes sure that the bottom of sprite is off screen from the top
OFF_TOP_SCREEN = -1 * SPRITE_SIZE

# Makes sure sprite is off the screen from the bottom
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE

# For button states
button_states = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}

# Palette for red text
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
