import time
import keyboard

running = True
timer = ""

def countdown(t):
        while (t):
            if (keyboard.is_pressed("p") == True): # if p is held down the timer pauses
                print("paused", end = '\r')
                time.sleep(1)
                if (secondAdded == False): # adds one second to account for issue of one second being deducted on pause
                    t += 1
                    secondAdded = True
                
            else:
                print("             ", end = "\r") # clears line
                secondAdded = False
                mins, secs = divmod(t, 60) # converts secs to minutes and seconds
                global timer
                timer = "{:02d}:{:02d}".format(mins, secs)
                #setTimer(timer);
                #print("timer from get statement: " + getTimer())
                print(timer, end = '\r')
                time.sleep(1)
                t -= 1

def getTimer(): #returns timer
    global timer
    return(timer)


while (running == True):
    t = int(input("enter time in seconds: "))
    countdown(t)
    print("Timer finished!!")
    answered = False

    while (answered == False):
        contProg = input("do you want to run again? (y/n): ")
        if (contProg == "y" or contProg == "Y"):
            print("restarting...")
            answered = True
        elif (contProg == "n" or contProg == "N"):
            print ("quitting...")
            answered = True
            running = False
        else:
            print("error, bad value, either y or n")
import time
import keyboard

running = True

while (running == True):
    def countdown(t):
        while (t):
            if (keyboard.is_pressed("p") == True): # if p is held down the timer pauses
                print("paused", end = '\r')
                time.sleep(1)
                if (secondAdded == False): # adds one second to account for issue of one second being deducted on pause
                    t += 1
                    secondAdded = True
                
            else:
                print("             ", end = "\r") # clears line
                secondAdded = False
                mins, secs = divmod(t, 60) # converts secs to minutes and seconds
                timer = "{:02d}:{:02d}".format(mins, secs)
                print(timer, end = '\r')
                time.sleep(1)
                t -= 1
        
    t = int(input("enter time in seconds: "))
    countdown(t)
    print("Timer finished!!")
    answered = False

    while (answered == False):
        contProg = input("do you want to run again? (y/n): ")
        if (contProg == "y" or contProg == "Y"):
            print("restarting...")
            answered = True
        elif (contProg == "n" or contProg == "N"):
            print ("quitting...")
            answered = True
            running = False
        else:
            print("error, bad value, either y or n")

