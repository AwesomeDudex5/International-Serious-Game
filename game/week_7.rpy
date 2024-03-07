


label week_7_debug:
    jump week_7_start

label week_7_start:
    $ current_week = 7
    jump week_7_screen_display

label week_7_screen_display:
    scene background week
    call screen week_7_screen
    jump week_7_dialogue

define talk_with_andy_flag = 0
define talk_with_alex_flag = 0
$ bool_test = false


#Start of the dialogue
label week_7_dialogue:
    scene background school
    show screen pressure_display

    "(It is the last few weeks before the semester ends)"

    show teacher normal
    Instructor "Alright, today's lecture concludes here. Next, I'd like to remind everyone about the requirements for the final assignment." 
    Instructor "This is a group project. You need to form groups and, as a team, create a bar prototype for a mobile game."
    Instructor "For this assignment, I encourage you not to team up with friends who speak the same language or those you've teamed up with before." 
    Instructor "This will help you socialize and collaborate with a broader range of classmates."

    hide teacher normal

label week_7_talk_options:
    "(Peter looks around for someone to team up with)"

menu:
    "Talk with Andy" if talk_with_andy_flag == 0:
        $ talk_with_andy_flag = 1
        jump week_7_talk_with_andy
    "Talk with Alex" if talk_with_alex_flag == 0:
        $ talk_with_alex_flag = 1
        jump week_7_talk_with_alex
    "Talk with Student 1":
        jump week_7_talk_with_student1



label week_7_talk_with_andy:
    show peter normal at left
    Peter "Hi Andy! Do you mind teaming up with me?"

    show bill normal at right
    Andy "Sorry, Peter, this time I want to challenge myself. I hope to make new friends and improve my language and social skills."
    Andy "Perhaps you can also try challenging yourself."

    hide peter normal
    hide bill normal
    jump week_7_talk_options


label week_7_talk_with_alex:
    show peter normal at left
    Peter "Hello Alex, have you already found your team?"

    show alex normal at right
    Alex "Yes, Peter, I've already found my team members. We've started discussing the game theme."

    hide peter normal
    hide alex normal
    jump week_7_talk_options


label week_7_talk_with_student1:
    show peter normal at left
    Peter "Hello, Ehh…Do you mind teaming up with me?"

    show student1 normal at right
    Student1 "Hmm... kén, wi ar still lackin' a team memba, so yu k?n join us."
    "(You still find it a bit hard to understand her. But you decide to team up with her anyway)"
    Peter "Ok, let's form a team then. Um...Sera..fina?"
    Seraphina "It’s Seraphina, yu can kawl mi Sera."
    Peter "Okok. So..for this final project, the instructor is expecting us to…"
    Seraphina "Wi need t? create a paper prOto!yPe for a mobile game, d?e professor talked 'bout it in class."
    Peter "Ohh, yes, paper prototype. Do you have any thoughts on the game genre?"
    Seraphina "I dunn? kno... I prolly like games 'bout Peits?. Like Cats. I might prefer a simulation game."

    hide peter normal
    hide student1 normal

    "(After talking with Seraphina about the project, Peter goes home to work on the project)"

label week_7_home:
    scene background room

    "(Peter arrives home and settles into his room)"
    "(He then starts brainstorming for the project)"

    show peter normal

    Peter "Ah, this group assignment is really giving me a headache."
    Peter "I haven't collaborated much with others before, and her accent is making it a bit hard for me to understand." 
    Peter "What did she say before?"

    "(Peter looks through his notes)"

    Peter "I hope my understanding of what she said is correct, but I have to trust that I've grasped at least some key information." 
    Peter "I hope I can successfully complete this task; otherwise, I'll have to consult with her again." 
    Peter "But... that will be a little bit embarrassing."

    "(Peter hesitates for a moment, then stands up and walks to the window)"

    Peter "Maybe I should go downstairs and ask them to lower the volume, explain that I'm studying?" 
    Peter "Hopefully, they'll understand."

    "(The cacophony from outside becomes even more pronounced, and Peter furrows his brow)"

    Peter "But I don't want to come off as too naggy either." 
    Peter "Perhaps I can try enduring it for a while; after all, parties do eventually come to an end, right?"

    "(Peter sits back at his desk, attempting to refocus)"

    Peter "I hope this party wraps up soon; I need to finish this assignment. Or maybe I should just grab some earplugs to force myself to concentrate." 
    Peter "Life is always full of unexpected surprises."


label week_7_end:
    scene background week
    "The end"



