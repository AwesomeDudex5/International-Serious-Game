


screen mapPopoUp():
    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle"images/Mapicon.jpg"
        action ShowMenu("showmap")
screen showmap():
    add"images/BG art.png"xpos 0 ypos 0 xsize config.screen_width ysize config.screen_height

    imagebutton:
        xalign 0.75
        yalign 0.1
        xoffset -5
        yoffset 5
        idle "film"
        hover "film_hover"
        action Jump ("filmweekent")
    
    imagebutton:
        xalign 0.25
        yalign 0.2
        xoffset -5
        yoffset 5
        idle "House.png"
        hover "House Hover.png"
        action Jump ("houseweekent")

    
    imagebutton:
        xalign 0.55
        yalign 0.15
        xoffset -5
        yoffset 5
        idle "police station"
        hover "policestation_Hover.png"
        action Jump ("policeweekent")
    
    
    imagebutton:
        xalign 1
        yalign 0.75
        xoffset -5
        yoffset 5
        idle "hospital"
        hover "hospital_hover"
        action Jump ("hosptweekent")

    



    imagebutton:
        xalign 0.5
        yalign 0.75
        xoffset -5
        yoffset 5
        idle "Restaurant.png"
        hover "Restaurant Hover.png"
        action Jump ("restweekent")

    
    imagebutton:
        xalign 0.25
        yalign 0.65
        xoffset -5
        yoffset 5
        idle "school"
        hover "school_Hover.png"
        action Jump ("schoolweekent")


    
    imagebutton:
        xalign 1
        yalign 0.25
        xoffset -5
        yoffset 5
        idle "store"
        hover "store_Hover.png"
        action Jump ("storeweekent")

    
    imagebutton:
        xalign 0.85
        yalign 0.55
        xoffset -5
        yoffset 5
        idle "Dorm.png"
        hover "Dorm Hover.png"
        action Jump ("dormweekent")


