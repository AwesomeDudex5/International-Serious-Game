screen mapPopoUp():
    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle"images/Mapicon.jpg"
        action ShowMenu("showmap")
screen showmap():
    
    add "images/BG_art.png" xpos 0 ypos 0 xsize config.screen_width ysize config.screen_height
    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "images/returnIcon.jpg"
        action Return()
    
    #finded
    imagebutton:
        xalign 0.75
        yalign 1
        xoffset -2
        yoffset 2
        idle "hospital icon"
        hover "hospital icon selected" 
        action NullAction()
    #finded
    imagebutton:
        xalign 0.25
        yalign 0.75
        xoffset -2
        yoffset 2
        idle "film icon" 
        hover "film icon selected"
        action NullAction()

    imagebutton:
        xalign 0.1
        yalign 0.95
        xoffset -2
        yoffset 2
        idle "House Hover.png"
        hover "House.png" 
        action NullAction()
    
    
    #finded
    imagebutton:
        xalign 0.55
        yalign 0.75
        xoffset -2
        yoffset 2
        idle "police station icon"
        hover "police station icon selected" 
        action NullAction()

    imagebutton:
        xalign 0.95
        yalign 0.75
        xoffset -2
        yoffset 2
        idle "Restaurant Hover.png"
        hover "Restaurant.png" 
        action NullAction()

    
    #finded
    imagebutton:
        xalign 0.25
        yalign 1
        xoffset -2
        yoffset 2
        idle "school icon"
        hover "school icon selected" 
        action NullAction()
    
    
    imagebutton:
        xalign 0.55
        yalign 0.35
        xoffset -2
        yoffset 2
        idle "Dorm.png"
        hover "Dorm Hover.png" 
        action NullAction()
    
    #finded
    imagebutton:
        xalign 0.95
        yalign 0.25
        xoffset -2
        yoffset 2
        idle "store icon"
        hover "store icon selected" 
        action NullAction()
    
 
       
       
