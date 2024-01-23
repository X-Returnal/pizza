"""
Pizza Time
---------------
manange a virtual resteraunt by taking orders, working the kiction, running the checkout,
and manageing money and inventory 
---------------
will cantrell
"""
from ast import Try
from socket import timeout
from inputimeout import inputimeout, TimeoutOccurred
import userinput
import start_menu
import order
import mgnt
import kiction
import threading
import time
from os import system

roomid:int = -1
userinput = None

def update(uinput):
    system("cls")
    global roomid
    if roomid == -1:
        roomid = start_menu.onEnter()
    # run logic and create the next game frame
    if roomid == 0:
        start_menu.update(uinput)
    else:
        order.update(uinput)
    
    match roomid:
        case 0:
            start_menu.draw_scene()
    

while True:
    update(userinput)
    try:
        userinput = inputimeout(prompt=">> ", timeout = 1)
    except TimeoutOccurred:
        userinput = None