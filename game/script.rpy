﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nissa")
define j = Character("Jane")
define a = Character("Ania")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg start

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nissa worried

    # These display lines of dialogue.

    n "Oh, hi! My friends are coming... You're probably be better off..."

    hide nissa

    show ania unhappy

    a "Hi. Traffic was horrendous."

    # This ends the game.

    return
