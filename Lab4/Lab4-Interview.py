from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)

def trinket_C():
    G = green
    O = nothing
    C = [
    O, O, O, G, G, G, O, O,
    O, O, G, G, G, G, O, O,
    O, G, G, O, O, O, O, O,
    O, G, G, O, O, O, O, O,
    O, G, G, O, O, O, O, O,
    O, G, G, O, O, O, O, O,
    O, O, G, G, G, G, O, O,
    O, O, O, G, G, G, O, O,
    ]
    return C
    
    temp = 0

while True:
    events = s.stick.get_events()
    for event in events:
        if event.action == 'pressed':
            if event.direction == 'left':  
                s.set_pixels(trinket_C)
                
            if event.direction == 'right':
                print('The temperature is ' , temp)
