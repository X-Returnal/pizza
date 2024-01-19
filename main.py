"""
Pizza Time
---------------
manange a virtual resteraunt by taking orders, working the kiction, running the checkout,
and manageing money and inventory 
---------------
will cantrell
"""

import userinput
import start_menu
import order
import mgnt
import kiction
import threading
import time
from os import system
roomid:int = -1



class RepeatEvery(threading.Thread):
    def __init__(self, interval, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.interval = interval  # seconds between calls
        self.func = func          # function to call
        self.args = args          # optional positional argument(s) for call
        self.kwargs = kwargs      # optional keyword argument(s) for call
        self.runable = True
    def run(self):
        while self.runable:
            self.func(*self.args, **self.kwargs)
            time.sleep(self.interval)
    def stop(self):
        self.runable = False





def update():
    system("cls")
    global roomid
    if roomid == -1:
        
        temp = start_menu.onEnter()
        
        roomid = temp
    # run logic and create the next game frame
    if roomid == 0:
        start_menu.update()
    else:
        order.update()
    
    match roomid:
        case 0:
            start_menu.draw_scene()
    

thread = RepeatEvery(1,update)

thread.start()
thread.join()