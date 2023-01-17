#!/usr/bin/env python3
# Created by: Van Nguyen
# Created on: Jan, 9 2023
# This program is the "Climb to the sky" game on the PyBadge


import random
import time

import constants
import stage
import ugame


# This function is for the splash scene
def splash_scene():
    # Prepares the splash scene sound
    coin_sound = open("coin.wab", "rb")

    # Accesses the audio module from the ugame library
    sound = ugame.audio

    # Stops any sound from currently playing
    sound.stop()

    # Un-mutes the sound
    sound.mute(False)
    sound.play(coin_sound)

    # Loads the background and sprite image bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Creates the background image
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # Split the image into tile:
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    #
    game = stage.Stage(ugame.display, constants.FPS)

    # Adds the background to the layers list
    game.layers = [background]

    # Renders the background
    game.render_block()

    # Game loop forever
    while True:
        # Pauses for 2 seconds then switches to menu scene
        time.sleep(2.0)
        menu_scene()


# This function is for the Menu Scene
def menu_scene():
    # Loads background and sprite image bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Adds text object
    text = []

    # Creates text object
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # Moves text to (20, 10)
    text1.move(20, 10)

    # Sets the text to "VAN UNITED GAMES"
    text1.text("VAN UNITED GAMES")

    # Adds text object to the text list
    text.append(text1)

    # Creates another text object
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # Moves text object to (40, 110)
    text2.move(40, 110)

    # Sets text object to "PRESS START"
    text2.text("PRESS START")

    # Adds text object to text list
    text.append(text2)

    # Creates background grid
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # Creates the state object and sets the FPS to 60
    game = stage.Stage(ugame.display, constants.FPS)

    # Adds background to layers list
    game.layers = text + [background]

    # Draws the background
    game.render_block()

    # Loops forever
    while True:
        # Gets user input
        keys = ugame.buttons.get_pressed()

        # IF the start button is pressed
        if keys & ugame.K_START != 0:
            # Plays the game scene
            game_scene()

        # Ensures that the game will be at 60fps by stopping loop
        game.tick()


# This function is the main game game_scene
def game_scene():
    # Image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # ****Reminder: change the sprites later
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Keeps track of the state of the buttons
    a_button = constants.button_states["button_up"]
    b_button = constants.button_states["button_up"]
    start_button = constants.button_states["button_up"]
    select_button = constants.button_states["button_up"]

    # Prepares the sound
    # Open the "pew.wav" file for reading
    firing_sound = open("pew.wav", "rb")

    # Accesses the audio module of the ugame library
    sound = ugame.audio

    # Stops any playing sounds
    sound.stop()

    # Un-mutes the music/sounds
    sound.mute(False)

    # Sets the background to image 0 in the image bank
    # and sets size to 10x8 tiles of size 16x16
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # Randomizes the game scene background
    # Iterates through each X and Y coordinate
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            # Picks a random tile from (1-3)
            tile_picked = random.randint(1, 3)

            # Places the tile at X and Y location
            background.tile(x_location, y_location, tile_picked)

    # User's sprite that will continually update
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # Lighting bolt sprite will come at the user
    lighting_bolt = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # Creates stage for background and sets framerate to 60fps
    game = stage.Stage(ugame.display, 60)

    # Sets all layers of the sprites and determines the order they show up
    game.layers = [ship] + [lighting_bolt] + [background]

    # Renders all sprites
    game.render_block()

    # Repeats forever (game loops)
    while True:
        # Gets User Input
        keys = ugame.buttons.get_pressed()

        # IF the user presses the A button
        if keys & ugame.K_X != 0:
            # If the A button was pressed, updates button state
            if a_button == constants.button_states["button_up"]:
                a_button = constants.button_states["button_just_pressed"]
            # Checks if the button is still pressed and updates button state
            elif a_button == constants.button_states["button_just_pressed"]:
                a_button = constants.button_states["button_still_pressed"]
        # IF A button is not pressed
        else:
            # IF the button has been released and updates button state
            if a_button == constants.button_states["button_still_pressed"]:
                a_button = constants.button_states["button_released"]
            # Updates button state to "button_up"
            else:
                a_button = constants.button_states["button_up"]

        # IF the user presses the B button
        if keys & ugame.K_O != 0:
            pass

        # IF the user presses the START button
        if keys & ugame.K_START != 0:
            print("START pressed")

        # IF the user presses the SELECT button
        if keys & ugame.K_SELECT != 0:
            print("SELECT pressed")

        # IF the user presses the "Right" button
        if keys & ugame.K_RIGHT != 0:
            # Moves ship to the right
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            # Prevents ship from going off screen
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        # IF the user presses the "Left" button
        if keys & ugame.K_LEFT != 0:
            # Moves the ship to the left
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                # Prevents ship from going left
                ship.move(0, ship.y)

        # IF the user presses the "Up" button
        if keys & ugame.K_UP != 0:
            pass

        # IF the user presses the "Down" button
        if keys & ugame.K_DOWN != 0:
            pass

        # IF A button is pressed
        if a_button == constants.button_states["button_just_pressed"]:
            # Plays the firing sound effect
            sound.play(firing_sound)

        # Renders the sprites
        game.render_sprites([ship] + [lighting_bolt])

        # Ensures that the game will run at 60fps by pausing the loops
        game.tick()


if __name__ == "__main__":
    # Starts Splash Scene
    splash_scene()
