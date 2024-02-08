
label week_2_start:
    jump week_2_screen_display

label week_2_screen_display:
    scene background 1
    call screen week_2_screen
    jump week_2_dialogue


#Start of the dialogue
label week_2_dialogue:
    scene background 1
    "(School has officially started)"
