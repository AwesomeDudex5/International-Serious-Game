

label week_3_debug:
    jump week_3_start

label week_3_start:
    $ current_week = 3
    if pressure < 5:
        stop music
        play music "BGM.mp3" volume 1.0     
    else:
        stop music
        play music "BGM Room.mp3" volume 1.0
    jump week_3_screen_display

label week_3_screen_display:
    scene background week
    call screen week_3_screen
    jump week_3_wakeup

label week_3_wakeup:
    scene background room
    "A new week has begun."
    show screen pressure_display

menu:
    "Wake Up":
        jump week_3_dialogue
    "Slacking off at home" if pressure >= 5:
        "You've skipped all the classes, how delightful!"
        "Stress ---"
        jump menuintroduction

label alex_name:

menu:
    "H...Ha^x!, I’m doing well...what about you?":
        jump forgot_name_1
    "Sorry, what’s your name again?":
        jump forgot_name_0

label forgot_name_1:
    if language_skill < 3:
        "I'█ dong wel, nd bi the wy...my neme is 'Alex'...you for█ot that?"
    else:
        "I'm doing well, and by the way...my name is 'Alex'...you forgot that?"
    "The atmosphere became awkward, so you and Andy didn't say much"
    $ pressure += 1
    "Stress"
    jump week_3_dialogue_continue

label forgot_name_0:
    if language_skill < 3:
        "Yu don't lie██mber me? Ahh...m█ neme i█ Alex."
    else:
        "You don't remember me? Ahh...my name is Alex."
    "The atmosphere became awkward, so you and Andy didn't say much"
    jump week_3_dialogue_continue

#Start of the dialogue
label week_3_dialogue:
    scene background school
    show alex normal at right
    show peter normal at left
    if alex_information == 0:
        Character("Ha?**x") "Helo Peter, how was your waekend?"
        jump alex_name
    if alex_information == 1:
        Alex "Hello Peter, how was your weekend?"
        Peter "Hello Alex! I’m doing well! What about you?"
        jump week_3_dialogue_2nd_part
    hide peter normal
    hide alex normal

label week_3_dialogue_2nd_part:
menu:
    "I gues you are taking ‘Cross-Cultural Game Communication’ cou█rse right?":
        show alex normal at right
        Alex "Yes! That is the first core course of Game Linguistics. It seems like you still remember my major!"
        jump week_3_dialogue_continue
    "How was your first Sociology class?":
        show alex normal at right
        Alex "What? Ehh… I wasn’t taking that class. I major in Game Linguistics, Human Computer Interaction. Don’t you remember?"
        jump week_3_dialogue_continue


label week_3_dialogue_continue:
    scene background school

    show bill normal at right
    if language_skill < 3:
        Andy "Good Moring guys! We are going do half day off this week! To you have any special plans?"
    else:
        Andy "Good Morning guys! We are going to have a day off this week! Do you have any special plans?"
    show peter normal at left
    Peter "What? We have a day off this week?"
    
    Andy "Yes of course, you didn’t pay attention to the campus news? Come on!"
    
    if language_skill < 3:
        Peter "Ehh, I wes having a had ti█e on my assignments…So I didn’t pay attention to the Email."
    else:
        Peter "Ehh, I was having a hard time on my assignments…So I didn’t pay attention to the Email."
    "Stress + \n(Feeling like missed out on something important)"
    $ pressure += 1
    
    hide andy normal
    show alex normal at right

    if language_skill < 3:
        Alex "Checking mailsnd steying epda█ed with school information is cru█ial; it can help you not mistletoe on important updates."
        Alex "Ef your facing defficulties with your stadies, perhaps I can assist you doo?"
        Alex "I spel█d my weakends stu█ying at di leblery, soif y█ur intested, you can join me."
        Peter "Ehh...ya! Thank you!" 
    else:
        Alex "Checking em█ils end staying updated with sch█ol information is crucial; it can help y█u not miss out on important updates."
        Alex "If you're facing diffic█lties with your studies, perhaps I can assi█t you too?"
        Alex "I sp█nd m█ weekends stud█ing at the lebrary, so if you're int█rested, you can join me."
        Peter "That sounds great! I'll check my weekend schedule when I get back." 
        Peter "If I have the time, I'd be more than willing to study together with you!" 
    Peter "What about you, Andy? What’s your plan for this week?"

   
    hide alex normal
    show bill normal at right
    Andy "Me? I'm planning to unw█nd a bit this week. I'm thinking of going to the Cinema." 
    Andy "However, I'm waiting to go with someone else; it's not as enjoyable alone." 
    Andy "Are you interested? If you're free, you can join as well."
   
    Peter "That also sounds like a good plan…I didn't even know there was a Cinema near our school. And it's also a good way to release the pressure."
    jump week_3_parent_call

label week_3_parent_call:
    scene background room

    "(After talking with your new friends and attending classes, you return back to your room for the day)"
    "(Your dad calls you over the phone)"
    
    Dad "Hello kid! How’s everything going so far? Are you able to keep up with the course work?"

    show peter normal
    Peter "Hi dad."


menu:
    "Everything is doing fine! Yes, I can keep up with the coursework!":
        Dad "Is that so? Well… you better try your best... Almost all of our family's savings are going into your education, it will be tough for us if you can’t graduate."
        jump week_3_parent_call_option_continue
    "Ehh… Not too bad. It’s a little bit hard but I’m trying my best to follow up.":
        Dad "Is that so? Well… you better try your best..." 
        Dad"Almost all of our family's savings are going into your education, it will be tough for us if you can’t graduate."
        jump week_3_parent_call_option_2

label week_3_parent_call_option_2:
    menu:
        "Alright, alright, I get it. No need to repeat it over and over. I'm already under a lot of pressure!":
            Dad "What's with this attitude? Do you know how much our family has sacrificed for your education? You need to show gratitude and appreciate that!"
            "Stress + \n (Lectured by parent)"
            $ pressure += 1
            jump week_3_parent_call_option_continue
        "Yes, Dad, I understand. Don't worry, I won't let you down.":
            Dad "Alright, if you encounter any difficulties, remember to talk to us. We will do our best to help you!"
            "Stress - \n (Encouragement from parent)"
            $ pressure -= 1
            jump week_3_parent_call_option_continue

label week_3_parent_call_option_continue:
    
    Dad "Actually, the reason I called you this time is to assign you a task." 
    Dad "We are currently in the process of applying for your permanent residency card, and I need you to go get a Proof for no criminal record."
    
    show peter normal
    Peter "A what? And where should I go to get this?"
    
    Dad "A Proof for no criminal record? I guess that’s what they call this stuff. I guess you can get it from your school? 
    I’m not sure, you can go talk with them or search on the internet."
    
    Peter "Alright…… I will try my best to handle it as soon as possible."
    
    Dad "Make sure to get on it right away! Go inquire about it this week! We need to have that document within the next 6 weeks!"

label week_3_weekend:
    menu:
        "Cinema with Andy":
            "Stress - - \n (Spending time with friends alleviates stress)"
            $ pressure -= 2
            jump week_3_end
        "Library with Alex":
            "Study +, Language + \n (Studying at library improves your language skills)"
            $ pressure += 1
            $ language_skill += 1
            jump week_3_end
        "Police certificates event" if not finished_police_cert:
            jump police_cert_event_start

label week_3_end:
    jump menuintroduction
           



           




