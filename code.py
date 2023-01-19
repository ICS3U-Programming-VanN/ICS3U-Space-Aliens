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
    coin_sound = open("coin.wav", "rb")

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

    # Sets framerate to 60fps and manages input
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

    # Initialize Score Variable
    score = 0

    # Creates text object
    score_text = stage.Text(width=29, height=14)

    # Clears the text object
    score_text.clear()

    # Sets the cursor position
    score_text.cursor(0, 0)

    # Moves text position
    score_text.move(1, 1)

    # Displays the score
    score_text.text(f"Score: {score}")

    # This function takes the lighting bolt from off the screen to off the screen
    def show_lighting_bolt():
        # Iterates through each lighting bolt held in the lighting_bolt list
        for lighting_bolt_number in range(len(lighting_bolt)):
            # IF the lighting bolt is off screen
            if lighting_bolt[lighting_bolt_number].x < 0:
                # Moves the lighting bolt to a random place at the top of the screen
                lighting_bolt[lighting_bolt_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )

                # Exits loop once the alien has been place back on the screen
                break

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

    # Prepares the sound
    # Open the "boom.wav" file for reading
    boom_sound = open("boom.wav", "rb")

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

    # Lighting bolt sprite that will come at the user
    lighting_bolt = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # Creates list to hold all the lighting bolts
    lighting_bolt = []

    # Creates a lighting bolt object for the number of MAX lighting bolts
    for lighting_number in range(constants.TOTAL_NUMBER_OF_LIGHTING_BOLTS):
        a_single_lighting_bolt = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )

        # Appends the lighting bolt to the list
        lighting_bolt.append(a_single_lighting_bolt)

    # Calls function to place the lighting bolt on the screen at a random location from the top
    show_lighting_bolt()

    # Creates list for lasers to be shot
    lasers = []

    # Iterates for the max number of lasers
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        # Creates laser object
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )

        # Adds laser to lasers list
        lasers.append(a_single_laser)

    # Creates stage for background and sets framerate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Sets all layers of the sprites and determines the order they show up
    game.layers = [score_text] + lasers + [ship] + lighting_bolt + [background]

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
            pass

        # IF the user presses the SELECT button
        if keys & ugame.K_SELECT != 0:
            pass

        # IF the user presses the "Right" button
        if keys & ugame.K_RIGHT != 0:
            # Moves ship to the right
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            # Prevents ship from going off screen
            else:
                ship.move(0, ship.y)

        # IF the user presses the "Left" button
        if keys & ugame.K_LEFT != 0:
            # Moves the ship to the left
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                # Prevents ship from going left
                ship.move(160, ship.y)

        # IF the user presses the "Up" button
        if keys & ugame.K_UP != 0:
            pass

        # IF the user presses the "Down" button
        if keys & ugame.K_DOWN != 0:
            pass

        # IF A button is pressed
        if a_button == constants.button_states["button_just_pressed"]:
            # Iterates for every laser we have
            for laser_number in range(len(lasers)):
                # Moves laser to above the sprite
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x + 3, ship.y)

                    # Plays the firing sound effect
                    sound.play(firing_sound)

                    # Breaks out the loop
                    break

        # Moves the laser each frame
        for laser_number in range(len(lasers)):
            # Checks if there is a laser on screen
            if lasers[laser_number].x > 0:
                # Moves the laser
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )

                # Checks if the laser if off screen
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    # Moves laser to temporary location
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # Iterates for each lighting bolt in the lighting_bolt list
        for lighting_bolt_number in range(len(lighting_bolt)):
            # If the lighting of is on the screen
            if lighting_bolt[lighting_bolt_number].x > 0:
                # Moves the lighting bolt down (at the lighting bolt speed)
                lighting_bolt[lighting_bolt_number].move(
                    lighting_bolt[lighting_bolt_number].x,
                    lighting_bolt[lighting_bolt_number].y + constants.ALIEN_SPEED,
                )

                # IF the lighting bolt has gone off screen
                if lighting_bolt[lighting_bolt_number].y > constants.SCREEN_Y:
                    # Moves lighting bolt to off screen holding location
                    lighting_bolt[lighting_bolt_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

                    # Calls function to show the lighting bolt
                    show_lighting_bolt()

                    # Decrements score by 1
                    score -= 1

                    # Ensures that the score stays at 0 or above
                    if score < 0:
                        # Sets score to zero
                        score = 0

                    # Clears the score text
                    score_text.clear()

                    # Sets the cursor to (0, 0)
                    score_text.cursor(0, 0)

                    # Moves the score text to (1, 1)
                    score_text.move(1, 1)

                    # Displays the score/reprints it
                    score_text.text("Score: {0}".format(score))

        # Iterates through lasers list
        for laser_number in range(len(lasers)):
            # IF the laser is on screen
            if lasers[laser_number].x > 0:
                # Iterates for the length of lighting_bolt list
                for lighting_bolt_number in range(len(lighting_bolt)):
                    # IF the alien is on screen
                    if lighting_bolt[lighting_bolt_number].x > 0:
                        # IF the laser and alien collide
                        if stage.collide(
                            lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            lighting_bolt[lighting_bolt_number].x + 1,
                            lighting_bolt[lighting_bolt_number].y,
                            lighting_bolt[lighting_bolt_number].x + 15,
                            lighting_bolt[lighting_bolt_number].y + 15,
                        ):
                            # Moves the lighting bolt off screen
                            lighting_bolt[lighting_bolt_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )

                            # Moves the laser off screen
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )

                            # Stops any sound from playing
                            sound.stop()

                            # Plays the boom sound
                            sound.play(boom_sound)

                            # Calls function twice to spawn two new lighting bolts
                            show_lighting_bolt()
                            show_lighting_bolt()

                            # Increments the score
                            score = score + 1

                            # Clears the score text and reprints/resets it
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)

                            # Displays updated score
                            score_text.text("Score: {0}".format(score))

        # Renders the sprites
        game.render_sprites(lasers + [ship] + lighting_bolt)

        # Ensures that the game will run at 60fps by pausing the loops
        game.tick()


if __name__ == "__main__":
    # Starts Splash Scene
    splash_scene()
