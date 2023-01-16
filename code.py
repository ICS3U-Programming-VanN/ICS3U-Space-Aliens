#!/usr/bin/env python3
# Created by: Van Nguyen
# Created on: Jan, 9 2023
# This program is that "Space Aliens" game on the PyBadge


import constants
import stage
import ugame


def game_scene():
    # This function is the main game game_scene

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
    background = stage.Grid(image_bank_background, 10, 8)

    # User's sprite that will continually update
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

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
    game_scene()
