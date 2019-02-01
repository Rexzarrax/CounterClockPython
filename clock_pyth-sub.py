import time
import os

from clock import Clock

#clears console   
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#program entry point
def main():
    #Set the time per increment and the maximum length the clock will run for
    Sleeper = 0.1
    maxLength = 86410 * 7

    myClock = Clock()

    print(myClock.DrawClock())

    for i in range(0, maxLength):
        time.sleep(Sleeper)
        cls()
        print("Python Clock")
        myClock.IncrementClockSec()
        print(myClock.DrawClock())

if __name__ == "__main__":
    main()

        

    


