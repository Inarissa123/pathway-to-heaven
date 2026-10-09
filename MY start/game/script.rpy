
# Declare characters used by this game. The color argument colorizes the
# name of the character.




define e = Character("Delilah")

define h = Character("Hailey")

define t = Character("Timo")

define n = Character("Nema")

define a = Character("Amelia")

image dh1 = "Delilah happy1.jpg"

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

h "It was an odd idea to me how anybody could be this popular."

h "Even in my old school which was known for popular people to have a cultish like following it was never as severe as here."

h "Only a few people didn't follow along with everybody else like me."

h "their names are Timo, Nema, Amelia, and a few others."

h "The first three I named are all my friends and we sit together at lunch and recess everyday."

h "And today is the day I try to become friends with Delilah."

scene moving through crowd with dissolve

"Hailey squeezes through the crowd of people trying to reach Delilah."

"When Hailey finally reached the center of the pool of people, she was finally able to see Delilah upclose for the first time."

scene closeup of Delilah with dissolve

"When Hailey saw her upclose she notcied that Delilah had skin that almost seemed plastic, her long dark wavy hair so shiny it glowed like strings of a glass mirror."

"But there was one thing that stuck out to Hailey" 

"Delilah's eyes."

scene Deli Eyes with dissolve

"Her eyes had had no spark behind them, they were completely dull."

"Every person that hailey had seen or met had a spark in their eyes, even the most depressed person she had met had atleast a little smidge of spark in them."

"This made Hailey feel even more uneasy about her."

"Something was definetely {i}off{/i} about Delilah."

scene canteen with dissolve

show dh1 

e "Oh hi there! My name is Delilah but I'm sure you know that already."

e "What's your name?"

"Hailey was startled by Delilah's sudden greeting, she didn't expect her to come up to her like that but she answered Delilah either way."
 
menu:
    "It's Hailey, nice to meet you too.":
        e "Nice to meet you too.."
        e "So is there something you wanna ask me about? It's the first time I've seen you come up to me."

    "My name is Hailey. It's nice to meet you too!":
        e "Nice to meet you too!"
        e "So what are you here for? Just wondering you know, it's not like I see you coming up to me that much."

h "I just wanted to interview you for the school newspaper on how it's like to be the most popular girl in school, I'm part of the journalism club."

e "Oh alright then, I'll be happy to answer for the newspaper."

e "So are we going to do the interview here or somewhere else and what time?"

h "Oh right, meet me in the library after school 3:30pm, are you good with that?"

e "Sure thing, see you later!"

hide dh1 with dissolve

"Hailey walks away from the crowd towards her friends in absolute surprise."

h "What am I doing!? I just randomly blurted out what came in my mind that I thought could be used as a way to be her friend and an interview!?"

h "All I've been doing in my club is reading true crime logs and writing them in the paper! Lastly I've never interviewed anyone in my life!"

h "Maybe I can get my friends to help me with the interview questions"

show t1 with dissolve

t "Hey Hailey, is there something up in your mind? you don't look like your usual self today."

show n1 with dissolve

n "Yeah there's defenitely something off about you"

a "I saw you talking with Delilah just now did something happen between you guys?"

h "I was trying to become her friend because I got curios and ended up asking her to be interviewed for the school newspaper even though I've never done anything like that before!"

h "I was wondering if you guys could help me plan quetions for the interview since I can't think of anything to ask her."

t "Sure thing, I can help you with that. "

t "What about the rest of you guys? "

a "Sure, I can help you with that too. "

n "Sure why not. "

h "Thank you so much guys, I really appreciate it!"

#add transition here with a label about the interview

scene library with dissolve


return