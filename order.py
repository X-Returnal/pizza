import pandas

order = [0,3]


def onEnter():
    #runs when user enter the room
    return [1]
def update(input):
    global order
    
    match order[0]:
        case 0:
            pass
        case 1:
            pass 
    return [1]
    
def draw_scene():
    global order
    match order[0]:
        case 0:
            if order[1] > 0:
                print(f"there are {order[1]} customer(s) waiting.")
                print("press \"e\" to take an order")
                print("\003")
        case 1:
            print(order)

