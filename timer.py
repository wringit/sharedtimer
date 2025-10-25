import time
import keyboard
import threading


running = True
timer = ""


def countdown(t, timer_name):
        while (t):
            if (keyboard.is_pressed("p") == True): # if p is held down the timer pauses
                print("paused", end = '\r')
                time.sleep(1)
                if (secondAdded == False): # adds one second to account for issue of one second being deducted on pause
                    t += 1
                    secondAdded = True
               
            else:
                print(f"{timer_name}: ", end="")


                print("             ", end = "\r") # clears line
                secondAdded = False
                mins, secs = divmod(t, 60) # converts secs to minutes and seconds
                global timer # we are using global timer
                timer = "{:02d}:{:02d}".format(mins, secs)
                #print("timer from get statement: " + getTimer())
                #print(timer, end = '\r')
                print(f"{timer_name}: {timer}")


                time.sleep(1)
                t -= 1
        print(f"\n{timer_name}: Timer finished!!")




def getTimer(): # returns timer
    global timer
    return(timer)


def start_multiple_timers(timer_values):
    threads = []
    # Create and start a new thread for each timer
    for timer_name, timer_value in timer_values.items():
        thread = threading.Thread(target=countdown, args=(timer_value, timer_name))
        threads.append(thread)
        thread.start()


    # Wait for all threads to finish
    for thread in threads:
        thread.join()




while (running == True):


    num_timers = int(input("How many timers do you want to create? "))
    timer_values = {}


    # Collect the starting time for each timer
    for i in range(num_timers):
        timer_name = f"Timer {i + 1}"
        start_time = int(input(f"Enter the starting time for {timer_name} in seconds: "))
        timer_values[timer_name] = start_time


    # Start all the timers concurrently
    start_multiple_timers(timer_values)






    '''t = int(input("enter time in seconds: "))
    countdown(t)
    print("Timer finished!!")'''
    answered = False


    while (answered == False):
        contProg = input("do you want to run again? (y/n): ")


        if (contProg == "y" or contProg == "Y"):
            print("restarting...")
            answered = True


        elif (contProg == "n" or contProg == "N"):
            print("quitting...")
            answered = True
            running = False


        else:
            print("error, bad value, either y or n")
