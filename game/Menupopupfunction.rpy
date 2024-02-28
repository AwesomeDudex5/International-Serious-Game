screen mapPopoUp():
    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle"images/Mapicon.jpg"
        action ShowMenu("showmap")
screen showmap():
    add"images/sample map.png"

    imagebutton:
        xalign 0.5
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
        idle "kobe normal"
        hover "kobe tired"
        action NullAction()

    imagebutton:
        xalign 0
        yalign 1
        xoffset -5
        yoffset 5
        idle "mom normal"
        hover "mom normal"
        action NullAction()