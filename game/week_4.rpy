


label week_4_debug:
    jump week_4_start

label week_4_start:
    $ current_week = 4
    jump week_4_screen_display

label week_4_screen_display:
    scene background week
    call screen week_4_screen
    jump week_4_dialogue

#Start of the dialogue
label week_4_dialogue:
    scene background school
    
    "Start Week 4"
