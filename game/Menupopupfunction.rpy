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
        xalign 0.1
        yalign 1
        xoffset -5
        yoffset 5
        idle "images/returnIcon.jpg"
        action Return()
    

    imagebutton:
        xalign 0.5
        yalign 1
        xoffset -5
        yoffset 5
        idle "hospital icon"
        hover "hospital icon selected"
        action NullAction()

    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "film icon"
        hover "film icon selected"
        action NullAction()

    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "film icon"
        hover "film icon selected"
        action NullAction()
    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "film icon"
        hover "film icon selected"
        action NullAction()

    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "film icon"
        hover "film icon selected"
        action NullAction()



    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "film icon"
        hover "film icon selected"
        action NullAction()

    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "film icon"
        hover "film icon selected"
        action NullAction()


    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "film icon"
        hover "film icon selected"
        action NullAction()