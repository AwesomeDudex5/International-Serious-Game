

label police_cert_event_start:
    #UNCOMMENT TO CHECK FOR DEBUG
    #"starting police cert event, check police parts and jump to right parts"

    if start_police_cert == False:
        "No reason to be here yet"
        jump move_to_next_chapter

    if not police_cert_part_1:
        jump police_cert_event_part_1
    if not police_cert_part_2:
        jump police_cert_event_part_2


label police_cert_event_part_1:
    scene background school
    
    "Peter went to inquire at the School Police Department"

    show peter normal at left
    Peter "Hello Sir."

    show cop normal at right
    Officer "Hello, how can I help you?"
    
    Peter "I'd like to find out how to obtain a Certificate of No Cr***** Record. I'm an international student and have no clue about the process."
    
    Officer "Sorry, can you repeat that?"
    
    Peter "A... Proof for no criminal record?"
    
    Officer "Got you. Ok, we can issue that for you. Do you have these required documents with you?"
    
    Peter "Yes, I have them with me, here you are."
    
    Officer "Ok thank you. The processing will take approximately two days, and then you can come here to collect it."
    
    Peter "Thank you officer, have a good day!"

label police_cert_event_part_1_end:
    scene background room
    "(After Peter's trip to the police department, Peter returns to his room)"
    
    show peter normal at left
    Peter "By the way, Dad, I sent you the document for the Certificate of No Criminal Record. Did you see it?"
    
    show dad normal at right
    Dad "Oh, right, I was just about to tell you. I've checked with the agency, and it seems this document won't suffice. It's issued by your school, and it's not formal enough. We might need to obtain the document from the City, or County Police Department."

    
    #-----Set Police Cert Var
    $ police_cert_part_1 = True
    jump move_to_next_chapter


label police_cert_event_part_2:
    scene background store
    "Peter went to the inquire at the County Police Department this time."

    show peter normal at left
    Peter "Hello Sir, Good afternoon. I'd like to inquire if the processing of the Proof for no cr&@&@ record is done here?"
   
    show cop normal at right
    Officer "I'm sorry, could you ask that again? You said you need something?"
    Peter "It‘s, uhh…Proof for no crimi￥al record? Or Certificate of No Cr%^$al Record?"
    Officer "Oh I see, I guess you mean a Cle$%^nce 2e#$er."
    Peter "Ehh..Sorry can you repeat that?"
    Officer "Sure, You are looking for a Cl@&^nce Le#ter."

    hide peter normal
    hide cop normal

menu:
    "Ok…ya I guess that’s what I need…":
        "(Peter goes through the motions)"
        jump police_cert_event_part_2_option_1

    "(Double Check the Information)":
        jump police_cert_event_part_2_option_2


label police_cert_event_part_2_option_1:
    scene background room
    "(Peter returns back to his room and calls his dad)"

    Dad "I have received your document, but it's still not right this time. 
    You need to inquire more, don't be afraid to communicate with people!"

    menu:
        "Peter: I haven't been getting precise information from you guys either!":
            Dad "As I said, you need to ask more, confirm when in doubt! You can't always blame others!" 
            "(You had an argument with your father.)"
            "Stress ++ \n (Lecture from parent)"
            $ pressure += 2
            jump police_cert_event_part_2_option_1_end

        "Peter: Ah, sorry, Dad. It's my fault. I apologize; I don't have much social experience, and I didn't think things through. I won't make the same mistake next time.":
            Dad "It's okay, child. Everyone has a first time. I understand you, and you're much better than I was at your age. Take it slow. Just be more careful next time." 
            "Stress - \n (Affirmation from parent)"
            $ pressure -= 1
            jump police_cert_event_part_2_option_1_end

label police_cert_event_part_2_option_1_end:
    scene background store
    "(Peter returns to the County Police Department)"
    jump police_cert_event_part_2_continue



label police_cert_event_part_2_option_2:
    "(Peter goes through his paperwork to make sure everything is right)"
    jump police_cert_event_part_2_continue


label police_cert_event_part_2_continue:
    show peter normal at left
    Peter "I am applying for permanent residency in Country A. Is this really the document I need?"

    show cop normal at right
    Officer "It’s for a permanent residence application? I’m not sure…but I guess our Clearance Letter will work…just one second, let me double check."

    hide peter normal
    hide cop normal
    "(The officer goes through the paperwork)"
    "(...)"

    show cop normal at right
    Officer "Oh, I guess you are right. Good thing you asked this question. 
    Otherwise you will waste a lot of time. 
    The document you need is actually an Identity History Summary Check provided by the Federal Bureau of Investigation."

    show peter normal at left
    Peter "Sorry…you said Identity History Summary Check issued by…?"

    Officer "Federal Bureau of Investigation. The “FBI”."

    Peter "Ohh, Okok. So what should I do now?"

    Officer "You can fill out a form here and then we'll collect your fingerprints. 
    After that, you can send the documents to the address provided on their official website. 
    Then, you'll need to wait for their updates."

    Peter "Ok, thank you officer!"
    jump police_cert_event_part_2_end

label police_cert_event_part_2_end:
    scene background room
    "(Peter returns to his room and fills out the form)"
    "(A few days later, he is now certified)"
    
    #-----Set Police Cert Var
    $ police_cert_part_2 = True
    $ finished_police_cert = True

    jump move_to_next_chapter



label move_to_next_chapter:
    if(current_week == 3):
        jump week_4_start
    elif(current_week == 4):
        jump week_5_start
    elif(current_week == 5):
        jump week_6_start
    elif(current_week == 6):
        jump week_7_start
    elif(current_week == 2):
        jump week_3_start
    elif(current_week == 1):
        jump week_2_start


