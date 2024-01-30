"""
Pizza Time
---------------
manange a virtual resteraunt by taking orders, working the kiction, running the checkout,
and manageing money and inventory 
---------------
will cantrell
"""
import start_menu
import order
import kiction
import mgnt
import checkout
from os import system

roomid:int = -1
prevroomid:int = -1
order_data = []
userinput = None

def update(uinput):
    system("cls")
    global roomid
    global prevroomid
    if roomid == -1:
        roomid = start_menu.onEnter()
        prevroomid = roomid
    #check if new room entered. if true, run on entered logic
    if prevroomid != roomid:
        match roomid:
            case 0:
                roomid = start_menu.onEnter()
            case 1:
                temp = order.onEnter()
                roomid = temp[0]



    # run logic and create the next game frame
    match roomid:
        case 0:
            roomid = start_menu.update(uinput)
        case 1:
            temp = order.update(uinput)
            roomid = temp[0]
        case _:
            print("no room here")
    
    match roomid:
        case 0:
            start_menu.draw_scene()
        case 1:
            order.draw_scene()
        
    prevroomid = roomid
    

while True:
    update(userinput)
    userinput = input(">> ")