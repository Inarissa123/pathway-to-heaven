# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Delilah")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene school hallway with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show delilah happy

    # These display lines of dialogue.

    e "Oh hi! My name is Delilah but I'm sure you know that already."

    e "What's your name?"

    menu:

        "It's Hailey, nice to meet you too.":
             e "Nice to meet you too.."

        "My name is Hailey. It's nice to meet you too!":
         e "Nice to meet you too!"

    # This ends the game.

    return