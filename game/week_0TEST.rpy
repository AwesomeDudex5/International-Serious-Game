# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#---VARIABLES---
#define p = Character("Peter", color="68a24b")
#default pressure = 0


# The game starts here.

label debug_start:

    scene background 1
    play music "audio/Liyue.mp3"

    show peter normal at right
    show kobe normal at left:
        xalign 0.5 yalign 1.0
    p "Hi I'm Peter from Fortnite."

    show peter rich at right
    show kobe tired at left:
        xalign 1.0 yalign 1.0
    p "This school looks poggers!"

menu:
    "Genshin Impact: Add Pressure": 
        $ pressure += 1
        jump chapter_one
    "Star Rail: Minus Pressure":
        $ pressure -= 1
        jump chapter_two

label chapter_one:
    scene background 2:
        zoom 2.0
    show peter normal at right
    show peter rich
    p "Is this the place from Genshin Impact? Pressure: [pressure]"
    jump story_end_one

label chapter_two:
    scene background 2:
        zoom 2.0
    show peter normal at right
    show peter rich
    p "Is this the place from Honkai Star Rail? [pressure]"
    jump story_end_two

label story_end_one:
    p "The real Genshin was the Impact along the way"
    jump wwwwww

label story_end_two:
    p "The real Honkai was the Star Rai we made along the way."
    jump wwwwww

