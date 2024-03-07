


label week_6_debug:
    jump week_6_start

label week_6_start:
    $ current_week = 6
    jump week_6_screen_display

label week_6_screen_display:
    scene background week
    call screen week_6_screen
    jump week_6_wakeup

label week_6_wakeup:
    scene background room
    "A new week has begun."
    show screen pressure_display

menu:
    "Wake Up":
        jump week_6_dialogue
    "Slacking off at home" if pressure >= 4:
        "You've skipped all the classes, how delightful!"
        "Stress ---"
        jump menuintroduction

define can_go_on_trip = 1

#Start of the dialogue
label week_6_dialogue:
    scene background school

    "(Peter attends class as usual. He has grown accustomed to his schedule)"
    show teacher normal
    Instructor "Alright, it's about time, I hope everyone has an enjoyable weekend."

    hide teacher normal
    "（After Class）"
    
    show student1 normal
    if(language_skill < 65):
        Student1 "Uv yu T#rd? Dhi n!e$bai nas$nal park h@z disk*untid tikkits for dhi nekst fyu deiz, @nd dhi wedher hæz bin gret leitli." 
        Student1 "S4ud wi plan a fi&@d trep dhis wik&#d?" 
    else:
        Student1 "Uv yu hurd? Dhi n!erbai nashunal park h@z disk*untid tikkits for dhi nekst fyu deiz, @nd dhi wedher hæz bin gret leitli."
        Student1 "Shud wi plan a fiyld trip dhis wikénd?"
    
    hide student1 normal
    show alex normal
    Alex "Oh, realli? Sounds grait! Ai don't hav eniθing speshal planned dhis wikénd. Okay, Ai'm in!"

    hide alex normal
    hide student1 normal
    hide peter normal

menu:
    "I can't quite make out what they're saying...":
        "It might be embarrassing to join their conversation" 
        "… I think I'll just head home." 
        "Stress - \n (avoided conversation and relaxed at home)"
        $ pressure -= 1
        $ can_go_on_trip = 0
        jump week_6_weekend

    "Join the conversation":
        jump week_6_join_conversation_1

label week_6_join_conversation_1:
    scene background school
    
    show peter normal at left
    Peter "Hey guys, what are you talking about?"

    show student1 normal at right
    Student1 "We're planning to organize a field trip for the weekend because there's a discount on tickets for the nearby national park."
    "She seems to have a bit of an accent; you find it challenging to understand."

    hide peter normal
    hide student1 normal

menu:
    "(Glancing at Andy, seeking assistance.)":
        show bill normal at right
        Andy "Ah, do you have time this weekend?" 
        Andy "We're planning a trip this weekend, there's a discount on tickets for the nearby national park."
        jump week_6_join_conversation_2

    "Ehh…Sorry? You said that you are planning to do something this weekend?":
        show student1 normal at right
        Student1 "Yes, we are planning to visit the national park."
        jump week_6_join_conversation_2

    "That sounds great! Wish you have a great weekend!":
        "(After wishing them a fun trip, you part from the conversation)"
        $ can_go_on_trip = 0
        jump week_6_weekend
        
label week_6_join_conversation_2:

    hide alex normal
    hide student1 normal

    show peter normal at left
    Peter "That sounds great, can I join?"
    
    show student1 normal at right
    Student1 "Ehh…what do you guys think? Do we still have space in the car?"

    hide student1 normal
    show bill normal at right
    Andy "Yes, there is. If not, I can also drive my car."

    hide bill normal
    show student2 normal at right
    Student2 "Great! Then we will see each other this weekend!"
    jump week_6_weekend

label week_6_weekend:
    scene background room
    "(It is the weekend)"
    "(How does Peter spend his time)"

menu:
    "Self Study":
        "Study + + \n (Studied up on class material to gain knowledge)"
        $ study += 2
        jump week_6_end

    "Cinema":
        "Stress - - \n (Going out and watching the latest movie helps destress)"
        $ pressure -= 2
        jump week_6_end

    "Police certificates event":
        "(Peter decides to get Dertification of Criminal Record from the police department)"
        jump police_cert_event_start

    "Try to cook":
        "(Attempted to try new recipes)"
        "Stress - \n (Cooking is relaxing, plus good food)"
        $ pressure -= 1
        jump week_6_end

    "Field trip with classmates" if can_go_on_trip == 1:
        "(Went with Alex and others on a weekend field trip)"
        "Stress - , Language + \n (Spending time with others is fun, also a good chance to get comfortable conversing)"
        $ pressure -= 1
        $ language_skill += 1
        jump week_6_end

label week_6_end:
    "(Weekend has ended)"
    jump menuintroduction