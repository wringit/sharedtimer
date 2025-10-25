import time;

def countdown(t):
    while (t):
        mins, secs = divmod(t, 60) # converts secs to minutes and seconds
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t-=1
        #print("result: " + str(t))

t = int(input("enter time in s: "))
countdown(t)