


label week_5_debug:
    jump week_5_start

label week_5_start:
    $ current_week = 5
    jump week_5_screen_display

label week_5_screen_display:
    scene background week
    call screen week_5_screen
    jump week_5_dialogue

#Start of the dialogue
label week_5_dialogue:
    scene background school
    "(It is midterm week. Peter takes tests for all of his classes)"
    "(The next day, he gets his results...)"
    "(He passes with flying colors)"
    jump week_5_event_start

label week_5_event_start:
    scene background room
    "(During the weekend, Peter felt some discomfort in his stomach)"
    "(What does he do?)"

menu:
    "Self-care. Drink some milk.":
        "Action Point - -   Stress + \n (Stayed home and drank milk. Despite rest, the sickening feeling lingered)"
        $ current_action_points -= 2
        jump week_5_weekend
    "Go to the hospital.":
        "Action Point -" 
        $ current_action_points -= 1
        jump week_5_hospital_start

label week_5_hospital_start:
    scene background hospital
    "(Peter went to the hospital)"

    show receptionist normal at right
    FrontDesk "Hello. How can I help you today?"

    show peter normal at left
    Peter "Good afternoon, today I'm having a sudden, sharp pain in my stomach. And I wish to see a doctor."
    FrontDesk "Sure, do you have an app^5ntment with us?"
    Peter "Appointment? No sorry, I don’t have an appointment. It just started hurting today."
    FrontDesk "Ok, do you want me to make an appointment for you? The earliest available appointment is likely to be n#￥@#h."
    Peter "? ? Sorry what? What time did you say?"
    FrontDesk "The earliest available appointment is likely to be NEXT MONTH, Sir! You can make an appointment first, go home and rest while waiting."
    Peter " Next……MONTH!?"

    hide peter normal
    hide receptionist normal

menu:
    "It's too late for me! I can’t wait until that time.":
        jump week_5_hospital_continue_1

    "Ok…Do you have any recommended medications for relieving stomach pain?":
        jump week_5_hospital_continue_1


label week_5_hospital_continue_1:
    show receptionist normal at right
    FrontDesk "If you feel the situation is urgent, you can go register at the emergency."

    show peter normal at left
    Peter "Hello, I'm here to register at the emergency room."

    hide receptionist normal
    show nurse normal at right
    "(The doctor enters the room)"
    Doctor "Hello, Mr. Peter. I'm Dr. S^#ith. Please tell me about your symptoms and when the stomach pain started."

    Peter "Hello, doctor. The stomach pain began this morning and has been persistent since then. It's quite severe."

    if language_skill > 60:
        Doctor "I understand. Besides the stomach pain, do you have any other discomfort? Any na$#@a, 5omei8ing, or other symptoms?"
    else:
        Doctor "I understand. Besides the sto@@ach pain, do you have any 0yhr dis34ort? Any 7a@#;a, 5$m?t45, or other 6y$#5oms?"

    hide peter normal
    hide nurse normal

menu:   
    "Do you need…my medical history record?":
        Doctor "Sure, let me call in a translator to communicate with you."
        jump week_5_hospital_continue_2
    
    "Some nausea but no vomiting. Also, I feel a bit lightheaded":
        "(A translator enters the room)"
        jump week_5_hospital_continue_2

label week_5_hospital_continue_2:

    show nurse normal at right
    Doctor "Okay, thank you for your description. Based on your symptoms, it's likely a dia@$12#sis of G10_!#@$m(Gastrospasm)."
    Doctor "We'll administer Ωaod1m? Bi#@$te (Sodium Bicarbonate) to you first and wait for a while to see if the situation improves."

    hide nurse normal
    show random person
    Translator "The doctor believes you may be experiencing Gastrospasm. He will prescribe Sodium Bicarbonate for you, which should provide some relief."

    show peter normal at left
    Peter "Sodium Bicarbonate?"

    Translator "It can neutralize stomach acid and relieve Gastrospasm. Ah, it is similar to baking soda."

    Peter "Ohh, ok, ok. Thank you, doctor."

    jump week_5_hospital_end

label week_5_hospital_end:
    hide peter normal
    hide nurse normal
    hide random person
    "(After his talk with the doctor, Peter returns home)"



label week_5_weekend:
    scene background room
    "(It is the weekend)"
    "(How do you spend your time)"

menu:
    "Self Study":
        "Study + n\ (Gained knowledge)"
        $ study += 1
    "Study with Andy & Alex":
        "Study ++, Language + \n (Studying with friends improve language proficiency)"
        $ study += 1
        $ language_skill += 1
    "Police certificates event":
        "(Peter goes to the police office to get his international certification)"
        jump police_cert_event_start
    "Hang out":
        "Stress - - \n (Hanging with friends and chilling can alleviate stress)"
        $ pressure -= 2

label week_5_end:
    "(Weekend is over)"

    #Game Over check
    #Mak and Li, add this code to places where it needs to go
    if pressure >= max_pressure:
        jump game_over_screen

    jump week_6_start

