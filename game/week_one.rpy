 


#---VARIABLES---
define Peter = Character("Peter", color="68a24b")
define Bill = Character("Andy", color="#4397fa")
define Andy = Character("Andy", color="#4397fa")
define Alex = Character("Alex", color="#d45e27")
define Mom = Character("Mom", color="#e011be" )
define Dad = Character("Dad", color="#331b9e")
define Seraphina = Character("Seraphina", color="#331b9e")
define Instructor = Character("Instructor", color= "#830950")
define Student1 = Character("Student", color="#af8c18")
define Student2 = Character("Student", color="#af8c18")
define Officer = Character("Cop", color="#5a17b1")
define Homeless = Character("Homeless", color="#1ba026")
define Nurse = Character("Nurse", color="#db179a")
define Doctor = Character("Doctor", color="#db179a")
define Translator = Character("Doctor", color="#777777")
define MaleStore = Character("Store Staff", color="#9b6513")
define FemaleStore = Character("Store Staff", color="#af8c18")
define Racist = Character("Racist Person", color="#e01f1f")
define FrontDesk = Character("Front Desk Receptionist", color="#3aa743")
define RandomPerson = Character("Random Person", color="#af8c18")

#----Stats------
default pressure = 0
default max_pressure = 20
default max_action_points = 50
default current_action_points = 50
default study = 0
default language_skill = 50
default money = 100

$ unknown_word_color = "#e71c1c" #red
default finished_police_cert = False
default police_cert_part_1 = False
default police_cert_part_2 = False

default current_week = 1

label start:
    #For debugging, uncomment the line below with the week you want to debug
    #jump week_7_debug

    jump week_1_screen_display

label week_1_screen_display:
    $ current_week = 1
    scene background week
    call screen week_1_screen
    jump week_1_start


#Start of the dialogue
label week_1_start:
    scene background school
    show peter normal
    show screen pressure_display
    Peter "Wow, this is our school, it’s soo big! It took me ages to find my dorm!" 
    Peter "I remember Andy should be around here... uhh, kinda struggling to make sense of this map."
    Peter "Hello, excuse me, how do I get to this location?"
 
    hide peter normal
    show student1 normal
    Character("Stranger") "Oh! Go straight ahead, take a left, pass by @!#, then make a right, 
    and you'll see #!, There will be a sign for Bu***g 7 right above the entrance, you can't miss it!"

    hide student1 normal
    show peter normal
    Peter "Uhhh..."

    hide peter normal

menu:
    "Excuse Me?": 
        jump week_1_continue
    "Ok....":
        "pressure+ \n (Pressure from uncertainty)"
        $ pressure += 1
        jump week_1_continue

label week_1_continue:
    show peter normal at left
    Peter "Hey, Andy! You're finally here. I've been waiting for you at the school gate for a while."

    show bill normal at right
    Andy "Oh, thank goodness you're here, Peter! Long time no see!"

    hide peter normal
    show mom normal at left
    Mom "Hello Andy! Long time no see. You look very energetic!"

    Andy "Hello Mr. X and Mr. X! Yeah, it's been ages! You haven't been here for long, have you? How's it going?"

    show peter normal at left
    hide mom normal
    Peter "Uhh... hard to say. I didn't realize how rusty my language skills were until I landed."

    Andy "Haha, I can relate to that too. It should just take some time to adapt, I guess. It varies from person to person. Let me help you carry these things up!"

    Peter "Thank you!"

    "(An hour later...)"

    Andy "So, have you already toured the entire campus?"

    Peter "Well, I'm still getting used to it. This campus is really huge, with so many buildings and places to remember."

    Andy "Totally get it. You know, let me give you a quick overview of each area."

    hide peter normal
    hide bill normal
    show sample map:
        xalign 0.5 yalign 0.5

    Andy "Over there is the main academic building where most of our classes are held(For Study event)." 
    Andy "The library, like you mentioned, is a great spot for studying(For study event with classmates)."
    Andy "Oh, and the cafeteria is just a short walk from here(For social event with classmates)."

    hide sample map
    show peter normal at left
    Peter "Thanks, Andy! It's helpful to have a guide. Anything else I should know about?"
    jump week_1_gym_scene

