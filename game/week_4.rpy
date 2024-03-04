


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
    
    show teacher normal at right
    Instructor "Good morning, everyone! Today, I will introduce you to some knowledge related to M#$5c c^$@#."
    Instructor "I hope you can all keep up because this is crucial to our topic today."

    show student1 normal at left
    Student1 "M#$5c c^$@#? What's that?"

    Instructor "A M#$5c c^$@# is an important concept in game design. Simply put, it's a specific area where players may encounter various special game rules or events."
    Instructor "We use the term M#$5c c^$@# to describe the specific space where a game occurs."
    Instructor "This boundary is separate from what we call 'real life' in terms of both time and space."

    hide student1 normal
    show student2 normal at left
    Student2 "That sounds interesting! Can you give an example?"

    Instructor "Certainly."

    hide teacher normal
    hide student2 normal
    "(The students attend their classes for the rest of the day.)"
    "(In several hours, the classes have come to an end for the week)"

    Instructor "Alright, it's about time, I hope everyone has an enjoyable weekend. "
    Instructor "Also, a reminder that next week will be #$#d@ week."
    Instructor "There won't be class this Friday, so please take this time to review and prepare well."

menu:
    "Option 1: Talk with Instructor":
        "Study ++  Stress ++ \n (Muster up courage to talk with instructor to get more information)"
        $ pressure += 2
        $ study += 2
        jump week_4_menu_choice_inquire
    "Option 2: Talk with classmates":
        "Study +  Stress + \n (Talking with classmates can be stressful at first, but you learn more about them)"
        $ pressure += 1
        $ study += 1
        jump week_4_menu_choice_inquire
    "Option 3: Go home":
        "Stress - - (No better place like home to rest and relax)"
        $ pressure -= 2
        jump week_4_menu_choice_go_home

label week_4_menu_choice_inquire:
    "(What does Peter talk about?)"
    menu:
        "Inquire about Study related questions.":
            "(Discussed the concept of the magic circle that was taught in class)"
        "Chit-chat about daily anecdotes.":
            "Language +, Stress - \n (Getting comfortable talking with classmates)"
    
    menu: 
        "Inquire about Schedule related questions.":
            "(Discussed about midterms and that there are no classes on Friday)"
        "Chit-chat about daily anecdotes.":
            "Language +, Stress - \n (Getting comfortable talking with classmates)"

    show peter normal
    Peter "I guess I should get going now."
    jump week_4_menu_choice_go_home
        


label week_4_menu_choice_go_home:
    scene background room
    "(Time to do homework. Choose the correct answer)"

label week_4_homework_question_1:
    "What’s today’s topic?"

menu:
    "1. Mystic Castle":
        "That's not correct."
        jump week_4_homework_question_1

    "2. Magical World":
        "That's not correct."
        jump week_4_homework_question_1

    "3. Minecraft":
        "That's not correct."
        jump week_4_homework_question_1

    "4. Magical Circle":
        "That is correct!"
        jump week_4_homework_question_2

label week_4_homework_question_2:
    "What’s the event for next week?"

menu:
    "1. Holiday":
        "That's not correct."
        jump week_4_homework_question_2

    "2. Spring Break":
        "That's not correct."
        jump week_4_homework_question_2

    "3. Midterm":
        "That is correct."
        jump week_4_homework_question_3

    "4. Summer Break":
        "That's not correct."
        jump week_4_homework_question_2

label week_4_homework_question_3:
    "Did the Instructor mention anything about this week's schedule?"

menu:
    "1. Classes will proceed as usual on Tuesday.":
        "That's not correct."
        jump week_4_homework_question_3

    "2. No class on Wednesday":
        "That's not correct."
        jump week_4_homework_question_3

    "3. No class on Friday":
        "That is correct."
        jump week_4_weekend

    "4. Semester is over":
        "That's not correct."
        jump week_4_homework_question_3

label week_4_weekend:
    "(It is the weekend)"
    "(How does Peter spend time?)"

menu:
    "Self Study":
        "Study ++ \n (Studied for midterms)"

    "Study with Andy & Alex":
        "Study +  Language + \n (Studying with friends helps one get better with the language)"

    "Police certificates event":
        "(Peter decides to get certification for international students)"
        jump police_cert_event_start

    "Hang out with friends":
        "Stress - - \n (Spending time with friends is always a good way to relieve stress)"

label week_4_end:
    "(Weekend is over)"
    jump week_5_start



