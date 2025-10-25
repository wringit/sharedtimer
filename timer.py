import time
import keyboard

pause = False

def countdown(t):
    while (t):
        if (keyboard.is_pressed("p") == True): # if p is held down the timer pauses
            print("paused")
            time.sleep(1) # issue: time still counts down for one second after p is held
        else:
            mins, secs = divmod(t, 60) # converts secs to minutes and seconds
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
      
t = int(input("enter time in seconds: "))
countdown(t)
