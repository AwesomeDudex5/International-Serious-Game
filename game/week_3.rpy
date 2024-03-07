

label week_3_debug:
    jump week_3_start

label week_3_start:
    $ current_week = 3
    jump week_3_screen_display

label week_3_screen_display:
    scene background week
    call screen week_3_screen
    jump week_3_dialogue


#Start of the dialogue
label week_3_dialogue:
    scene background school
    
    show alex normal at right
    Alex "Hello Peter, how was your weekend?"

    show peter normal at left
    Peter "Hello Alex! I’m doing well! What about you?"

    hide peter normal
    hide alex normal

menu:
    "I guess you are taking The Foundations of UX Design course right?":
        show alex normal at right
        Alex "Yes! That is the first core course of HCI. It seems like you still remember my major!"
        jump week_3_dialogue_continue
    "How was your first Sociology class?":
        show alex normal at right
        Alex "What? Ehh… I wasn’t taking that class. I major in HCI, Human Computer Interaction. Don’t you remember?"
        jump week_3_dialogue_continue

label week_3_dialogue_continue:
    scene background school

    show bill normal at right
    Andy "Good Morning guys! We are going to have a day off this week! Do you have any special plans?"
    
    show peter normal at left
    Peter "What? We have a day off this week?"
    
    Andy "Yes of course, you didn’t pay attention to the campus news? Come on!"
    
    Peter "Ehh, I was having a hard time on my assignments…So I didn’t pay attention to the Email."
    
    "Stress + \n(Feeling like they missed out on something important)"
    $ pressure += 1
    
    hide andy normal
    show alex normal at right
   
    Alex "Checking emails and staying updated with school information is crucial; it can help you not miss out on important updates."
    Alex "If you're facing difficulties with your studies, perhaps I can assist you too?"
    Alex "I spend my weekends studying at the library, so if you're interested, you can join me."
   
    Peter "That sounds great! I'll check my weekend schedule when I get back." 
    Peter "If I have the time, I'd be more than willing to study together with you!" 
    Peter "What about you, Andy? What’s your plan for this week?"
   
    hide alex normal
    show bill normal at right
    Andy "Me? I'm planning to unwind a bit this week. I'm thinking of going to the Cinema." 
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
            $ language_skills += 1
            jump week_3_end
        "Police certificates event" if not finished_police_cert:
            jump police_cert_event_start

label week_3_end:
    jump menuintroduction
           



           




