# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Delilah")

define h = Character("Hailey")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene school hallway with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
h "Delilah was the popular girl of the school, always crowded with people, constantly asked out on dates, and never seemed to have a single flaw to people"

h "Every time I passed by her in the hallway or saw her from afar, I always seem to feel something off as if she was hiding something."

h "Every time I felt that I would brush it off, as she was always an open book to others, from what they said."

h "But I wasn't so sure about that." 

h "So in the end I thought it would be a great idea to be her friend just to see if I was right."

scene canteen with dissolve
    # These display lines of dialogue.
show crowd of people

h "The canteen is always like this."

h "Same crowd, same people,same everything."

h "And the crowd is always surrounding the same person, Delilah."

h "Only a few people didn't follow along with everybody else like me."

h "their names are Timo, Nema, Amelia, and a few others."

h "The first three I named are all my friends and we sit together at lunch and recess everyday."

h "And today is the day I try to become friends with Delilah."

"Hailey squeezes through the crowd of people "

  #  e "Oh hi! My name is Delilah but I'm sure you know that already."

   # e "What's your name?"

   # menu:
 #        "It's Hailey, nice to meet you too.":
 #            e "Nice to meet you too.."

 #       "My name is Hailey. It's nice to meet you too!":
  #       e "Nice to meet you too!"

    # This ends the game.

return