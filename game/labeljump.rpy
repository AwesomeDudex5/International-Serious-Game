default weekstransfer = 0

label filmweekent:
    scene background room
    $ pressure -= 2
    $ language_skill += 1
    Dad "we have a great weekend in theater"
    "stress - -, language + \n (watching a fun movie helps get used to the language)"
    jump weekcount


label dormweekent:
    scene background room
    Dad "we have a great weekend in another dorm"
    $ pressure -= 1
    "Stress - \n (Chilling in your room relaxes you)"
    jump weekcount

label policeweekent:
    scene background room
    if not finished_police_cert:
        "Going to the police station to get certification"
        jump weekcount_police
    else:
        Dad "Why You go to police station?"
        jump weekcount



label restweekent:
    scene background room
    Dad "we have a great meal on family resturant!"
    $ pressure -= 1
    "pressure - \n (Eating good food calms the soul)"
    jump weekcount


label houseweekent:
    scene background room
    Dad "we have a great time with your family"
    $ pressure -= 1
    "Stress - \n (Spending time with loved ones reduces stress)"
    jump weekcount

label hosptweekent:
    scene background room
    Dad "we go to hospital and check out you are perfect!"
    $ pressure += 1
    $ language_skill += 2
    "Stress - , Language + + \n (Appointments cause anxiety, got used to talking to staff)"
    jump weekcount


label schoolweekent:
    scene background room
    Dad "School is close. but you still want to study...."
    jump weekcount

label storeweekent:
    scene background room
    Dad "Dad are shopping this weekend"
    $ pressure -= 1
    $ language_skill += 1
    "Stress - , langauge + \n (Exploring the market can be fun, talking with staff improves language)"
    jump weekcount

label gameEnd: 
    menu: 
        "This is the End of the game, Thanks for Playing":
            $ renpy.full_restart()



label weekcount:
    $ weekend_map_start = False
    if weekstransfer ==0:
        $ weekstransfer+=1
        jump week_2_start
    if weekstransfer ==1:
        $ weekstransfer+=1
        jump week_3_start
    if weekstransfer ==2:
        $ weekstransfer+=1
        jump week_4_start
    if weekstransfer ==3:
        $ weekstransfer+=1
        jump week_5_start
    if weekstransfer ==4:
        $ weekstransfer+=1
        jump week_6_start
    if weekstransfer ==5:
        $ weekstransfer+=1
        jump week_7_start 
    if weekstransfer >5 :
        jump gameEnd

label weekcount_police:
    if weekstransfer ==0:
        $ weekstransfer+=1
        jump police_cert_event_start
    if weekstransfer ==1:
        $ weekstransfer+=1
        jump police_cert_event_start
    if weekstransfer ==2:
        $ weekstransfer+=1
        jump police_cert_event_start
    if weekstransfer ==3:
        $ weekstransfer+=1
        jump police_cert_event_start
    if weekstransfer ==4:
        $ weekstransfer+=1
        jump police_cert_event_start
    if weekstransfer ==5:
        $ weekstransfer+=1
        jump police_cert_event_start 
    if weekstransfer >5 :
        jump gameEnd


