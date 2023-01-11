#!/usr/bin/env python3
# Created by: Van Nguyen
# Created on: Jan, 9 2023
# This program is that "Space Aliens" game on the PyBadge


import stage
import ugame


def game_scene():
    # This function is the main game game_scene

    # Image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # Sets the background to image 0 in the image bank
    # and sets size to 10x8 tiles of size 16x16
    background = stage.Grid(image_bank_background, 10, 8)

    # Creates stage for background and sets framerate to 60fps
    game = stage.Stage(ugame.display, 60)

    # Sets all layers of the sprites and determines the order they show up
    game.layers = [background]

    # Renders all sprites
    game.render_block()

    # Repeats forever (game loops)
    while True:
        # Placeholder keyword
        pass


if __name__ == "__main__":
    game_scene()