label week_1_gym_scene:
    scene background gym

    show bill normal at right
    Andy "Of course! There's the sports complex where you can hit the gym or join recreational activities." 
    Andy "And if you ever need assistance, the student services office is in the administration building." 
    Andy "They're really helpful with any questions you might have."

    show peter normal at left
    Peter "Appreciate it, Andy! I'm sure with your guidance, I'll navigate this campus in no time."

    Andy "Also... um... I'm not sure if you're picky about food, but you might want to give the local cuisine a try." 
    Andy "Personally, I think I still prefer the flavors from my hometown. If you find it hard to adjust, you can go to this restaurant here." 
    Andy "It's quite similar to our hometown taste."

    Peter "Oh, got it! At least in the past couple of days, my parents are having a hard time adjusting to the local food here." 
    Peter "My father even seems to be experiencing some stomach issues. I'll go there tomorrow. My parents need to have some hometown flavors to ease their discomfort."

    Andy "Exactly, Peter! It's called 'Home Flavors,' it’s actually outside the campus, at this location. You should check it out sometime."

    Peter "Thanks, Andy! I appreciate the tip. I'll definitely give it a try if I need something familiar."

    Andy "Alright, I hope it was helpful for you. I've also scheduled an appointment with an advisor. I've got to go now!"

    Peter "Ok, See you later!"
    jump week_1_store_event


label week_1_store_event:
    scene background store

    "(Peter's parents decided to help him settle into his new place, so they headed to the supermarket.)"

    show mom normal at right
    Mom "Peter, What do these classifications mean? I can't read the labels here. Which of these milks is better?"

    show peter normal at left
    Peter "The labels mean... uh, whole milk and semi-skimmed milk." 
    Peter "I'm not sure which one is better, we usually don't pay much attention to this back home."

    Mom "Hello? Do you have...(talking with a supermarket staff)"
    Mom "Peter, can you ask if they have Pasteurized Eggs? I'm not sure how to say Pasteurized Eggs in this language."

    Peter "Ah, of course....Um... do you have...."

menu:
    "do you have...eggs.....without.....bacteria?": 
        "stress+ \n (Talking to strangers while being awkward)"
        $ pressure += 1
        jump week_1_continue_continue
    "(Look up how to say 'Pasteurized Eggs' online.)":
        show mom normal
        Mom "Hurry up!"
        "stress++ \n (Anxiety from time and external pressures)"
        $ pressure += 2
        jump week_1_continue_continue
    "raw-eating eggs?":
        jump week_1_continue_continue

label week_1_continue_continue:
    scene background store

    show male owner at right
    Character("Super Market Staff") "The….ohh, you mean P******ed Eggs, right?"

    show peter normal at left
    Peter "The ... .what? Uhh…Yes? Maybe?"

    show male owner at right
    Character("Super Market Staff") "It’s ok, let me show you. This way!"

    hide male owner
    show mom normal at right
    Mom "Great! Still relying on you! Your Language Skill is really good! What's that word called?"

    show peter normal
    Peter "Uhh..."

    hide peter normal
    hide mom normal
    hide male owner
    
menu:
    "'Pesterized?' Eggs, Mom!":
        show mom normal at right
        Mom "Awesome, learned a new word!"
        "stress+ \n (Lying to your mom)"
        $ pressure += 1
        jump week_1_event_2
    "I don't know mom... I didn't hear clearly":
        show mom normal at right
        Mom "Ah? Haven't you already passed language exams? Is he leading us to the right 
        place? Is it what we're looking for? You need to clarify!"
        "stress++ \n (Emotional Damage)"
        $ pressure += 2
        jump week_1_event_2
    "It’s ok mom, it’s just Raw-eating eggs, they can understand it.":
        jump week_1_event_2

label week_1_event_2:
    scene background room
    "(The next day)"

    show dad normal at right
    Dad "Have you checked the requirements for your major? Do you need a project or paper to graduate? What courses has the school scheduled for you this semester?"

    show peter normal at left
    Peter "My major doesn’t require a project or paper to graduate dad. It’s different from our country. And the school doesn’t schedule courses for us, we need to select classes."

    Dad "What? That sounds weird. Are you sure? And what class did you select?"

    hide peter normal
    hide dad normal

menu:
    "Spend time to learn the major requirement, see the hidden information, select the right courses.":
        "Action Point - -, Study ++, Language Skill +, stress + \n 
        (Researched and well informed, getting comfrotable reading another language)"
        $ current_action_points -= 1
        $ study += 2
        $ language_skill += 1
        $ pressure += 1
        jump menuintroduction
    "Talk with your major advisor":
        "Action Point -, Study +, Language Skill + \n
        (Gain more insight about your major)"
        $ current_action_points -= 1
        $ study += 1
        $language_skill += 1
        jump menuintroduction
    "Ignore it.":
        jump menuintroduction

label menuintroduction:
    scene background room
    show dad normal at right
    Dad "Do you want to go out and realaxing"
    call screen mapPopoUp


