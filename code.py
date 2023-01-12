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
    # ****Reminder: change the sprites later
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Sets the background to image 0 in the image bank
    # and sets size to 10x8 tiles of size 16x16
    background = stage.Grid(image_bank_background, 10, 8)

    # User's sprite that will continually update
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Creates stage for background and sets framerate to 60fps
    game = stage.Stage(ugame.display, 60)

    # Sets all layers of the sprites and determines the order they show up
    game.layers = [ship] + [background]

    # Renders all sprites
    game.render_block()

    # Repeats forever (game loops)
    while True:
        # Gets User Input
        keys = ugame.buttons.get_pressed()

        # IF the user presses the A button
        if keys & ugame.K_X:
            print("A pressed")

        # IF the user presses the B button
        if keys & ugame.K_O:
            print("B pressed")

        # IF the user presses the START button
        if keys & ugame.K_START:
            print("START pressed")

        # IF the user presses the SELECT button
        if keys & ugame.K_SELECT:
            print("SELECT pressed")

        # IF the user presses the "Right" button
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)

        # IF the user presses the "Left" button
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)

        # IF the user presses the "Up" button
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)

        # IF the user presses the "Down" button
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)

        # Renders the sprites
        game.render_sprites([ship])

        # Ensures that the game will run at 60fps by pausing the loops
        game.tick()


if __name__ == "__main__":
    game_scene()
