import time
import keyboard

pause = False

def countdown(t):
    while (t):
        if (keyboard.is_pressed("p") == True): # if p is held down the timer pauses
            print("paused")
            time.sleep(1)
            if (secondAdded == False): # adds one second to account for issue of one second being deducted on pause
                t += 1
                secondAdded = True
            
        else:
            secondAdded = False
            mins, secs = divmod(t, 60) # converts secs to minutes and seconds
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
      
t = int(input("enter time in seconds: "))
countdown(t)

