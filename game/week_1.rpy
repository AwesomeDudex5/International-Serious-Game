

label week_1:

    scene background 1
    play music "audio/Liyue.mp3"

    show peter normal
    p "This is week 2"

    show peter rich
    p "My current pressure is: [pressure]"
    p "I wonder what game I should play next?"

menu:
    "Blue Archive: Add Pressure": 
        $ pressure += 1
        jump choice_one
    "Palworld: Minus Pressure":
        $ pressure -= 1
        jump choice_two

label choice_one:
    show peter normal
    p "I played Blue Archive"
    p "My Pressure is: [pressure]"

label choice_two:
    show peter rich
    p "I played Palworld"
    p "My pressure is: [pressure]"

return

