from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

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

def trinket_J():
    Y = yellow
    O = nothing
    J = [
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, O, O, Y, Y, O, O, O,
    O, O, O, Y, Y, O, O, O,
    O, O, O, Y, Y, O, O, O,
    O, O, O, Y, Y, O, O, O,
    O, Y, Y, Y, Y, O, O, O,
    O, Y, Y, Y, O, O, O, O,
    ]
    return J

def trinket_M():
    B = blue
    O = nothing
    M = [
    B, B, O, O, O, O, B, B,
    B, B, B, O, O, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, O, B, B, O, B, B,
    B, B, O, O, O, O, B, B,
    B, B, O, O, O, O, B, B,
    B, B, O, O, O, O, B, B,
    B, B, O, O, O, O, B, B,
    ]
    return M

def any_arrow(event):    
    
    images = [trinket_C, trinket_J, trinket_M]
    count = 0
    if event.action == 'pressed':
        while True: 
            s.set_pixels(images[count % len(images)]())
            time.sleep(.75)
            count += 1
        
s.stick.direction_any = any_arrow