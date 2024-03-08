default weekstransfer = 0

label filmweekent:
    scene background room
    Dad "we have a great weekend in theater"
    jump weekcount


label dormweekent:
    scene background room
    Dad "we have a great weekend in another dorm"
    jump weekcount

label policeweekent:
    scene background room
    Dad "Why You go to plice station?"
    jump weekcount



label restweekent:
    scene background room
    Dad "we have a great meal on family resturant!"
    jump weekcount


label houseweekent:
    scene background room
    Dad "we have a great time with your family"
    jump weekcount

label hosptweekent:
    scene background room
    Dad "we go to hospital and check out you are perfect!"
    jump weekcount


label schoolweekent:
    scene background room
    Dad "School is close. but you still wnat to study...."
    jump weekcount
label storeweekent:
    scene background room
    Dad "Dad are shopping this weekend"
    jump weekcount

label gameEnd: 
    menu: 
        "This is the End of the game, Thanks for Playing":
            $ renpy.full_restart()



label weekcount:
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


