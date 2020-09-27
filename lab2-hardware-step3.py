from sense_emu import SenseHat

s = SenseHat()

print('Press right arrow for temperature to be displayed')
temp = 0
while True:
    events = s.stick.get_events()
    for event in events:
        if event.action == 'pressed':
            if event.direction == 'right':  
                print ('The temperature is', temp)
                temp += 1
    

