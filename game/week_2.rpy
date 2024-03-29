
default alex_information = 0

label week_2_debug:
    jump week_2_start

label week_2_start:
    $ current_week = 2
    if pressure < 5:
        stop music
        play music "BGM.mp3" volume 1.0     
    else:
        stop music
        play music "BGM Room.mp3" volume 1.0
    jump week_2_screen_display

label week_2_screen_display:
    scene background week
    call screen week_2_screen
    jump week_2_dialogue


#Start of the dialogue
label week_2_dialogue:
    scene background room
    "(School has officially started)"
    show screen pressure_display

menu:
    "Wake Up":
        jump week_2_continue
    "Slacking off at home" if pressure >= 6:
        "You've skipped all the classes, how delightful!"
        "Stress ---"
        jump menuintroduction

label week_2_continue:

    scene background school
    show teacher normal
    if language_skill < 3:
        Instructor "Welcome to Huk█# !@si;0, My name is █r1@#,To█ay we are going to do a queck overview of this course, but before that, let’s get to know the pea-pull a-rownd yew!"
    else:
        Instructor "Welcome to Go█ho! Sh^ h@me, My name is Fr1@#,Today we are going to do a quick overview of this course, but before that, let’s get to know the people around you!"
    hide teacher normal

    show alex normal at right
    if language_skill < 3:
        Character("???") "Hello! Mi neme es H-?l**, ad mi mejor is He*e in* #$@. "
    else:
        Character("???") "Hello! My name is Ha?**x, and my major is G@me Ii-Gu█st. (Game Linguist)"

    show peter normal at left
    Peter "Oh um..."

    hide peter normal
    hide alex normal

menu:
    "Sorry? Can you repeat that?":
        "Stress + \n (Anxiety from asking to repeat one's self)"
        $ pressure += 1
        jump week_2_menu_1_choice_1
    "Keep going to introduce yourself.":
        jump week_2_menu_1_choice_2

label week_2_menu_1_choice_1:

    show alex normal at right
    Character("Ha?**x?") "Hmm? Sure..?My name is il*x?, I major in G@me IinGu█st "

    show peter normal at left
    Peter "Uhh…can you…write it down?"
    $ alex_information = 1

    hide peter normal
    hide alex normal
    
    "Stress +, Language+, \n (Stress from awkwardly asking to write their name) \n (Learned more about the person and associated text)"
    $ pressure += 1
    $ language_skill += 1
    jump week_2_continue_1


label week_2_menu_1_choice_2:
    show peter normal at left
    Peter "Uhh….Hello! I'm Peter! My m█jor is N0t Sereous? Game!"
    jump week_2_continue_1
    

label week_2_continue_1:
    show teacher normal
    if language_skill < 3:
        Instructor "Alright, it sems bike everl█one hes become acquainted. Lets bi█n by g██et█ to know more about the co█rse. "
        Instructor "Th█e ar e t█al of ?x as██gn█ments in tis sem█ster, wth ech o█e tue on ph█ei. And thes w█ek we will main█y focus on ██."
    else:
        Instructor "Alright, it seems like everyone has bicome ac█uai█ted. Let's begin by get█ing to k█w more ab███ the cou███e.  "
        Instructor "Ther are a total of thkx a█ssi█nm█nts in this seme█er, with each one due on Fre██ t. And this week we will mainly focus on the Hem ██te TeSin."
    hide teacher normal
    "Classes went on for the week. Peter always made it to lectures each day."
    jump week_2_weekend

label week_2_weekend:
        scene background room
        "It is now the weekend."
        "Where do you decide to go? How do you spend your time?"

#-------------- WEEKEND -----------------
menu:
    "Restaurant":
        jump week_2_restaurant_option
    "Talk with Instructor":
        "Stress +, Language skill +, Study + \n (Anxiety from approaching the teacher, but got comfortable talking with him and gained knowledge)"
        $ pressure += 1
        $ language_skill += 1
        $ study += 1
        jump week_2_continue_2
    "Gaming at home":
        "Stress - - \n (While not productive, it is a great stress relievers)"
        $ pressure -= 2
        jump week_2_continue_2
    "Hang out":
        "Stress - - -, Money - \n (Great way to destress but it also cost money)"
        $ pressure -= 3
        $ money -= 1
        jump week_2_continue_2


