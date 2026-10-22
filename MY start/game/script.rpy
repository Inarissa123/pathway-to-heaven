

default never_end_up = 0 #

default romance = 0

default dissapear = 0

define ta = Character("Timo and Amelia")

define d = Character("Delilah")

define h = Character("Hailey")

define t = Character("Timo")

define n = Character("Nema")

define a = Character("Amelia")

image Delilah Happy = "Delilah happy1.jpg"

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

show Delilah Happy 

d "Oh hi there! My name is Delilah but I'm sure you know that already."

d "What's your name?"

"Hailey was startled by Delilah's sudden greeting, she didn't expect her to come up to her like that but she answered Delilah either way."
 
menu:
    "It's Hailey, nice to meet you too.":
        d "Nice to meet you too.."
        d "So is there something you wanna ask me about? It's the first time I've seen you come up to me."

    "My name is Hailey. It's nice to meet you too!":
        d "Nice to meet you too!"
        d "So what are you here for? Just wondering you know, it's not like I see you coming up to me that much."

h "I just wanted to interview you for the school newspaper on how it's like to be the most popular girl in school, I'm part of the journalism club."

d "Oh alright then, I'll be happy to answer for the newspaper."

d "So are we going to do the interview here or somewhere else and what time?"

h "Oh right, meet me in the library after school 3:30pm, are you good with that?"

d "Sure thing, see you later!"

hide Delilah Happy with dissolve

"Hailey walks away from the crowd towards her friends in absolute surprise."

h "What am I doing!? I just randomly blurted out what came in my mind that I thought could be used as a way to be her friend and an interview!?"

h "All I've been doing in my club is reading true crime logs and writing them in the paper! Lastly I've never interviewed anyone in my life!"

h "Maybe I can get my friends to help me with the interview questions"

#make them show up at the same time later
show t1 at left with dissolve

show n1 at center with dissolve

show a1 at right with dissolve

t "Hey Hailey, is there something up in your mind? you don't look like your usual self today."

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

"In the library, Hailey's mind is running in circles unable to read the text on the paper even after all that planning with her friends her mind is still blank."

"Delilah is sitting across from her staring in confusion."

show Delilah Worried with dissolve #Worried delilah

d "Hailey are you alright? you look as if you're about to faint!"

h "Oh sorry, I kinda zoned out for a while. Let's get started with the interview."

h "So how does it feel to be the most popular girl in school?"

show Delilah Happy with dissolve

d "I've never really thought about it that much, I'm honestly just used to how most people treat me."

d "It's always been like this and I don't really know the reason why people seem to love me so much, but I do enjoy a good amount of the attention I get."

h "Alright, next question have you ever liked someone before and if you did, how were they like? It's alright if you don't want to answer this question, I don't want to make you feel uncomfortable."

d "I've never actually liked anyone before in my whole life, but if I were to have one I would want them to be someone that truly knows who I am."

h "I see, so what is your favorite thing to do in your free time?"

d "Now that I think of it, I don't really have one, I just kind of do what I'm told to do like my home work and chores, besides that I really just kind of sit around and do nothing."

h "I see, so what is your favorite subject in school?"

d "Probally science and social studies because it let's me learn about humans and how the surrounding world works."

h "Why humans specifically?"

d "I just find them {i}{b}interesting{/b}{/i} in a way."

"Hailey and Delilah continue their interview for a while but after listening to her answers she grew even more suspicius about Delilah, especially when she found humans {b}\"interesting\"{/b}."

#add transition here after the interview and state with her friends

scene otwh with dissolve

h "After the interview, I was left with a lot of questions about Delilah and her life."

h "And what's her thing about humans? It kinda creeped me out when she said that especially with the way she said it."

h "I also somehow ended up getting her number!?(From my sharp wits of course)"

#show t1 at left, a1 at right, n1 at left with dissolve

t "So what are you gonna do with her number? How did you even get it from her? Did you guys become friends or something?"

h "I guess you could say that she said it would be a great idea to have eaxh other's number just in case we wanted to talk to each other or something like that."

a "After hearing about the thing about humans she difinitely seems a bit creepy."

a "I mean I get when you're into anthropology and find that type of stuff interesting but by the way she said based on what on what you said makes me think she has something else going on in her mind."

h "What do you mean by \"something else going on in her mind?\""

a "I thought you'd know since you said you were creeped out too."

h "Of course I didn't, I just said it creeped me out because of her tone."

a "So what I meant by that is, that she probally has some odd plan cooking up in her head that probally manipulaaates people I guess."

n "How did you even reach to that conclusion?"

n "You watch too many mystery movies I swear to god Amelia."

a "What? They're way more interesting than whatever stupid dramas you watch you know!"

t "Calm down guys there's nothing to fight about movie genres,  but either way Nema's right."

#put the show lines in the bottom at the same time
show Amelia angry

show Nema smirk

a "Hey!"

h "I've gotta go off from here now guys I'll see you tomorrow!"

show Amelia happy

show Nema happy

n "Bye Hailey!"

ta "Bye Hailey!"

"As Hailey parted from her friends she started thinking about when she tried approaching Delilah."

"The more she went on in her head the more she remembered each detail in each scene."

"And at some point she realized that Delilah was looking at her direction."

"She was {b}staring{/b} at Hailey the entire whole time."

"A few minutes go by and she arrives to her home."

scene Room with dissolve

"Right as Hailey steps into her room, she hears a notification coming from her phone."
#play notif

h "It's from Delilah."

#make scene where her phone pops up
"insert phone text message scene"
#text messages: 
# D: Hey there Ley-ley!!
# D: I just wanted to see how you were doing, did you just get home?
# Hr:Why is she already texting me? And what's with the nickname, I haven't heard that since 2nd grade.
# menu:
# h1:I'm doing fine hbu? and yes I did just get home +dont endup together
# h2:Hey Delilah, doing good just got home feel like I'm about to explode it's way too cold out to even be real +romance??
# d1:Doing amazingg, just asked to check in on u becuse I felt like something might've happened to you otw home
# d2:lol ikr it's so cold out anyways I just wanted to check in on u had feeling smth might've happened
# h1+2:like what?
# d1+2: Oh nothing much Thought one of my fans might've came at you espescially since you talked to me face to face alone
# h1+2: How many times has anything like this happened to you for you to ask something like this?
# d1+2: lol actually it happens not too often usually because someone tried to get closer with me or something like that
# d1+2: anyways happy nothing bad happened see you later!
# h1+2: thanks see you too
#phone fades off
h "That was... interesting to say the least."

#scene transition for the next day

scene school gate with dissolve

#label with arriving at school


return