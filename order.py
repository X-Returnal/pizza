import pandas as pd

order = [0,3]
ptypes = pd.read_csv("data/titanic.csv")
custchoices = ptypes[["Type"]]
def onEnter():
    #runs when user enter the room
    return [1]
def update(input):
    global order
    
    match order[0]:
        #counter
        case 0:
            pass
        #thinking customer (roll rng and create order)
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
            else:
                print("there are no customers waiting")
                
        case 1:
            print("The customer is thinking.")
            print("(Press enter to continue.)")