#--------------Restaurant Scene
label week_2_restaurant_option:
    scene background restaurant
    "(Peter walks to a local restaurant)"

    show random person at right
    if language_skill < 3:
        Character("Waiter") "Helo, jus█ for ne?"
    else:
        Character("Waiter") "Hello, just for one?"
    
    show peter normal at left
    Peter "Yes."

    Character("Waiter") "Okay,plea█se ha█e a s█at, this is the █enu."

    hide random person
    hide peter normal

menu:
    "1. Sp!cy Szechuan Ch!cken":
        jump week_2_restaurant_option_continue
    "2. M!so-Glazed S!lm0n w!th Was@b! P!reé":
        jump week_2_restaurant_option_continue
    "3. Ch@rr0ed V3get@bles w!th T3r!y@k! S@uce":
        jump week_2_restaurant_option_continue
    "4. Qü!n0@ F®ied R1ce w!th P!ne@ppl3 and Shrimp":
        jump week_2_restaurant_option_continue
    "5. C@ramel!zed M@ngo-Chil! Ch0col@te C@ke":
        jump week_2_restaurant_option_continue

label week_2_restaurant_option_continue:

    show peter normal at left
    Peter "Sorry, to you have a menu in *mother language*?"
    
    show random person at right
    Character("Waiter") "Of course! Let me get it for you, please wait a moment."

    hide peter normal
    hide random person
    "(Some time later...)"

    "(The waiter returns with the menu and hands it to Peter.)"

    show random person at right
    Character("Ms. Chen") "Hello dear. I'm the owner of this restaurant. You can call me Ms. Chen." 
    Character("Ms. Chen") "This is the menu in *mother language*. By the way… are you from *Home Town*?"
   
    show peter normal at left
    Peter "Yes, ma'am. How did you know?"
    
    Character("Ms. Chen") "Oh, I could definitely tell! Our hometown is also from there!" 
    Character("Ms. Chen") "It's been ages since I met a fellow villager! Come, come, what would you like to eat? Our dishes are truly authentic!" 
    Character("Ms. Chen") "By the way, dear, are you a student here? How long have you been here?..."

    "(Peter enjoys his meal while conversing with the restaurant owner)"

    "Stress - \n (Good food relaxes the mind)"
    $ pressure -= 1

    jump week_2_continue_2



label week_2_continue_2:
    scene background room
    "Time do homework"

# ----------- Homework Puzzle -----------------

# Question 1
label week_2_homework_1:
    "What course did you take this week?"

menu:
    "Game Art and Design":
        jump week_2_homework_1_correct
    "Game Theorem":
        jump week_2_homework_1_incorrect
    "Geography":
        jump week_2_homework_1_incorrect

label week_2_homework_1_correct:
    "That's correct"
    "Grade increase"
    $ study += 1
    jump week_2_homework_2

label week_2_homework_1_incorrect:
    "Thats wrong"
    jump week_2_homework_2

# Question 2
label week_2_homework_2:
    "What’s the topic for this week’s class?"

menu:
    "Definition of Geography":
        jump week_2_homework_2_incorrect
    "Developer Guide":
        jump week_2_homework_2_incorrect
    "Definitions of Game":
        jump week_2_homework_2_correct

label week_2_homework_2_correct:
    "That's correct"
    "Grade increase"
    $ study += 1
    jump week_2_homework_3

label week_2_homework_2_incorrect:
    "Thats wrong"
    jump week_2_homework_3

# Question 3
label week_2_homework_3:
    "How many assignments?"

menu:
    "Ten ":
        jump week_2_homework_3_incorrect
    "Six":
        jump week_2_homework_3_correct
    "Eight":
        jump week_2_homework_3_incorrect

label week_2_homework_3_correct:
    "That's correct"
    "Grade increase"
    $ study += 1
    jump week_2_homework_4

label week_2_homework_3_incorrect:
    "Thats wrong"
    jump week_2_homework_4


# Question 4
label week_2_homework_4:
    "What’s the due date?"

menu:
    "Feb 31st ":
        jump week_2_homework_4_correct
    "Festival ":
        jump week_2_homework_4_incorrect
    "Fridays":
        jump week_2_homework_4_incorrect

label week_2_homework_4_correct:
    "That's correct"
    "Grade increase"
    $ study += 1
    jump menuintroduction

label week_2_homework_4_incorrect:
    "Thats wrong"
    jump menuintroduction


label week_2_end:
    "(Homework is finished)"
    $ weekend_map_start = True
    jump menuintroduction