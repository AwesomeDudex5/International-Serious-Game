

label week_2_debug:
    jump week_2_start

label week_2_start:
    $ current_week = 2
    jump week_2_screen_display

label week_2_screen_display:
    scene background week
    call screen week_2_screen
    jump week_2_dialogue


#Start of the dialogue
label week_2_dialogue:
    scene background room
    "(School has officially started)"

menu:
    "Wake Up":
        jump week_2_continue
    "Struggle Out of Bed":
        jump week_2_continue
      
label week_2_continue:

    scene background school
    show teacher normal
    Instructor "Welcome to Ga$# !@si;0, My name is Fr1@#’,Today we are going to do a quick overview of this course, but before that,  let’s get to know the people around you!"

    hide teacher normal
    show alex normal at right
    Character("???") "Hello! My name is A**x, and my major is Hu*** C****** #$@."

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
    Alex "Hmm? Sure..?My name is Al*x?, I major in Hu**n Com**** In……"

    show peter normal at left
    Peter "Uhh…can you…write it down?"

    hide peter normal
    hide alex normal
    
    "Stress +, Language+, \n (Stress from awkwardly asking to write their name) \n (Learned more about the person and associated text)"
    jump week_2_continue_1


label week_2_menu_1_choice_2:
    show peter normal at left
    Peter "Uhh….Hello! I’m Peter! My major is xxx."
    jump week_2_continue_1
    

label week_2_continue_1:
    show teacher normal
    Instructor "Alright, it seems like everyone has become acquainted. Let's begin by getting to know more about the course. There are a total of #@$$ 
    assignments in this semester, with each one due on &&****. And this week we will mainly focus on the de#$$$%%g#!@."

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
        jump week_2_continue_2
    "Gaming at home":
        "Stress - - \n (While not productive, it is a great stress relievers)"
        jump week_2_continue_2
    "Hang out":
        "Stress - - -, Money - \n (Great way to destress but it also cost money)"
        jump week_2_continue_2


#--------------Restaurant Scene
label week_2_restaurant_option:
    scene background restaurant
    "(Peter walks to a local restaurant)"

    show random person at right
    Character("Waiter") "Hello, just for one?"
    
    show peter normal at left
    Peter "Yes."

    Character("Waiter") "Okay,please have a seat, this is the menu."

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
    Peter "Sorry, do you have a menu in *mother language*?"
    
    show random person at right
    Character("Waiter") "Of course! Let me get it for you, please wait a moment."

    hide peter normal
    hide random person
    "(Some time later...)"

    "(The waiter returns with the menu and hands it to Peter.)"

    show random person at right
    Character("Ms. Chen") "Hello dear. I'm the owner of this restaurant. You can call me Ms. Chen. This is the menu in *mother language*. By the way… are you from *Home Town*?"
   
    show peter normal at left
    Peter "Yes, ma'am. How did you know?"
    
    Character("Ms. Chen") "Oh, I could definitely tell! Our hometown is also from there! It's been ages since I
    met a fellow villager! Come, come, what would you like to eat? Our dishes are truly authentic! 
    By the way, dear, are you a student here? How long have you been here?..."

    "(Peter enjoys his meal while conversing with the restaurant owner)"

    "Stress - \n (Good food relaxes the mind)"

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
    jump week_2_homework_2

label week_2_homework_1_incorrect:
    "Thats wrong"
    jump week_2_homework_1

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
    jump week_2_homework_3

label week_2_homework_2_incorrect:
    "Thats wrong"
    jump week_2_homework_2

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
    jump week_2_homework_4

label week_2_homework_3_incorrect:
    "Thats wrong"
    jump week_2_homework_3


# Question 4
label week_2_homework_4:
    "What’s the due date?"

menu:
    "Feb 1st ":
        jump week_2_homework_4_incorrect
    "Festival ":
        jump week_2_homework_4_incorrect
    "Fridays":
        jump week_2_homework_4_correct

label week_2_homework_4_correct:
    "That's correct"
    jump week_2_end

label week_2_homework_4_incorrect:
    "Thats wrong"
    jump week_2_homework_4


label week_2_end:
    "(Homework is finished)"
    jump week_3_start