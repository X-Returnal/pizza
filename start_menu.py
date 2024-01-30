"""
Start menu for pizza time
first scene when loaded
holds all logic for start menu
"""

def onEnter():
    return 0
    
def update(input):
    if input == "w":
        print("")
        return 1
    return 0
def draw_scene():
    #creates the current scene ui
    print("Pizza Time!")
    print("Type \"w\" then submit to start")